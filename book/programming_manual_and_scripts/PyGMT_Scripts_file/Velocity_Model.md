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

# Velocity Model

- Author: *{{Fu}}*
- Update: *August 5, 2022*
- Reading: *30 min*

---




## Longmen mountain


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

Vs_path = '../files/longmen/Vs.xyz'
Reloc_path = '../files/longmen/cd.reloc'

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
            outgrid="../files/longmen/sample1.nc"
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
                grid="../files/longmen/sample1.nc",
                cmap="../files/longmen/temp_cpt.cpt",
                )
            
            fig.plot(x=reloc_all[i][0], y=reloc_all[i][2], no_clip=False,style='c0.1c',color="black",pen=True,panel=[xx, yy])

fig.colorbar(cmap="../files/longmen/temp_cpt.cpt",position="JMB+o4c/1c+w8c", frame=["xa0.5f0.25", 'y+l"Vs (km/s)"'])
fig.show()
# fig.savefig('yf.pdf')

```