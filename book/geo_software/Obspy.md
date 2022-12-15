# obspy

- Author: *{{Fu}}*
- Update: *August 5, 2022*
- Reading: *30 min*

---


## Event Data Process

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:38:21 2021
    sac 文件要求头文件内标记了发震时刻与震中距方位角信息
@author: yf
"""

import os
import glob
import obspy
import subprocess
import numpy as np
from obspy import Stream
from obspy.taup import TauPyModel
from obspy.taup.taup_create import build_taup_model
from math import sin,cos,pi
from obspy.core import UTCDateTime
from MCMTpy.utils.asdf_function import get_StationXML,Add_waveforms_head_info
from MCMTpy.utils.asdf_function import Add_waveforms,Add_stationxml,get_QuakeML,Add_quakeml



######################
def get_taup_tp_ts(model,depth,distance,degree=None):
    if degree==False:
        distance = distance/111.19

    time_p = model.get_travel_times(source_depth_in_km=depth,
                                    distance_in_degree=distance,
                                    phase_list=["p", "P"])

    time_s = model.get_travel_times(source_depth_in_km=depth,
                                    distance_in_degree=distance,
                                    phase_list=["s", "S"])

    ray_p = time_p[0].ray_param
    tp = time_p[0].time
    angle_p = time_p[0].incident_angle

    ray_s = time_s[0].ray_param
    ts = time_s[0].time
    angle_s = time_s[0].incident_angle

    return ray_p,tp,angle_p,ray_s,ts,angle_s



def rotate(data_raw,chn=['RTZ','ENZ']):
    '''
    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    chn : TYPE, optional
        DESCRIPTION. The default is ['RTZ','ENZ'].

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    data : TYPE
        DESCRIPTION.

    '''
    data = data_raw.copy()
    if ('R' in chn[0]) and ('T' in chn[0]) and ('Z' in chn[0]) and ('E' in chn[1]) and ('N' in chn[1]) and ('Z' in chn[1]):
        r_in_index = chn[0].index('R')
        t_in_index = chn[0].index('T')
        z_in_index = chn[0].index('Z')

        e_out_index = chn[1].index('E')
        n_out_index = chn[1].index('N')
        z_out_index = chn[1].index('Z')

        for i in range(0,len(data),3):
            BAZ = data[i].stats.back_azimuth/180*pi #float( baz )   # labels[9] 表示 asdf 文件中 baz 的值 Raw_data[chn].stats.asdf['labels'][9]
            R = data[i+r_in_index].data
            T = data[i+t_in_index].data
            Z = data[i+z_in_index].data
            E = -cos(BAZ)*T - sin(BAZ)*R
            N = sin(BAZ)*T - cos(BAZ)*R

            data[i+e_out_index].stats.channel='E'
            data[i+e_out_index].data = E
            data[i+n_out_index].stats.channel='N'
            data[i+n_out_index].data = N
            data[i+z_out_index].stats.channel='Z'
            data[i+z_out_index].data = Z

    elif ('E' in chn[0]) and ('N' in chn[0]) and ('Z' in chn[0]) and ('R' in chn[1]) and ('T' in chn[1]) and ('Z' in chn[1]):
        e_in_index = chn[0].index('E')
        n_in_index = chn[0].index('N')
        z_in_index = chn[0].index('Z')

        r_out_index = chn[1].index('R')
        t_out_index = chn[1].index('T')
        z_out_index = chn[1].index('Z')

        for i in range(0,len(data),3):
            BAZ = data[i].stats.back_azimuth/180*pi #float( baz )   # labels[9] 表示 asdf 文件中 baz 的值 Raw_data[chn].stats.asdf['labels'][9]
            E = data[i+e_in_index].data
            N = data[i+n_in_index].data
            Z = data[i+z_in_index].data
            R = -cos(BAZ)*N - sin(BAZ)*E
            T = sin(BAZ)*N - cos(BAZ)*E

            data[i+r_out_index].stats.channel='R'
            data[i+r_out_index].data = R
            data[i+t_out_index].stats.channel='T'
            data[i+t_out_index].data = T
            data[i+z_out_index].stats.channel='Z'
            data[i+z_out_index].data = Z

    else:
        raise ValueError('chn format error! abort!')

    return data
######################






#######################################################
################PARAMETER SECTION######################
#######################################################

#%% 1. data/file paths
RAWDATA       = "./YN.202105212148_MCMTpy_hpick"                              # dir where SAC files are located
allfiles_path = os.path.join(RAWDATA,'*sac')                                    # make sure all sac files can be found through this format


# 2. output data/file paths
Output_path   = "./YN.202105212148_MCMTpy_hpick_m_2"                                   # 输出文件存放的位置
source_name   = "source_enz"                                                    # asdf 文件的 source_tag
ASDF_filename = "YN.202105212148"                                               # asdf 文件的名称


# 3. 创建自己的速度模型，只有第一次需要 build_taup_model 计算走时表
taup_pick     = 'no'                                                           # select 'yes' to do Ray tracing with taup
v_model_path  = '../v_model/v_model.nd'
# build_taup_model(v_model_path, output_folder='../v_model', verbose=True)
model_path    = "../v_model/v_model.npz"


# 4. useful parameters
rotate_mode   = False                                                            # 是否要旋转分量
chn           = ['RTZ','ENZ']                                                   # rotate from chn[0] to chn[1]

freqmin       = 0.005                                                           # pre filtering frequency bandwidth (hz)
freqmax       = 2                                                               # note this cannot exceed Nquist frequency (hz)
samp_freq     = 5                                                               # targeted sampling rate (hz)
p_n0          = 100                                                              # P波到达前的采样点个数
npts          = 2048                                                            # 数据点长度(如果超过endtime,则按照endtime处理),trim时可能存在一个采样点的误差


# 5. event infomation (需要手动输入)
UTCtime       = UTCDateTime('2021-05-21'+'T'+'21:48:35.36'+'+08')               # 地震目录的时间都是北京时间，时区为 UTC+8，需要转换成 UTC 时间统一标准
nptime        = UTCtime.timestamp
year          = UTCtime.year
julday        = UTCtime.julday
hour          = UTCtime.hour
minute        = UTCtime.minute
second        = UTCtime.second
microsecond   = 0                                                               # UTCtime.microsecond, 请始终保持 0 
evla          = 25.682
evlo          = 99.881
evdp          = 17
mag           = 6.6





##################################################
# we expect no parameters need to be changed below

# assemble parameters for data pre-processing
prepro_para = {'RAWDATA':RAWDATA, 'allfiles_path':allfiles_path,\
               'Output_path':Output_path, 'source_name':source_name, 'ASDF_filename':ASDF_filename,\
               'taup_pick':taup_pick, 'v_model_path':v_model_path, 'model_path':model_path,\
               'freqmin':freqmin, 'freqmax':freqmax, 'samp_freq':samp_freq, 'p_n0':p_n0, 'npts':npts,\
               'UTCtime':UTCtime, 'evla':evla, 'evlo':evlo, 'evdp':evdp, 'mag':mag}
metadata = os.path.join(Output_path,'process_info.txt') 

# output parameter info
if not os.path.isdir(Output_path):os.mkdir(Output_path)
fout = open(metadata,'w')
fout.write(str(prepro_para))
fout.close()



##########################################################
#################PROCESSING SECTION#######################
##########################################################

#%% 0. sac 写入发震事件信息  (改成obspy更好！)
os.putenv("SAC_DISPLAY_COPYRIGHT", '0')                                         # 设置环境变量
cmd_sac = subprocess.Popen(['/Users/yf/1.Software/1.SAC/sac/bin/sac'], stdin=subprocess.PIPE, cwd=RAWDATA)         # 利用sac程序去除仪器响应 /Users/yf/1.Software/1.SAC/sac/bin/sac
s = ''
for sacfile in sorted(glob.glob(allfiles_path)):
    sac_name = sacfile.split('/')[-1]
    s += "r %s \n" % sac_name 
    s += "ch o gmt %s %s %s %s %s %s \n" % (year,julday,hour,minute,second,microsecond)  # 使用 sac 把发震时间写入头部变量 o 中
    s += "ch allt (0 - &1,o&) iztype IO \n"                                     # 将 发震时间 设置成 参考时间
    s += "ch evla %f evlo %f evdp %f mag %f\n" % (evla,evlo,evdp,mag)           # 写入事件位置
    s += "wh\n"

s += "q \n"

stdout, stderr = cmd_sac.communicate(s.encode())                                # Popen.communicate 命令会自带 Popen.wait(), 但保险起见还是需要自己添加 wait()命令
cmd_sac.wait()




#%% 1. obspy 读取原始数据 return: data
allfiles = sorted( glob.glob(allfiles_path) )
data_raw = Stream()

for i in range(0,len(allfiles),1):
    try:
        tr = obspy.read(allfiles[i])
        # print(tr[0].stats.sac.dist,tr[0].stats.sac.evdp)
        data_raw += tr
    except Exception:
        print(allfiles[i],': no such file or obspy read error');continue
data = data_raw.copy()




#%% 2. 读取台站的经纬度信息output "NET_STA" used in samole_dc.json and plot_dc.json

# 2.1 读取台站信息，并按照震中距排序
unique_stations = np.unique([tr.stats.station for tr in data])                  # 所有台站的名称 np.unique 去除重复元素

sta_num = unique_stations.shape[0]
NET_STA = np.empty(shape=(sta_num,6),dtype='object')                            # 创建空数组，类型是 object 可以包含字符和数字
for i in range(0,sta_num,1):
    tr = data.select(station=unique_stations[i])[0]                             # Just taking the first Trace if multiple
    NET_STA[i,0] = tr.stats.network
    NET_STA[i,1] = tr.stats.station
    NET_STA[i,2] = tr.stats.sac.stla
    NET_STA[i,3] = tr.stats.sac.stlo
    NET_STA[i,4] = 0                                                            # 台站的深度始终保持 0 
    NET_STA[i,5] = tr.stats.sac.dist

NET_STA = NET_STA[ NET_STA[:,5].argsort() ]                                     # 按照 dist 那一列排序


# 2.2 将 NET_STA 写入文件
fp = open('./NET_STA.txt', 'w')                                                 # "NET_STA" used in samole_dc.json and plot_dc.json
fp.write('[')
for i in range(0,sta_num,1):
    fp.write( str(NET_STA[i,0:5].tolist()) )
    fp.write(',')
    if i != (sta_num-1):
        fp.write('\n')
fp.write(']')
fp.close()

fp = open('./NET_STA_dist.txt', 'w')                                            # 包含震中距信息
fp.write('[')
for i in range(0,sta_num,1):
    fp.write( str(NET_STA[i,:].tolist()) )
    fp.write(',')
    if i != (sta_num-1):
        fp.write('\n')
fp.write(']')
fp.close()




#%% 3. taup射线追踪拾取到时
if taup_pick=='yes':
    model = TauPyModel(model=model_path)                                        # model_path 还可以是 "iasp91"  "prem"
    for i in range(0,len(data),1):
        depth = data[i].stats.sac['evdp']
        distance = data[i].stats.sac['dist']
        ray_p,tp,angle_p,ray_s,ts,angle_s = get_taup_tp_ts(model,depth,distance,degree=False)
        data[i].stats.sac["t1"]=tp                                              # 与 pyfk 标记方法一致，多了 ray_p ray_s
        data[i].stats.sac["user1"]=angle_p
        data[i].stats.sac["user3"]=ray_p
        data[i].stats.sac["t2"]=ts
        data[i].stats.sac["user2"]=angle_s
        data[i].stats.sac["user4"]=ray_s


# 3.1. 利用 taup 画 最后一个事件的 raypath
# if taup_pick=='yes':
#     path_p = model.get_ray_paths(source_depth_in_km=depth,
#                                   distance_in_degree=distance/111.19,
#                                 phase_list=["p", "P","s", "S"])
#     path_p[0].path.dtype
#     ax = path_p.plot_rays(plot_type="cartesian",legend=True)                    # 'spherical'  cartesian




#%% 4. 去均值去趋势
data.detrend(type='demean')
data.detrend(type='simple')
data.taper(max_percentage=0.05)





#%% 5. 滤波然后降采样 and 裁剪数据
# 5.1 滤波降采样
data.filter('bandpass', freqmin=freqmin, freqmax=freqmax, corners=4, zerophase=True)  # bandpass
data.resample(samp_freq,window='hanning',no_filter=True, strict_length=False)         # resample


# 5.2 裁剪每一个分量数据
for i in range(0,len(data),1):
    b = data[i].stats.sac['b']
    t1 = data[i].stats.sac['t1']
    t_start = data[i].stats.starttime + (t1-b) - p_n0/samp_freq
    # 判断数据长度 与 endtime 的关系
    t_end_npts = t_start+npts/samp_freq
    t_endtime = data[i].stats.endtime
    if t_end_npts > t_endtime:
        t_end = t_endtime
    else:
        t_end = t_end_npts

    data[i].trim(t_start, t_end)


# 5.3 把三分量数据裁成一样长
for i in range(0,round(len(data)/3)):
    t_start_1 = data[3*i].stats.starttime
    t_start_2 = data[3*i+1].stats.starttime
    t_start_3 = data[3*i+2].stats.starttime
    t_end_1 = data[3*i].stats.endtime
    t_end_2 = data[3*i+1].stats.endtime
    t_end_3 = data[3*i+2].stats.endtime
    t_start = max(t_start_1,t_start_2,t_start_3)
    t_end = min(t_end_1,t_end_2,t_end_3)
    data[3*i:3*i+3].trim(t_start, t_end)


# 5.4 转换波形数据的范围，去除仪器响应的单位是 velocity(nm/s), fk用的单位是 velocity(cm/s)
for i in range(0,len(data),1):
    data[i].data = 1e6*data[i].data




#%% 6. 旋转到 ENZ 方向
if  rotate_mode == True:
    for i in range(0,len(data)):
        data[i].stats.back_azimuth = data[i].stats.sac.baz
    data_enz = rotate(data=data,chn=chn)                                        # 反方位角需要有定义 data[i].stats.back_azimuth
else:
    data_enz = data




#%% 7. 输出 ASDF 与 sac 文件
source_lat   = data_enz[0].stats.sac.evla
source_lon   = data_enz[0].stats.sac.evlo
source_depth = data_enz[0].stats.sac.evdp
source_time  = data_enz[0].stats.starttime + data_enz[0].stats.sac.b            # UTCDateTime()

Output_file_path = os.path.join(Output_path, ASDF_filename+'.h5')
catalog_create   = get_QuakeML(source_name, source_lat, source_lon, source_depth,source_time)
Add_quakeml(Output_file_path,catalog_create)

Station_num = round(len(data_enz)/3)
for i in range(0,Station_num,1):                                                # 循环所有台站，写 ASDF 文件
    net_sta_name     = data_enz[3*i].stats.network+'_'+data[3*i].stats.station
    station_network  = data_enz[3*i].stats.network
    station_name     = data_enz[3*i].stats.station
    station_lat      = data_enz[3*i].stats.sac.stla
    station_lon      = data_enz[3*i].stats.sac.stlo
    station_depth    = 0
    station_distance = data_enz[3*i].stats.sac.dist
    station_az       = data_enz[3*i].stats.sac.az
    station_baz      = data[3*i].stats.sac.baz
    tp               = data_enz[3*i].stats.sac.t1
    ts               = data_enz[3*i].stats.sac.t2
    stream           = data_enz[3*i:3*i+3].copy()
    starttime        = data_enz[3*i].stats.starttime
    time_before_first_arrival = p_n0/samp_freq

    inv=get_StationXML(station_network, 
                       station_name,
                       station_lat, 
                       station_lon, 
                       station_depth, 
                       'enz')                                                   # 生成台站元

    # Add_waveforms_head_info([stream],
    #                         station_network,
    #                         station_name,
    #                         'enz',
    #                         starttime)                                        # 修改头文件中 channel 的信息顺序，变成 E/N/Z 顺序 (该版本不需要)

    print("now syn sac "+station_network+'_'+station_name+':\n')
    print('lat:',station_lat,'   lon:',station_lon)
    print(stream)
    print('\n\n')

    Add_waveforms([stream], 
                  catalog_create,
                  Output_file_path,
                  source_name,
                  tp,
                  ts,
                  station_distance,
                  station_az,
                  station_baz)                                                  # 添加波形

    Add_stationxml(inv,
                   Output_file_path)                                            # 添加台站元

    # stream.plot()

    for j in range(0,3,1):                                                      # 输出 sac 文件
        CHN = stream[j].stats.channel
        sac_filename = os.path.join(Output_path,source_name+'.'+station_network+'.'+station_name+'.'+CHN+'.sac')
        stream[j].write(sac_filename, format='SAC')

```

