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

# Lune plot

- Author: *{{Fu}}*
- Update: *August 6, 2022*
- Reading: *30 min*

---

## Lune

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
path='../files/lune/'
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
        levels= "../files/lune/temp_cpt1.cpt",
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
    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_01.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_02.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_03.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_04.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')

    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_05.dat', unpack=True, usecols=(0,1))
    fig.plot(x=x, y=y, pen='1p,gray,-')
    
    x,y = np.genfromtxt('../files/lune/dfiles/sourcetype_arc_06.dat', unpack=True, usecols=(0,1))
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
fig.colorbar(cmap="../files/lune/temp_cpt1.cpt",yshift="-0.5c",frame=["xa0.2f0.1", "y+l(marginal-posterior)"], )
fig.show()
# fig.savefig('lune_us.pdf')

```




## Hudson Plot

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
FM_path='../files/lune/'

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










## Beachball

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
FM_path='../files/lune/'

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
allfiles_path=os.path.join('../files/yangbi/*.SAC')
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


v_model_path  = '../files/yangbi/v_model//v_model.nd'
# build_taup_model(v_model_path, output_folder='./', verbose=True)
model_path    = "../files/yangbi/v_model//v_model.npz"
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
figurename=os.path.join('../files/lune/beachball_project.pdf')
plt.savefig(figurename,dpi=800, format="pdf")


```