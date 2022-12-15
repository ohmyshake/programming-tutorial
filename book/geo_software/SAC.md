# sac

- Author: *{{Fu}}*
- Update: *August 4, 2022*
- Reading: *30 min*

---


 <!-- seed2sac  sac2mseed cutevent -->



## Read and Write

The `SAC` wildcard is the same as the `Unix` wildcard, and contains only the following three types

- `*`: matches a string of any length (including zero length)

- `?`: matches any single non-null character

- `[]`: matches any single character in the list
    - `[ABC]` or `[A,B,C]` matches a single character A or B or C
    - `[0-9]` matches any digit from 0 to 9
    - `[a-g]` matches any single character in the range from a to g


**read:**

```bash
$ sac
 SEISMIC ANALYSIS CODE [07/17/2022 (Version 102.0)]
 Copyright 1995 Regents of the University of California

SAC> r cdv.n cdv.e cdv.z

SAC> r cdv.?                
./cdv.e ...cdv.n ...cdv.z   # attention! Here the file is read in character sort order

SAC> r cdv.[nez]
./cdv.e ...cdv.n ...cdv.z

SAC> r *   
./cdv.e ...cdv.n ...cdv.z

SAC> r more ./cdv.e         # one MORE file, and do not delete the past files in memory
```


**write:**

```bash
SAC> w test.n test.e test.z        # write into 3 new files

SAC> w over                        # overwrite the original disk files

SAC> wh                            # only overwrite the `header` parameters to the disk files

SAC> w append .new                 # add ".new" to the original file name
cdv.e.new cdv.n.new cdv.z.new
```


## Phase Pick


```bash
SAC> qdp off
SAC> ppk p 9        # plot 9 trances together
# 键入"t"和"0"标记到时，然后按"q"退出ppk模式
SAC> wh 
```
|    Command       |    Function    |      
| :------------:    | :-------------: |
| `b` | previous figure |
| `n` | next figure  |
| `x` | zoom in  |
| `o` | zoom out  |
| `q` | quit  |
| `t` | mark phase time |

## Data Process


```python
import os
import glob
import subprocess

#%% parameters
file_path = './'
f1 = 0.001  # remove instrument response then filter
f2 = 0.003
f3 = 2.1
f4 = 2.3
delta = 0.2  # downsample to 0.2s
evla = 10.0
evlo = 10.0
evdp = 10.0
mag = 5.0

#%% run
os.putenv("SAC_DISPLAY_COPYRIGHT", '0')  # set ernvironment variable
cmd_sac = subprocess.Popen(['sac'], stdin=subprocess.PIPE, cwd=file_path)
s = ''
for sacfile in sorted(glob.glob(os.path.join(file_path,'*.SAC'))):
    s += "r %s \n" % sacfile 
    s += "rmean; rtr; taper \n" 
    s += "ch evla %f evlo %f evdp %f mag %f\n" % (evla,evlo,evdp,mag)
    s += "wh\n"
    s += "trans from polezero s SAC.PZs to vel freq %f %f %f %f\n" % (f1,f2,f3,f4)   # remove response to velocity records
    s += "mul 1.0e9 \n" 
    s += "lp c %f \n" % (1/(2*delta))
    s += "interpolate delta %f \n" % delta
    s += "w over \n"
s += "q \n"

stdout, stderr = cmd_sac.communicate(s.encode())  # Popen.communicate will auto with Popen.wait(), but add wait() by yourself in case
cmd_sac.wait()
```



## Install rseed




## rseed to sac

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:16:39 2021
    参考网页：https://docs.python.org/zh-cn/3/library/subprocess.html
    命令：subprocess.Popen 本质是创建一个子进程，主（父）进程是调用它的Python程序。子进程创建完成后，父进程会继续执行子进程后面的程序而不管
        子进程有没有执行结束。所以可以阻塞父进程，等待子进程结束再执行后面的语句，使用Popen.wait()函数命令，使之变成串行程序。
        subprocess.call()函数自带阻塞功能。

    Python 中使用 subprocess 模块的 Popen 方法调用 SAC，通过 p.communicate() 
    将命令 s.encode() 传递给 SAC

    1. os.putenv("SAC_DISPLAY_COPYRIGHT", '0') 
        # a. 设置环境变量 SAC_DISPLAY_COPYRIGHT 的值为 0，这样就不用打印启动sac程序的欢迎页面了

    2. p = subprocess.Popen(["sac"], stdin=subprocess.PIPE, stdout=open('dirtest.txt','w'))  
        # a. stdin=subprocess.PIPE表示标准输入通过管道p.communicate输入
        # b. stdout=open('dirtest.txt','w')表示将标准输出到一个文本文件中,也可以使用subprocess.PIPE这个时候就不会打印到屏幕了，
            而是托管到第三方PIPE下面，不打印到主进程下
        # c. ["sac"]列表第一个字符串表示要执行的命令程序，列表后面的字符串表示该命令程序的输入

    3. p.communicate(s.encode()) 
        # a. p.communicate表示向 stdin 发送数据，或者从stdout和stderr中读取数据（参数stdin必须
            被设置为PIPE。同样，如果希望从stdout和stderr获取数据，必须将stdout和stderr设置为PIPE）
        # b. s.encode() 表示指定字符串s的编码格式

    4. 利用系统的 Shell 命令执行时，需要确保 shell=True，第一个变量例如 cmd_cat 就是shell格式下命令字符串.cwd='/'用于设置该子进程
        执行的路径。
       注意：系统的shell命令有自己的通配符正则化形式，所以这里的*会起到通配符的作用，第1、2、3中的通配符*将不起作用，会解释为字符串*
       cmd_cat = 'cat %s >> %s' % ('*_PZs_*','SAC.PZs1')  # shell命令的字符串格式
       subprocess.Popen(cmd_cat, shell=True,cwd='/')  # 利用Popen执行shell命令
       或者 subprocess.Popen('cat *_PZs_* >> SAC.PZs1', shell=True,cwd='/')

    5. a=subprocess.getstatusoutput('MCMTpy -h') 返回在 shell 中执行 cmd 产生的 (exitcode, output)

    6. subprocess.Popen(['rdseed', '-pdf',seed_name],cwd=file_path) 注意 seed_name 只能用相对路径，
       因为popen命令只会找当前路径下的文件名称，该文件名称不包含路径信息


@author: yf
"""

import os 
import subprocess
import glob
import shutil 
import pandas as pd
import numpy as np
from obspy.core import UTCDateTime


'''
该程序会将 file_path 的 seed 文件全部解压成sac，并去除仪器响应添加到 output_path 目录下

'''


############################
## 1. 输入参数 (路径必须是全英文，否则 subprocess.Popen 会报错)

# file_path = './1_three_earthquke'
file_path = './2_M_more_than_4/yunnan_network'                                 # 输入文件夹路径 yunnan_network  ||  instability_network
output_path = './sac_data'                                                      # 输出文件路径

readme_file = os.path.join(output_path,'readme')                                # 输出 logging 文件路径

rm_old_output_path = True                                                       # 是否删除已经存在的 output_path 文件夹，如果想处理多个 file_path 时，请保持 False

f1 = 0.001                                                                      # 去除仪器响应希望的滤波范围, 先去除仪器响应，再降采样
f2 = 0.003
f3 = 2.1
f4 = 2.3

delta = 0.2                                                                     # 降采样到 0.2s




############################
## 2. 读取地震目录信息
df = pd.read_excel('./fast_20210601232138.xls')
catalog_raw = df.values                                                         # pandas 转成 numpy

# catalog_new format: UTCtime/lat/lon/dep/mag
catalog_new = np.zeros(shape=catalog_raw.shape)
for i in range(0,catalog_raw.shape[0]):
    UTCtime = UTCDateTime(catalog_raw[i,0]+'T'+catalog_raw[i,1]+'+08')          # 地震目录的时间都是北京时间，时区为 UTC+8，需要转换成 UTC 时间统一标准
    nptime = UTCtime.timestamp
    lat = catalog_raw[i,2]
    lon = catalog_raw[i,3]
    dep = catalog_raw[i,4]
    mag = catalog_raw[i,5]

    catalog_new[i,0] = nptime
    catalog_new[i,1] = lat
    catalog_new[i,2] = lon

    ## 地震深度可能不存在，设成999
    try:
        catalog_new[i,3] = float(dep)
    except:
        catalog_new[i,3] = 999

    ## 地震震级可能不存在，设成999
    try:
        catalog_new[i,4] = float(mag)
    except:
        catalog_new[i,4] = 999



############################
## 3. rdseed to sac
seed_path = sorted(glob.glob( os.path.join(file_path,'*.seed') ))               # *.seed

if rm_old_output_path:                                                          # remove old output_path
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
if os.path.exists(output_path) == False:                                          # mkdir new output_path
    os.makedirs(output_path)

fp = open(readme_file, 'w')
for i in range(0,len(seed_path)):
    seed_name = seed_path[i].split('/')[-1]                                     # seed_name的时间是北京时间，只精确到分钟

    ### a.rdseed
    cmd_rdseed = subprocess.Popen(['rdseed', '-pdf',seed_name], cwd=file_path)   # rdseed 解压文件, 注意 seed_name 只能用相对路径，因为popen命令只会找当前路径下的文件名称，该文件名称不包含路径信息
    cmd_rdseed.wait()


    ### b.cat
    cmd_cat = subprocess.Popen('cat *_PZs_* >> SAC.PZs', shell=True, cwd=file_path) # 合并单个seed文件所有的仪器响应文件
    cmd_cat.wait()

    ### b.1 将 rdseed 生成的原始 sac 文件保存起来
    output_seed_path = os.path.join(output_path,'RAW_SAC',seed_name)
    if os.path.exists(output_seed_path)==False:                                 # mkdir new output seed path
        os.makedirs(output_seed_path)

    for file in glob.glob(file_path+'/*.SAC'):                                  # cp sac
        file_name = file.split('/')[-1]
        out_name = os.path.join(output_seed_path,file_name)
        shutil.copyfile(file, out_name)

    PZ_file = os.path.join(file_path,'SAC.PZs')                               # cp SAC.PZs
    shutil.copyfile(PZ_file, os.path.join(output_seed_path,'SAC.PZs'))


    ### c.sac
    os.putenv("SAC_DISPLAY_COPYRIGHT", '0')                                     # 设置环境变量
    cmd_sac = subprocess.Popen(['sac'], stdin=subprocess.PIPE, cwd=file_path)   # 利用sac程序去除仪器响应 /Users/yf/1.Software/1.SAC/sac/bin/sac
    s = ''
    for sacfile in sorted(glob.glob(os.path.join(file_path,'*.SAC'))):
        sac_name = sacfile.split('/')[-1]                                       # sac_name的时间是UTC时间，精确到毫秒

        year = int(sac_name.split('.')[0])                                      # 通过sac文件名称读取时间，后续可以修改成读取 sac 的头部变量
        julday = int(sac_name.split('.')[1])
        hour = int(sac_name.split('.')[2])
        minute = int(sac_name.split('.')[3])
        second = int(sac_name.split('.')[4])
        UTCtime = UTCDateTime(year=year, julday=julday, hour=hour, minute=minute, second=second) 
        nptime = UTCtime.timestamp

        evla = 0; evlo = 0; evdp = 0; mag = 0
        for j in range(catalog_new.shape[0]):
            if abs(catalog_new[j,0]-nptime) < 60:                               # 精确到60秒, 因为sac文件开始记录的时间不是地震开始时刻，seed文件对秒进行舍入到分钟
                evla = catalog_new[j,1]
                evlo = catalog_new[j,2]
                evdp = catalog_new[j,3]
                mag = catalog_new[j,4]
                break

        s += "r %s \n" % sac_name 
        s += "rmean; rtr; taper \n" 
        s += "ch evla %f evlo %f evdp %f mag %f\n" % (evla,evlo,evdp,mag)
        s += "wh\n"
        s += "trans from polezero s SAC.PZs to vel freq %f %f %f %f\n" % (f1,f2,f3,f4)   # 去完仪器响应变成速度记录 to vel
        s += "mul 1.0e9 \n" 
        s += "lp c %f \n" % (1/(2*delta))
        s += "interpolate delta %f \n" % delta
        s += "w over \n"
    s += "q \n"

    stdout, stderr = cmd_sac.communicate(s.encode())                            # Popen.communicate 命令会自带 Popen.wait(), 但保险起见还是需要自己添加 wait()命令
    cmd_sac.wait()


    ### d.write logging readme
    if (evla==0) and (evlo==0) and (evdp==0) and (mag==0):                      # 判断该seed事件，是否在地震目录中找到
        fp.write('not_find_in_catalog:   '+seed_name)
        fp.write('\n')
    else:
        fp.write('catalog_time:\t')                                             # 判断该seed事件,存在地震目录
        fp.write(str(UTCDateTime(catalog_new[j,0]))+'\t')
        fp.write('sac_time:\t')
        fp.write(str(UTCDateTime(nptime))+'\t')
        fp.write('difference_time:\t')
        fp.write(str(catalog_new[j,0]-nptime)+'\t')
        fp.write('\n')


    ### e.remove file
    if (evla==0) and (evlo==0) and (evdp==0) and (mag==0):
        output_seed_path = os.path.join(output_path,'no_event_'+seed_name)      # 没有地震目录的文件夹名称
        if os.path.exists(output_seed_path)==False:                             # mkdir new output seed path
            os.makedirs(output_seed_path)
    else:
        output_seed_path = os.path.join(output_path,seed_name)
        if os.path.exists(output_seed_path)==False:                             # mkdir new output seed path
            os.makedirs(output_seed_path)

    for file in glob.glob(file_path+'/*.SAC'):                                  # cp
        file_name = file.split('/')[-1]
        out_name = os.path.join(output_seed_path,file_name)
        shutil.copyfile(file, out_name)

    for file in glob.glob(file_path+'/*.SAC'):                                  # remove sac file
        os.remove(file)
    for file in glob.glob(file_path+'/SAC_PZs_*'):                              # remove PZs file
        os.remove(file)
    os.remove(file_path+'/SAC.PZs')                                             # remove SAC.PZs


fp.close()






#%% 可能用到的命令：

############################
### python os 修改路径
# pwd_path = os.getcwd()
# os.chdir(file_path)   # 进入需要操作的文件夹，rdseed 程序在此文件夹下生成sac数据
# os.chdir(pwd_path)

### Popen stdout 输出到文件
# log = open('some file.txt', 'a')
# log.write('some text, as header of the file\n')
# log.flush()  # <-- here's something not to forget!
# c = subprocess.Popen(['dir', '/p'], stdout=log, stderr=log, shell=True)

### os shutil python对文件的操作
# shutil.copytree('./data_sac_1') # 拷贝整个文件夹文件
# shutil.copyfile("oldfile","newfile") # 拷贝单个文件
# shutil.rmtree('./data_sac_1') # 删除该目录下所有文件
# os.remove("aa.txt") # 删除文件
# os.mkdir('要清空的文件夹名') # 创建文件夹 创建单个目录
# os.makedirs("/Users/ximi/version") # 创建多级目录
# os.path.exists() # # 检验给出的路径是否真地存
```

