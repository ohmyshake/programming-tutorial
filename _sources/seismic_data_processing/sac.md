# sac

- Author: *{{Fu}}*
- Update: *August 4, 2022*
- Reading: *30 min*

---

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



