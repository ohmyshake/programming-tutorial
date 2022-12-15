#%%

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
# %%
