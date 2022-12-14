# SAC

- Author: *{{Fu}}*
- Update: *July 30, 2022*
- Reading: *10 min*

---


## Introduction
`SAC`, Seismic Analysis Code, is one of the most widely used data Analysis packages in the field of seismology.



## Install Source Code

The SAC protocol only allows IRIS to distribute the `source` and `binary` packages to seismological personnel. So if you want to get the SAC package from official channels, you have to apply on the `IRIS` website [http://ds.iris.edu/ds/nodes/dmc/forms/sac/](http://ds.iris.edu/ds/nodes/dmc/forms/sac/)


:::{warning}
The SAC protocol specifies that users do not have the right to distribute SAC packages. Therefore, do not expose the SAC package on the network.
:::


`SAC` relys on [XQuartz](https://www.xquartz.org/), For MAC-OSX, if it is not already on your system, XQuartz needs to be downloaded from https://www.xquartz.org/ and installed. Refer to [Apple's support](https://support.apple.com/zh-cn/HT201341), and we can download the `.dmg` file and install `XQuartz` directly.

**Compile the source code**:

:::::{tab-set}
::::{tab-item} MacOS

```bash
$ tar -xvf sac-102.0.tar.gz
$ cd sac-102.0
$ mkdir build
$ cd build
$ ../configure --prefix=/usr/local/sac
$ make
$ sudo make install
```
::::

::::{tab-item} Linux(Ubuntu)
Install dependency packages firstly:

```bash
$ sudo apt update
$ sudo apt install build-essential
$ sudo apt install libncurses5-dev libsm-dev libice-dev
$ sudo apt install libxpm-dev libx11-dev zlib1g-dev
$ sudo apt install libedit-dev libxml2-dev libcurl4-openssl-dev
```

Compile SAC:

```bash
$ tar -xvf sac-102.0.tar.gz
$ cd sac-102.0
$ mkdir build
$ cd build
$ ../configure --prefix=/usr/local/sac
$ make
$ sudo make install
```
::::
:::::
:::{note}
Some system software packages are required to compile the SAC, but Anaconda's software package conflicts with the system software package. Therefore, the `Anaconda` user needs to temporarily block Anaconda's environment variable settings.
:::


## Configure Path

```bash
$ vim ~/.zshrc
# add the following lines to ~/.zshrc file
export SACHOME=/usr/local/sac
export SACAUX=${SACHOME}/aux
export PATH=${SACHOME}/bin:${PATH}

export SAC_DISPLAY_COPYRIGHT=1
export SAC_PPK_LARGE_CROSSHAIRS=1
export SAC_USE_DATABASE=0
```

- `SACHOME`: the installation path
- `SACAUX`: the directory of auxiliary files needed for SAC to run
- `PATH`: the system environment variable that enables the system to find the SAC executable correctly
- `SAC_DISPLAY_COPYRIGHT`: control whether to display the version and copyright information when starting SAC, which is generally set to 1
- `SAC_PPK_LARGE_CROSSHAIRS`:  control the cursor size during seismic phase picking
- `SAC_USE_DATABASE`: control whether conversion of the SAC format to GSE2.0 format. This feature is not normally used and is therefore set to 0






