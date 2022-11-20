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

# Map

- Author: *{{Fu}}*
- Update: *August 5, 2022*
- Reading: *30 min*

---

## 2021 Yangbi Earthquake Map

```{code-cell} ipython3
:tags: [hide-input]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
allfiles_path = os.path.join('../files/yangbi/*.SAC')             # 某个地震事件的文件夹，通配所有SAC数据
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









## Dayindian Water reservoir

**Make grd files:**

```bash
$ range=99.0/102.0/24.0/27.5
$ gmt grdsample ./topo_data/srtm_57_07.asc -I0.0005 -Gtmp.grd -R$range
$ gmt grdgradient tmp.grd -Gtmp.ient -A0/270 -Ne0.5
$ gmt makecpt -Chaxby -Z -T-1000/4000/100 > tmp.cpt
```

**Pygmt plot:**

```{code-cell} ipython3
:tags: [hide-input]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    grid = "../files/dayindian/tmp.grd",
    shading = "../files/dayindian/tmp.ient",
    cmap = "../files/dayindian/tmp.cpt",
    # region=region,
    # projection=projection,
    # frame='a0.2',
)
fig.colorbar(
    # Colorbar position justified outside map frame (J) at Middle Right (MR),
    # offset (+o) by 1 cm horizontally and 0 cm vertically from anchor point,
    # with a length/width (+w) of 7 cm by 0.5 cm
    cmap="../files/dayindian/tmp.cpt",
    position="JMR+o0.7c/-2c+w7c/0.5c",  # mu表示单位放在下面
    frame=["xa500f250", "y+l(m)"],
    truncate = "1000/3000",  # 截断表示 从1000m至4000m
    scale=1,
)
# replot map_scale
fig.basemap(region=region, projection=projection,frame=['a0.1',"WSen"],map_scale="g100.62/25.72+c25.7+w2k+u")    # a后面加lat/lon的间隔

### b.fault
fig.plot(#data="../files/dayindian/fault/CN-faults.gmt",
         data="../files/dayindian/fault/fault_paper.txt",
         region=region, # 必须添加，否则断层会画出界
         pen="1.5p,red")

# create space-delimited file
with open("../files/dayindian/fault/faultname_paper.txt", "w") as f:
    f.write("100.40 25.705 5 8p,Helvetica-Bold,gray30 CM Honghegu\n")
    f.write("100.58 25.865 55 8p,Helvetica-Bold,gray30 CM Yongsheng-Binchuan\n")

fig.text(textfiles="../files/dayindian/fault/faultname_paper.txt", angle=True, font=True, justify=True)

# cleanups
os.remove("../files/dayindian/fault/faultname_paper.txt")


### c.seismicity
time_bd = UTCDateTime("2012-09-07T12:15:00")
earthquakes_path = '../files/dayindian/seismicity/20080106-20211121.txt'
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
fig.plot(data="../files/dayindian/reservoir_shape/dayindian_reservoir_shape",
         pen="0.2p,blue",
         color="blue")

fig.text(text="Reservoir",
          x=100.507,
          y=25.793,
          font="10p,Helvetica-Bold,blue",
          transparency=30)


### e.station
sta_lat_lon_path = '../files/dayindian/sta_lat_lon/sta_lat_lon_select.txt'
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
    fig.plot(data="../files/dayindian/plate_boundary/India_Eurasia",
         pen="0.5p,red",
         style="f0.5/6p+t+l",
         color = "red")
    fig.plot(data="../files/dayindian/plate_boundary/Philippin_Eurasia",
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
fout = open("../files/dayindian/tmp.legend", 'w')
fout.write(leg)
fout.close()

### c.legend
fig.legend(spec="../files/dayindian/tmp.legend", position="x-0.1c/-2.5c+w6.2i+l1.2+jBL", box='+gwhite+p0.5p')

#%% 5.Save fig
fig.show()
# fig.savefig("STA_location.pdf")
```