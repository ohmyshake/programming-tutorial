# Overview

- Author: *{{Fu}}*
- Update: *July 24, 2022*
- Reading: *10 min*

---

:::{warning}
This tutorial supports **Monterey (12.4)**, and may also be valid for Big Sur (11) and macOS Catalina (10.15). **MacOS M1**  will be supplemented later...
:::



## Re-Install MacOS

::::{tab-set}

:::{tab-item} Intel Monterey

Reinstall Monterey system as follows:

- Restart the computer, and hold {kbd}`Command` + {kbd}`R` key until Apple logo appears.
- Enter {kbd}`Disk Utility` and {kbd}`Erase` the hard disk.
- Select reinstall macOS Monterey.

:::

:::{tab-item} M1

Working...

:::

::::



## APP

Complete list in my mac please check [Mac-Software.md](./Overview_file/MacSoftware.md) list. Here are several resources website.

- [**awesome-mac**](https://github.com/jaywcjlove/awesome-mac) is a github collecting awesome macOS software.


**Genuine Software**:

* App Shopper: [`http://appshopper.com/`](http://appshopper.com/)
* MacUpdate: [`https://www.macupdate.com/`](https://www.macupdate.com/)
* 少数派: [`http://sspai.com/tag/Mac`](http://sspai.com/tag/Mac)
* Mac玩儿法: [`http://www.waerfa.com`](http://www.waerfa.com)
* 腾讯柠檬精选: [`https://lemon.qq.com/lab/`](https://lemon.qq.com/lab/)


**Pirated Software**. Refuse piracy from me. Software vendors can go to these places rights.

* MacWk: [`https://macwk.com/`](https://macwk.com/)
* AppKed: [`http://www.macbed.com`](http://www.macbed.com)
* Softasm: [`https://softasm.com/`](https://softasm.com/)
* Appstorrent: [`https://appstorrent.ru/`](https://appstorrent.ru/)
* Mac精品软件: [`http://xclient.info/`](http://xclient.info/)
* Mac毒: [`https://www.macdo.cn`](https://www.macdo.cn)


**Rice University Software for Student**:

* [`https://kb.rice.edu/69000`](https://kb.rice.edu/69000)


**USTC Software for Student**:

* [`http://zbh.ustc.edu.cn/zbh.php`](http://zbh.ustc.edu.cn/zbh.php), need USTC-VPN.


**SUSTech Software for Student**:

* [`https://lib.sustech.edu.cn/gjyrj_116/list.htm`](https://lib.sustech.edu.cn/gjyrj_116/list.htm)



## File managment

Toctree Mac finder as follows:

::::{toggle}
```
$ toctree Mac finder
FuYin-MAC/
├── Applications    # built-in
├── Desktop         # built-in
├── Documents       # built-in
├── Downloads       # built-in
├── me
├── bin
├── src
├── code
├── data
├── learn
├── project
├── workspace
└── yinfu           # built-in
```
::::

### Applications

- Store apps downloaded from App Store and the Internet, such as Chrome/Wechat...

### Desktop

- Some temporary files

### Documents

- Some software uses this folder to store files, such as Matlab/Adobe, but I don't usually use it to store my files.

### Download

- Default directory for browser downloads

### me

- {file}`~/me` stores my life files, which have nothing to do with scientific research.

```{toggle}
:show:

::::{grid}
:gutter: 1

:::{grid-item-card} Health
:columns: 4
Body health.
:::

:::{grid-item-card} Cook
:columns: 4
Cooking study.
:::

:::{grid-item-card} Information
:columns: 4
Certificate.
:::

:::{grid-item-card} PhD_application
:columns: 4
...
:::

:::{grid-item-card} Photo
:columns: 4
...
:::

:::{grid-item-card} Rice-file
:columns: 4
...
:::

:::{grid-item-card} USTC-file
:columns: 4
...
:::

::::
```
<!-- about how to use {toggle} refer to https://jupyterbook.org/en/stable/interactive/hiding.html#hiding-remove-content -->



### bin

- {file}`~/bin` stores simple **executable code** and tool-based scripts, 
such as `rdseed`. And also put executable files of large programs here, such `specfem` and `matlab`.

- Adds the directory's path to the environment variable `PATH`.

- More information please check [Seis-Software.md](./Overview_file/SeisSoftware.md) list.


### src

- {file}`~/src` stores source code from **other institutions’ software**, such as SAC, OpenMPI, Specfem-2D...

- More information please check [Seis-Software.md](./Overview_file/SeisSoftware.md) list.

```{note}
Remember that after compiling, put the executable code in the {file}`~/bin` folder.
```


### code

- {file}`~/code` stores source code wrote by myself, and it's **my personal code**.

- More information please check [Seis-Software.md](./Overview_file/SeisSoftware.md) list.

```{note}
Remember that after compiling, put the executable code in the {file}`~/bin` folder.
```


### data

- {file}`~/data` stores some common data, such as seismic waveform, fault data, earthquake catalog, etc., which can be shared by multiple different research projects.

- And {file}`~/data` stores my **Bachelor & Master Thesis**, **meeting report slides** (*Group/SSA/AGU/CGU...*), and some **meeting video**.


### learn

- {file}`~/learn` stores some **reference book** about seismology and some **seismology lesson**.

- And {file}`~/learn` stores **skill lessons** such as Bayes and C++.



### project

- {file}`~/project` store research project, such as {file}`~/project/MCMTpy` a earthquake source project.


### workspace

- {file}`~/workspace` is a directory for doing occasional tests or simple experiments.


### yinfu

- {file}`/Users/yinfu` equals to {file}`~` which is the user's root path.


