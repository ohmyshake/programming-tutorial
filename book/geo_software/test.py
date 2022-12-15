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
# %%
