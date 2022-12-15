---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# PyGMT

- Author: *{{Fu}}*
- Update: *July 30, 2022*
- Reading: *10 min*

---

## Introduction


[PyGMT](https://github.com/GenericMappingTools/pygmt) is a library for processing geospatial and geophysical data and making publication quality maps and figures. It provides a Pythonic interface for the [Generic Mapping Tools (GMT)](https://github.com/GenericMappingTools/gmt), a command-line program widely used in the Earth Sciences.



## Installation
It's recommended to install `Pygmt` into `base` environment.

:::::{tab-set}
::::{tab-item} conda

Simple installation using conda:
```bash
$ conda install --channel conda-forge pygmt
```
::::

::::{tab-item} mamba
If you use mamba:
```bash
$ mamba install --channel conda-forge pygmt
```
::::
:::::



## Data Set Config
<!-- 269.69 -->

The directory that GMT automatically downloads the data file from the server is `~/.gmt/server`. About the detailed info, please check [GMT Chinese Manual about Geodata set session](https://docs.gmt-china.org/latest/dataset/usage/#gmt)

**Mirror**
    
The `GMT` data server currently has multiple [mirrors](https://www.generic-mapping-tools.org/mirrors/) around the world. 
Run the following command to set your mirror channel:

```bash
# If you are in China
$ gmt set GMT_DATA_SERVER http://china.generic-mapping-tools.org

# If you are in US West Coast
$ gmt set GMT_DATA_SERVER http://sdsc-opentopography.generic-mapping-tools.org

# Show URL of the remote GMT data server
$ gmt --show-dataserver
```
Then the above command will generate a `gmt.conf` file in your current path, copy it to the `GMT` user directory `~/.gmt`.




**GMT Built-in Data**

- [GSHHG: Global high-resolution shoreline data](https://docs.gmt-china.org/latest/dataset/gshhg/): includes coastlines, rivers and borders.

- [DCW: Digital Chart of the World](https://docs.gmt-china.org/latest/dataset/dcw/): includes the boundary of seven continents, the boundary of 250 countries or regions in the world, and the provincial/state boundary of 8 major countries.





**GMT Romote Data**

- [Earth_relief](https://docs.gmt-china.org/latest/dataset/earth-relief/): global relief data, automatically download into `~/.gmt/server/earth/earth_relief` directory
- [Earth_age](https://docs.gmt-china.org/latest/dataset/earth-age/): the age of the earth's oceanic crust, automatically download into `~/.gmt/server/earth/earth_age` directory
- More info please check [GMT Chinese Manual ...](https://docs.gmt-china.org/latest/dataset/#id2)

I have downloaded the `Earth_relief` dataset into `~/.gmt/server/earth/earth_relief` directory, with the resolution is `30s` which equal to `1 kilometer`(size of ~778M). Download data by the following command `gmt get`:

```bash
$ gmt get -Ddata=earth_relief -I30s
```

**Custom Data**

Users can also customize their own database directory to store their own data in it, compared with the default directory `~/.gmt/server`. My database directory is `~/data/GMTDB/`, add the following lines into your configuration file.

```bash
$ vim ~/.zshrc
# >>> pygmt(base) initialize >>>
export GMT_DATADIR=/Users/yinfu/data/GMTDB/
# <<< pygmt(base) initialize <<<
```
 
Then you can check the whether it has successed:

```bash
# Show full path of user's ~/.gmt dir
$ gmt --show-userdir

# Show directory/ies with user data.
$ gmt --show-datadir
```



## My Data List

:::{toggle}
|    Name       |    From       |   Directory  |     
| ------------  | ------------- | :----------: |
| `Earth_relief with 30s`   | GMT remote data       |  `~/.gmt/server/earth/earth_relief`    |
| ``   | ...       |  `~/data/GMTDB/`    |

:::



## Parameters Setting


Please check [GMT Chinese Manual about parameter configuration](https://docs.gmt-china.org/latest/conf/overview/)


`pygmt` use `pygmt.config` to set the default parameters.

```python
import pygmt

pygmt.config(PARAMETER = value)
```
 




## MAP


### 2021 Yangbi Earthquake Map

```{code-cell} python
:tags: [hide-input]
"""
Created on Tue May 25 22:44:49 2021

@author: yf
"""

import pygmt
import numpy as np
import os,glob,obspy
from obspy import Stream
from obspy.taup import TauPyModel
from obspy.taup.taup_create import build_taup_model


#%% 1. data/file paths
allfiles_path = os.path.join('./pygmt_files/yangbi/*.SAC')             # 某个地震事件的文件夹，通配所有SAC数据
limiting_sta = ['XG.CHT','XG.HDQ','XG.XBT','XG.ZYT','YN.TUS','YN.YUX']         # 限幅的台站名称

#%% 2.读取原始数据 return: data
allfiles = sorted( glob.glob(allfiles_path) )
data_raw = Stream()
for i in range(0,len(allfiles),1):
    tr = obspy.read(allfiles[i])
    data_raw += tr
data = data_raw.copy()

#%% 3.读取台站的经纬度信息
lons = []; lats = []; net = []; sta = []; names = []
unique_stations = np.unique([tr.stats.station for tr in data])                  # 所有台站的名称
for station in unique_stations:
    tr = data.select(station=station)[0]                                        # Just taking the first Trace if multiple
    lons.append(tr.stats.sac.stlo)
    lats.append(tr.stats.sac.stla)
    net.append(tr.stats.network)
    sta.append(tr.stats.station)
    names.append(f'{tr.stats.network}.{tr.stats.station}')                      # 所有台站台网的名称
evlo = tr.stats.sac.evlo # 地震位置
evla = tr.stats.sac.evla


# 3.1 Determine a nice, padded region
# region = [np.min(lons), np.max(lons), np.min(lats), np.max(lats)]
# x_pad = (region[1] - region[0]) * 0.1
# y_pad = (region[3] - region[2]) * 0.1
# region = [region[0] - x_pad, region[1] + x_pad, region[2] - y_pad, region[3] + y_pad]
region = [96.5, 107, 21, 29.5]                                                    # 手动指定 region 范围

# 3.2 Determine a nice stereographic projection
lon_0 = np.mean(region[:2])
lat_0 = np.mean(region[2:])
if lat_0 > 0:
    ref_lat = 90
else:
    ref_lat = -90
projection = f'S{lon_0}/{ref_lat}/6i'
# projection = f'M{lon_0}/{lat_0}/6i'


#%% 4. pygmt plot
fig = pygmt.Figure()                                                            # Create figure
# 4.1 画行政边界图
fig.coast(region=region,                                                        # pygmt coast
          projection=projection,
          shorelines=True,
          water='lightblue',
          land='lightgrey',
          borders=[1, 2],
          frame=['a2',"WSEN"])

# # 4.2 画台站图
for i in range(0,len(names),1):
    if names[i] in limiting_sta:
        color = 'red'
        legend_red_index = i
    else:
        color = 'blue'
        legend_blue_index = i
    fig.plot(x=lons[i],                                                                  # pygmt plot 画台站
              y=lats[i],
              style='i0.1i',
              color=color,
              pen=True)

# 4.3 画legend需要的label
fig.plot(x=lons[legend_red_index],                                                                  # pygmt plot 画台站
          y=lats[legend_red_index],
          style='i0.1i',
          color='red',
          pen=True,
          label="Clipped_data+S0.25c")                                                                     # lagend 里面必须得加_,否则把空格当成文件，会报错
fig.plot(x=lons[legend_blue_index],                                                                  # pygmt plot 画台站
          y=lats[legend_blue_index],
          style='i0.1i',
          color='blue',
          pen=True,
          label="Normal_data+S0.25c")

# 4.4 标注台站名称 
fig.text(text=names,                                                            # pygmt text 台站名称
          x=lons,
          y=lats,
          xshift ='0.2c',
          yshift ='0.2c',
          font="5p,Helvetica-Bold,white",
          fill="orange",
          transparency=20)

# 4.5 画地震的五角星
fig.plot(x=evlo,                                                                  # pygmt plot 画台站
          y=evla,
          style='a0.3i',
          color='yellow',
          pen=True,)

# 4.6 画震源机制
focal_mechanism = dict(strike=138, dip=76, rake=-170, magnitude=6.7)            # store focal mechanisms parameters in a dict
fig.meca(focal_mechanism,                                                       # pygmt meca 画沙滩球
          scale="1.0c",
          longitude=98.5,
          latitude=26.6,
          depth=12.0,
          G='red')

# 4.7 画 箭头
fig.plot(x=evlo, 
          y=evla, 
          style="v0.3c+eA+a30", 
          direction=([145], [1.6]), 
          pen="0.8p"
          )

# 4.8 添加图例
fig.legend(spec=None, position="JTR+jTR+o1.5c/0.7c", box='+gwhite+p0.5p')

# 4.9 画插图
with fig.inset(position="jTL+w3c/2.3c+o1.0c/0.5c", box="+pblack"):
    # Use a plotting function to create a figure inside the inset
    fig.coast(
        region=[70, 135, 15, 55],
        projection="M105/42.5/3c",  #"M3c",
        land="white",
        borders=[1, 2],
        shorelines="1/thin",
        water="white",
        # Use dcw to selectively highlight an area
        # dcw="US.MA+gred",
    )
    
    fig.plot(x=tr.stats.sac.evlo,                                                                  # pygmt plot 画台站
          y=tr.stats.sac.evla,
          style='a0.15i',
          color='red',
          pen=True,)

#%% 5 保存图片
# fig.savefig("STA_location_yangbi.pdf")                                             # pygmt savefig 保存图片
fig.show()
```









### Dayindian Water reservoir

**Make grd files:**

```bash
range=99.0/102.0/24.0/27.5
gmt grdsample ./topo_data/srtm_57_07.asc -I0.0005 -Gtmp.grd -R$range
gmt grdgradient tmp.grd -Gtmp.ient -A0/270 -Ne0.5
gmt makecpt -Chaxby -Z -T-1000/4000/100 > tmp.cpt
```

**Pygmt plot:**

```{code-cell} ipython3
:tags: [hide-input]
"""
Created on Tue May 25 22:44:49 2021
    1. run S1_get_cpt_grd.sh first.
    2. run this script
    
@author: yf
"""
import pygmt
import numpy as np
import os,glob
from obspy.core import UTCDateTime

#%% 1.Set config
fig = pygmt.Figure()
pygmt.config(FONT_ANNOT_PRIMARY="10p")  # 设置字体大小,define fig = pygmt.Figure() first
pygmt.config(MAP_FRAME_TYPE="fancy")
pygmt.config(MAP_FRAME_WIDTH="0.15c")  # 设置地图边界粗细
pygmt.config(FORMAT_GEO_MAP="ddd.xx")  # 设置经纬度格式
pygmt.config(MAP_TICK_PEN_PRIMARY="1.5p,black") # 控制比例尺的线及刻度属性


#%% 2.Plot main fig
region = [100.345, 100.66, 25.70, 25.91]
projection = 'M100.5/25.75/6i'
fig.basemap(region=region, projection=projection,frame=['a0.1',"WSen"])    # a后面加lat/lon的间隔

### a.grimage
# pygmt.makecpt(cmap="haxby", series=[1000, 4000])  # not used, use external cpt now
fig.grdimage(
    grid = "./pygmt_files/dayindian/tmp.grd",
    shading = "./pygmt_files/dayindian/tmp.ient",
    cmap = "./pygmt_files/dayindian/tmp.cpt",
    # region=region,
    # projection=projection,
    # frame='a0.2',
)
fig.colorbar(
    # Colorbar position justified outside map frame (J) at Middle Right (MR),
    # offset (+o) by 1 cm horizontally and 0 cm vertically from anchor point,
    # with a length/width (+w) of 7 cm by 0.5 cm
    cmap="./pygmt_files/dayindian/tmp.cpt",
    position="JMR+o0.7c/-2c+w7c/0.5c",  # mu表示单位放在下面
    frame=["xa500f250", "y+l(m)"],
    truncate = "1000/3000",  # 截断表示 从1000m至4000m
    scale=1,
)
# replot map_scale
fig.basemap(region=region, projection=projection,frame=['a0.1',"WSen"],map_scale="g100.62/25.72+c25.7+w2k+u")    # a后面加lat/lon的间隔

### b.fault
fig.plot(#data="../files/dayindian/fault/CN-faults.gmt",
         data="./pygmt_files/dayindian/fault/fault_paper.txt",
         region=region, # 必须添加，否则断层会画出界
         pen="1.5p,red")

# create space-delimited file
with open("./pygmt_files/dayindian/fault/faultname_paper.txt", "w") as f:
    f.write("100.40 25.705 5 8p,Helvetica-Bold,gray30 CM Honghegu\n")
    f.write("100.58 25.865 55 8p,Helvetica-Bold,gray30 CM Yongsheng-Binchuan\n")

fig.text(textfiles="./pygmt_files/dayindian/fault/faultname_paper.txt", angle=True, font=True, justify=True)

# cleanups
os.remove("./pygmt_files/dayindian/fault/faultname_paper.txt")


### c.seismicity
time_bd = UTCDateTime("2012-09-07T12:15:00")
earthquakes_path = './pygmt_files/dayindian/seismicity/20080106-20211121.txt'
s1_lats = []; s1_lons = []; s1_M = []; s1_t = []
s2_lats = []; s2_lons = []; s2_M = []; s2_t = []
with open(earthquakes_path,'r',encoding='ISO-8859-1') as f:
    for line in f:
        try:
            t = UTCDateTime(line.split()[0])
            lat = float(line.split()[2])
            lon = float(line.split()[3])
            M = float(line.split()[6])
            if M < 10:
                if time_bd<=t:
                    s1_t.append(t)
                    s1_lats.append(lat)
                    s1_lons.append(lon)
                    s1_M.append(M)
                else:
                    s2_t.append(t)
                    s2_lats.append(lat)
                    s2_lons.append(lon)
                    s2_M.append(M)
        except:
            continue
# before time_bd
fig.plot(x=s1_lons,
         y=s1_lats,
         size=np.array(s1_M)*0.03,
         style="c",
         color="148/0/211",
         pen="0.25p,148/0/211")
# after time_bd
fig.plot(x=s2_lons,
         y=s2_lats,
         size=np.array(s2_M)*0.03,
         style="c",
         color="255/0/255",
         pen="0.25p,255/0/255")


### d.reservoir
fig.plot(data="./pygmt_files/dayindian/reservoir_shape/dayindian_reservoir_shape",
         pen="0.2p,blue",
         color="blue")

fig.text(text="Reservoir",
          x=100.507,
          y=25.793,
          font="10p,Helvetica-Bold,blue",
          transparency=30)


### e.station
sta_lat_lon_path = './pygmt_files/dayindian/sta_lat_lon/sta_lat_lon_select.txt'
Red_sta = ['53263','53265']         # 红色的台站
lats = []; lons = []; names = []
with open(sta_lat_lon_path,'r') as f:
    for line in f:
        line.strip()
        sta_name = line.split()[0]
        lon = float(line.split()[1])
        lat = float(line.split()[2])
        names.append(sta_name)
        lats.append(lat)
        lons.append(lon)

for i in range(0,len(names),1):
    if names[i] in Red_sta:
        color = 'red'
    else:
        color = 'black'
    if (lons[i]<region[1]) & (lons[i]>region[0]) & (lats[i]<region[3]) & (lats[i]>region[2]):
        fig.plot(
            x=lons[i],
            y=lats[i],
            style='t0.15i',
            color=color,
            pen=True)

fig.text(text=names,
          x=lons,
          y=lats,
          xshift ='0.0c',
          yshift ='-0.25c',
          font="7p,Helvetica-Bold,black",
          )


#%% 3.Inset
with fig.inset(position="jTL+w6c+o-0.3c/-1.6c",margin="0.5c"): #  box="+pblack"
    pygmt.config(MAP_FRAME_WIDTH="0.1c")
    # a.basemap
    fig.basemap(region=[70.0, 130.0, 10.0, 40.0], 
                projection="B100/5/10/40/?",
                frame=['a15',"wsen"])
    
    # b.coast
    fig.coast(
        # region=[70.0, 130.0, 10.0, 40.0],
        # projection="B100/5/10/40/?",  #"M3c",
        # frame = ['a10',"wsen"],
        land="white",
        shorelines="0.1p,black",
        # area_thresh = 1000,
        water="white",
        # borders=1,
        )
    
    # c.plate_boundary
    fig.plot(data="./pygmt_files/dayindian/plate_boundary/India_Eurasia",
         pen="0.5p,red",
         style="f0.5/6p+t+l",
         color = "red")
    fig.plot(data="./pygmt_files/dayindian/plate_boundary/Philippin_Eurasia",
         pen="0.5p,red",
         style="f0.5/6p+t+l",
         color = "red")
    
    # d.text
    fig.text(text=["INDIA","CHINA"],                                                            # pygmt text 台站名称
          x=[79,108],
          y=[22,31],
          xshift ='0.0c',
          yshift ='0.0c',
          font="8p,Helvetica-Bold,black",
          )
    fig.text(text=["Bengal Bay","South China Sea"],                                                            # pygmt text 台站名称
          x=[88,114],
          y=[16,16],
          xshift ='0.0c',
          yshift ='0.0c',
          font="4p,Helvetica-Bold,black",
          transparency=20)
    
    # e.start
    fig.plot(x=100.500534,
             y=25.809124,
             pen="0.1p,green",
             style="a0.5c",
             color = "green")

#%% 4.Legend
### a.set legend
leg = """
### station
S 0.5c t 0.2i black 1.0p 2.0c  Seismic Stations
G -1l
S 1.2c t 0.2i red 1.0p 2.0c 
G -1l

### reservoir
S 9.6c a 0.5c green 1.0p,green 10.8c  Dayindian Reservoir
G 0.2c

### faults
S 0.8c - 0.5i - 1.5p,red 2.0c  Faults
G -1l

### boundary
S 9.6c f0.5/6p+l+t 0.3i red 1.0p,red 10.8c  Plate Boundary
G 0.2c

### m1
S 0.3c c 0.03c 148/0/211 0.25p 2.0c  Before Impoundment (Mb: 1~5)
G -1l
S 0.8c c 0.09c 148/0/211 0.25p
G -1l
S 1.4c c 0.15c 148/0/211 0.25p
G -1l

### m2
S 9.1c c 0.03c 255/0/255 0.25p 10.8c  After Impoundment (Mb: 1~5)
G -1l
S 9.6c c 0.09c 255/0/255 0.25p
G -1l
S 10.2c c 0.15c 255/0/255 0.25p
"""

### b.write temporary file
fout = open("./pygmt_files/dayindian/tmp.legend", 'w')
fout.write(leg)
fout.close()

### c.legend
fig.legend(spec="./pygmt_files/dayindian/tmp.legend", position="x-0.1c/-2.5c+w6.2i+l1.2+jBL", box='+gwhite+p0.5p')

#%% 5.Save fig
fig.show()
# fig.savefig("STA_location.pdf")
```



## Velocity Model

### Longmen mountain


```{code-cell} ipython3
:tags: [hide-input]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:50:49 2022

@author: yf
"""

import pygmt
import numpy as np

Vs_path = './pygmt_files/longmen/Vs.xyz'
Reloc_path = './pygmt_files/longmen/cd.reloc'

dep=[0.00,  0.200,  0.400,  0.600,  0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.5, 3, 4, 5, 6, 7, 8, 9 ]
start=[[103.67,31.36], [103.6,31.26], [103.47,31.25], [103.4,31.18], [103.34,31.1], [103.28,30.95]]
end=[[104.07,30.96], [104,30.86], [103.87,30.85], [103.8,30.78], [103.74,30.7], [103.68,30.55]]

region=[103.2, 104.1, 30.5, 31.4]

# 1. read data
data = np.loadtxt(Vs_path)

dep_info = [0]
for i in range(1,len(data)):
    if data[i][2] != data[i-1][2]:
        dep_info.append(i)
dep_info.append(len(data))

reloc = np.loadtxt(Reloc_path)
reloc_all=[]
for i in range(0,len(start)):
    data1=np.vstack((reloc[:,2], reloc[:,1],reloc[:,3])).T
    earthquakes = pygmt.project(data=data1, center=start[i], endpoint=end[i], convention='xyz', width='-0.05/0.05')
    reloc_all.append(earthquakes)

# 2. track lines info
track_lines = []
for i in range(0,len(start)):  # loop lines    
    track_all=[]
    for j in range(0,len(dep_info)-1):  # loop depth
        points = pygmt.project(center=start[i], endpoint=end[i], generate='0.02')
        pygmt.surface(
            x=data[dep_info[j]:dep_info[j+1],0], 
            y=data[dep_info[j]:dep_info[j+1],1], 
            z=data[dep_info[j]:dep_info[j+1],3],
            region=region,
            nodata="o9999",
            spacing="0.02",
            outgrid="../files/longmen/sample.nc")
        track = pygmt.grdtrack(points=points, grid="../files/longmen/sample.nc", newcolname="vs")
        track_all.append( [np.array(track.r), np.array(track.s), dep[j]*np.ones(len(np.array(track.r))), np.array(track.vs)]  )
    # print("i=",i,"\n")
    track_lines.append(track_all)

# 4. colorbar
pygmt.makecpt(cmap="jet",reverse=True, background=True, series=[2.2, 3.7, 0.01],output="../files/longmen/temp_cpt.cpt")

# 3. plot fig
fig = pygmt.Figure()
with fig.subplot(
    nrows=3,
    ncols=2,
    figsize=("25c", "11c"),
    autolabel=True,
    frame=["af", "WSne"],
    margins=["0.1c", "0.2c"],
    # title="My Subplot Heading",
):
    
    for i in range(0,len(start)):  # loop lines 
        # a. 剖面的信息
        Lon=[]
        Lat=[]
        Dep=[]
        Vs=[]
        for j in range(0,len(dep_info)-1):
            lon=track_lines[i][j][0].tolist()
            lat=track_lines[i][j][1].tolist()
            dep=track_lines[i][j][2].tolist()
            vs=track_lines[i][j][3].tolist()
            Lon=Lon+lon
            Lat=Lat+lat
            Dep=Dep+dep
            Vs=Vs+vs
        # Lon.reverse()
        # Lat.reverse()
        # Dep.reverse()
        # Vs.reverse()
        # b. 剖面插值
        pygmt.surface(
            x=Lon, 
            y=Dep, 
            z=Vs,
            region=[start[i][0], end[i][0], 0, 9],
            nodata="o9999",
            spacing="0.002/0.1",
            outgrid="./pygmt_files/longmen/sample1.nc"
            )
        # c.剖面画图
        with pygmt.config(
            PS_PAGE_ORIENTATION='landscape', 
            PROJ_LENGTH_UNIT='inch', 
            MAP_FRAME_TYPE='plain', 
            MAP_TICK_LENGTH='0.0c', 
            MAP_FRAME_PEN='2p', 
            FONT_ANNOT_PRIMARY='10p,Helvetica,black', 
            FONT_HEADING='15p,Helvetica,black', 
            FONT_LABEL='8p,Helvetica,black'):

            xx=i//2
            yy=i%2
            fig.basemap(
                zsize='-4i',
                region=[start[i][0], end[i][0], 0, 9], 
                projection='X10c/-3c',
                frame=['xafg+l"Longtitude"','yafg+l"Depth (km)"'],
                panel=[xx, yy])

            fig.grdimage(
                # img_in='D',
                projection='X10c/-3c', 
                region=[start[i][0], end[i][0], 0, 9], 
                grid="./pygmt_files/longmen/sample1.nc",
                cmap="./pygmt_files/longmen/temp_cpt.cpt",
                )
            
            fig.plot(x=reloc_all[i][0], y=reloc_all[i][2], no_clip=False,style='c0.1c',color="black",pen=True,panel=[xx, yy])

fig.colorbar(cmap="./pygmt_files/longmen/temp_cpt.cpt",position="JMB+o4c/1c+w8c", frame=["xa0.5f0.25", 'y+l"Vs (km/s)"'])
fig.show()
# fig.savefig('yf.pdf')

```



## Earthquake Source

### Lune

```{code-cell} ipython3
:tags: [hide-input]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:41:09 2022

@author: yf
"""

import os
import pygmt
import lune
import numpy as np
import xarray as xr
import MomentTensor as MTpy

#%%# 1. input parameters
path='./pygmt_files/lune/'
MPI_n = 20                       # total MPI cores
chain_n = 1                     # total chain in each core
N =  0                           # from N to compute in each chain

marker = [["DC",0,0,"0.4c/0.4c"], ["CLVD",-30,0,"-0.6c/0c"], ["CLVD",30,0,"0.6c/0c"],
          ["ISO",0,-90,"0.0c/-0.3c"], ["ISO",0,90,"0.0c/0.3c"], 
          ["LVD",-30,35,"-0.5c/0c"], ["LVD",30,-35,"0.5c/0c"],
          ["_",-30,-55,"-0.3c/0c"], ["_",30,55,"0.3c/0c"], 
          ["C(nu=0.25)",-30,60,"-1.1c/0c"], ["C(nu=0.25)",30,-60,"1.1c/0c"]]

#%% 2. read data
# all
Misfit_np = np.array([])
Mxx_np = np.array([]); Mxy_np = np.array([]); Mxz_np = np.array([])
Myy_np = np.array([]); Myz_np = np.array([]); Mzz_np = np.array([])
for i in range(0,MPI_n,1):
    rank_path = os.path.join(path,'rank_'+str(i)+'_output')
    for j in range(0,chain_n,1):
        FM_path = os.path.join(rank_path,'chain_'+str(j)+'_FM_2_accept_all')
        MISFIT_path = os.path.join(rank_path,'chain_'+str(j)+'_MISFIT_2_accept_all')
        # 2-d
        FM = np.loadtxt(FM_path)[N:,:]
        Mxx_np = np.hstack((Mxx_np, FM[:,1]))
        Mxy_np = np.hstack((Mxy_np, FM[:,2]))
        Mxz_np = np.hstack((Mxz_np, FM[:,3]))
        Myy_np = np.hstack((Myy_np, FM[:,4]))
        Myz_np = np.hstack((Myz_np, FM[:,5]))
        Mzz_np = np.hstack((Mzz_np, FM[:,6]))
        # 1-d
        MISFIT = np.loadtxt(MISFIT_path)[N:]
        Misfit_np = np.hstack((Misfit_np,MISFIT))

# mean
FM_mean_NED = np.array([np.mean(Mxx_np), 
                    np.mean(Myy_np),
                    np.mean(Mzz_np),
                    np.mean(Mxy_np), 
                    np.mean(Mxz_np), 
                    np.mean(Myz_np), ])
FM_mean_USE = MTpy.mt_convert(FM_mean_NED, old="NED", new="USE")


#%% 3. compute gamma and delta
# lam = lune.lune2lam(gamma, delta, M0)
Lsort,Vsort = lune.eig(lune.mat(FM_mean_USE))
gamma_mean, delta_mean, M0 = lune.lam2lune(Lsort)
focal_mechanism = np.hstack((gamma_mean,delta_mean,10,FM_mean_USE,22)) # depth = 10 in [lon, lat, depth, MT_USE, exp]

gamma_all=[]; delta_all=[]
for i in range(0,len(Mxx_np)):
    FM = [Mxx_np[i], Myy_np[i], Mzz_np[i], Mxy_np[i], Mxz_np[i],  Myz_np[i]]
    lsort,vsort = lune.eig(lune.mat(FM))
    gamma, delta, M0 = lune.lam2lune(lsort)
    gamma_all.append(gamma)
    delta_all.append(delta)

H, lon, lat = np.histogram2d(gamma_all,delta_all, bins=(20, 20),density=True)
H = H/np.max(H)

data = xr.DataArray(
    data=H.T,
    dims=["lat", "lon"],  # do not mix up the order of lat and lon
    coords=dict(
        lon=(["lon"], lon[0:-1]),
        lat=(["lat"], lat[0:-1]),
    ),
    attrs=dict(
        description="Statistical diagram",
        units="degree",
    ),
)


#%% 4. gmt plot
fig = pygmt.Figure()

xyzdata = pygmt.grd2xyz(data)
xyzdata_np = xyzdata.to_numpy()
pygmt.makecpt(cmap="hot",reverse=True, series=[0, 1, 0.02],output="../files/lune/temp_cpt1.cpt")

with pygmt.config(
        PS_PAGE_ORIENTATION='landscape', 
        PROJ_LENGTH_UNIT='inch', 
        MAP_FRAME_TYPE='plain', 
        MAP_TICK_LENGTH='0.0c', 
        MAP_FRAME_PEN='2p', 
        FONT_ANNOT_PRIMARY='12p,Helvetica,black', 
        FONT_HEADING='18p,Helvetica,black', 
        FONT_LABEL='10p,Helvetica,black'):

    # 1.basemap with lune
    fig.basemap(
                region=[-30,30,-90,90], 
                projection='H0/2.8i', 
                frame="wesn+g255/255/245")

    # 2.contour lines
    fig.contour(
        projection='H0/2.8i',
        x=xyzdata_np[:,0],
        y=xyzdata_np[:,1],
        z=xyzdata_np[:,2],
        levels= "./pygmt_files/lune/temp_cpt1.cpt",
        no_clip=True,
        # annotation=0.2,
        I=True,
        )

    # 3.focal mechanism
    fig.meca(focal_mechanism,
          scale="1.0c",
          longitude=gamma_mean,
          latitude=delta_mean,
          convention='mt',
          component ="full",
          G='red')


    # 4.lines
    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_01.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_02.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_03.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_04.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_05.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')
    
    x,y = np.genfromtxt('./pygmt_files/lune/dfiles/sourcetype_arc_06.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')


    # 5.marker
    for i in range(0,len(marker)):
        text=marker[i][0]
        x=marker[i][1]
        y=marker[i][2]
        offset=marker[i][3]
        fig.text(text=text,x=x,y=y,offset=offset,no_clip=True,font="10p,Helvetica-Bold,black")
        fig.plot(x=x, y=y, no_clip=True,style='c0.2c',color="black",pen=True)


#%% 5.save
fig.colorbar(cmap="./pygmt_files/lune/temp_cpt1.cpt",yshift="-0.5c",frame=["xa0.2f0.1", "y+l(marginal-posterior)"], )
fig.show()
# fig.savefig('lune_us.pdf')

```




### Hudson Plot

```{code-cell} ipython3
:tags: [hide-input]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:11:29 2021

@author: yf
"""


import matplotlib.pyplot as plt
import numpy as np
import os
from obspy.imaging.mopad_wrapper import beach
from matplotlib import cm
import MomentTensor as MTpy







#%%# 1. input parameters
FM_path='./pygmt_files/lune/'

MPI_n=20
N = 2000  # 从多少开始计算解

interval = 100




#%% 2. read data
FM_accept_list = []
for i in range(0,MPI_n,1):
    rank_path = os.path.join(FM_path,'rank_'+str(i)+'_output/chain_0_FM_2_accept_all')
    FM_accept = np.loadtxt(rank_path)[N:,:]
    FM_accept_list.append(FM_accept)

max_len = max(len(row) for row in FM_accept_list)
# min_len = min(len(row) for row in FM_accept_list)


FM_all_list = []
for i in range(0,max_len,1):
    # print(i)
    for j in range(0,MPI_n,1):
        len_mpi_n = len(FM_accept_list[j])
        if i < len_mpi_n:
            FM_all_list.append(FM_accept_list[j][i])




FM_all = np.array(FM_all_list)
FM_raw = FM_all[N:,1:7]   # 
Mxx_np = FM_raw[:,0]
Mxy_np = FM_raw[:,1]
Mxz_np = FM_raw[:,2]
Myy_np = FM_raw[:,3]
Myz_np = FM_raw[:,4]
Mzz_np = FM_raw[:,5]
FM = np.vstack((Mxx_np,  Myy_np,  Mzz_np,  Mxy_np,  Mxz_np,  Myz_np)).T

FM_mean=np.zeros(shape=(6))
for i in range(0,6,1):
    FM_mean[i]=np.mean(FM[0:,i])



#%% 3. plot Hudson
fig1, ax1 = plt.subplots(1 ,1,  dpi=800)

# plt.rc('font',family='Times New Roman')
MTpy.Hudson_plot(ax=ax1)
for i in range(0,len(FM),interval):  #len(FM)
    # print(i)
    MT = MTpy.MTensor(FM[i,:])
    M=MT.mt

    k,T = MTpy.M2kT_space(M)
    U,V = MTpy.kT2UV_space(k,T)
    
    map_vir = cm.get_cmap(name='YlGn')
    colors = map_vir(i/len(FM))
    # print(colors)
    ax1.scatter(U,V, color=colors,marker='o', s=1, alpha=0.5)  #  edgecolors='g'



#%% 4. plot mean beachball
MT = MTpy.MTensor(FM_mean)
M=MT.mt
k,T = MTpy.M2kT_space(M)
U,V = MTpy.kT2UV_space(k,T)                                                     # 求出平均值beachball 所在的位置

Length_Ball = 0.2
beach1 = beach(FM_mean, xy=(U,V),  linewidth=0.5,width=Length_Ball, alpha=0.7,\
                facecolor='r',bgcolor='w', edgecolor='k',mopad_basis='NED',nofill=False,zorder=1 )
ax1.add_collection(beach1) 
ax1.set_aspect("equal")





#%% 5. 设置colorbar
position=fig1.add_axes([0.85, 0.15, 0.01, 0.5])                                #   [0.15, 1.02, 0.25, 0.015]是colorbar的位置，分别表示左、下、长度、宽度（所占fig的比例）
font_colorbar = {'family' : 'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 6,
        }
sm = cm.ScalarMappable(cmap=map_vir)                                            #   map_vir是当前的colorbar的类型
sm.set_array(np.arange(0,len(FM)+1))                                                   #   设置colorbar的纵坐标轴数值变化范围
cb=plt.colorbar(sm,cax=position,orientation='vertical')                       #   ’orientation‘表示水平放置坐标轴  'horizontal'
cb.set_label('Sample Number',fontdict=font_colorbar)

ax1.set_xlim(-4/3-0.1, 4/3+0.3)
ax1.set_ylim(-1-0.1, 1+0.1)




#%%# 6. save figure
# fig.show()
# plt.title("hudson_plot")
# figurename=os.path.join('./Hudson_plot.png')
# plt.savefig(figurename,dpi=100, format="png")

```










### Beachball

```{code-cell} ipython3
:tags: [hide-input]


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:11:29 2021

@author: yf
"""


import matplotlib.pyplot as plt
import numpy as np
import os
import obspy
import glob
from obspy import Stream
from obspy.taup import TauPyModel
from obspy.taup.taup_create import build_taup_model
from obspy.imaging.mopad_wrapper import beach
import MomentTensor as MTpy
from matplotlib import cm


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

######################



#%%# 1. input parameters
FM_path='./pygmt_files/lune/'

MPI_n=20
N = 2000  # 从多少开始计算解

interval = 1000




#%% 2. read data
FM_accept_list = []
for i in range(0,MPI_n,1):
    rank_path = os.path.join(FM_path,'rank_'+str(i)+'_output/chain_0_FM_2_accept_all')
    FM_accept = np.loadtxt(rank_path)[N:,:]
    FM_accept_list.append(FM_accept)

max_len = max(len(row) for row in FM_accept_list)
# min_len = min(len(row) for row in FM_accept_list)


FM_all_list = []
for i in range(0,max_len,1):
    # print(i)
    for j in range(0,MPI_n,1):
        len_mpi_n = len(FM_accept_list[j])
        if i < len_mpi_n:
            FM_all_list.append(FM_accept_list[j][i])

# FM = np.array(FM_all_list)




FM_all = np.array(FM_all_list)
FM_raw = FM_all[N:,1:7]   # 
Mxx_np = FM_raw[:,0]
Mxy_np = FM_raw[:,1]
Mxz_np = FM_raw[:,2]
Myy_np = FM_raw[:,3]
Myz_np = FM_raw[:,4]
Mzz_np = FM_raw[:,5]
FM = np.vstack((Mxx_np,  Myy_np,  Mzz_np,  Mxy_np,  Mxz_np,  Myz_np)).T


FM_mean=np.zeros(shape=(6))
for i in range(0,6,1):
    FM_mean[i]=np.mean(FM[0:,i])



#%% 3.read station
allfiles_path=os.path.join('./pygmt_files/yangbi/*.SAC')
allfiles = sorted( glob.glob(allfiles_path) )
data_raw = Stream()
for i in range(0,len(allfiles),1):
    try:
        tr = obspy.read(allfiles[i])
        # print(tr[0].stats.sac.dist,tr[0].stats.sac.evdp)
        data_raw += tr
    except Exception:
        print(allfiles[i],': no such file or obspy read error');continue
        # raise ValueError('no such rawfile! please double check!')
data = data_raw.copy()
data.filter('bandpass', freqmin=0.005, freqmax=0.5, corners=4, zerophase=True)  # bandpass


v_model_path  = './pygmt_files/yangbi/v_model//v_model.nd'
# build_taup_model(v_model_path, output_folder='./', verbose=True)
model_path    = "./pygmt_files/yangbi/v_model//v_model.npz"
model = TauPyModel(model=model_path)    # "iasp91"  "prem"
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






#%% 4.plot 平均震源机制解
# ax0 = plt.gca()
fig, ax0 = plt.subplots(1 ,1,  dpi=800)
Length_Ball = 100
beach1 = beach(FM_mean, xy=(50, 50),  linewidth=1,width=Length_Ball-1, alpha=0.2,\
                facecolor='k',bgcolor='w', edgecolor='k',mopad_basis='NED',nofill=False,zorder=1 )
ax0.add_collection(beach1) 
ax0.set_aspect("equal")


## .plot 蒙特卡洛震源机制解
# for i in range(0,FM.shape[0],interval):
#     # print(i)
#     map_vir = cm.get_cmap(name='YlGn')
#     colors = map_vir(i/len(FM))
#     beach1 = beach(FM[i,0:6], xy=(50, 50),  linewidth=0.05,width=Length_Ball-1, alpha=0.5,\
#                 facecolor='g',bgcolor='w', edgecolor=colors, mopad_basis='NED',nofill=True,zorder=1 )
#     ax0.add_collection(beach1) 
#     ax0.set_aspect("equal")


## .plot 画背景线
# beach1 = beach(FM_mean, xy=(50, 50),  linewidth=1,width=Length_Ball-1, alpha=1,\
#                 facecolor='w',bgcolor='w', edgecolor='k',mopad_basis='NED',nofill=True,zorder=1 )
# ax0.add_collection(beach1) 
# ax0.set_aspect("equal")


## .plot 在沙滩球上画台站和波形
menthod='schmidt'   # 'schmidt'  # 'wulff'

for i in range(0,len(data),3):
    AZM = data[i].stats.sac['az'] 
    TKO = data[i].stats.sac['user1']
    net_sta_name = data[i].stats.network+'_'+data[i].stats.station
    
    X, Y = MTpy.project_beachball(AZM, TKO, R=Length_Ball/2, menthod=menthod)
    
    tt=np.linspace(X, X+10, num=len(data[i].data)) 
    ax0.plot(X, Y, "rv", ms=10,zorder=1) 
    # ax0.plot(tt, 5*data[i].data/0.01 + Y,  color='black',lw=0.2,alpha=0.6,zorder=1)
    ax0.text(X, Y,net_sta_name,horizontalalignment='right', verticalalignment='center',\
          fontsize=5, color='black',bbox = dict(facecolor = "r", alpha = 0.0),zorder=1) 



#%%# 5.标注保存
# MT = str_dip_rake2MT(strike=FM_mean[0],dip=FM_mean[1],rake=FM_mean[2])
MT = MTpy.MTensor(FM_mean)
Dec = MTpy.Decompose(MT)
Dec.decomposition_iso_DC_CLVD()   # Dec.help()
Dec.print_self()

T_axis, P_axis, N_axis = MTpy.MT2TPN(MT)
T = MTpy.vector2str_dip(T_axis)
P = MTpy.vector2str_dip(P_axis)
N = MTpy.vector2str_dip(N_axis)

Tx, Ty = MTpy.project_beachball(AZM=T.strike, TKO=(90-T.dip), R=Length_Ball/2, menthod=menthod)
ax0.text(Tx,Ty,'T',horizontalalignment='center', verticalalignment='center',\
          fontsize=20, color='k',alpha=0.7,zorder=1) 

Px, Py = MTpy.project_beachball(AZM=P.strike, TKO=(90-P.dip), R=Length_Ball/2, menthod=menthod)
ax0.text(Px,Py,'P',horizontalalignment='center', verticalalignment='center',\
          fontsize=20, color='k',alpha=0.7,zorder=1) 

Nx, Ny = MTpy.project_beachball(AZM=N.strike, TKO=(90-N.dip), R=Length_Ball/2, menthod=menthod)
ax0.text(Nx,Ny,'N',horizontalalignment='center', verticalalignment='center',\
          fontsize=20, color='k',alpha=0.7,zorder=1) 




#%%# 6. save figure
plt.title("beachball")

# 设置colorbar
position=fig.add_axes([0.85, 0.15, 0.01, 0.5])                                #   [0.15, 1.02, 0.25, 0.015]是colorbar的位置，分别表示左、下、长度、宽度（所占fig的比例）
font_colorbar = {'family' : 'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 6,
        }
sm = cm.ScalarMappable(cmap=map_vir)                                            #   map_vir是当前的colorbar的类型
sm.set_array(np.arange(0,len(FM)+1))                                                   #   设置colorbar的纵坐标轴数值变化范围
cb=plt.colorbar(sm,cax=position,orientation='vertical')                       #   ’orientation‘表示水平放置坐标轴  'horizontal'
cb.set_label('Sample Number',fontdict=font_colorbar)


ax0.set_xlim(0,100)
ax0.set_ylim(0,100)
ax0.set_axis_off() 
# fig.show()
figurename=os.path.join('./pygmt_files/lune/beachball_project.pdf')
plt.savefig(figurename,dpi=800, format="pdf")


```