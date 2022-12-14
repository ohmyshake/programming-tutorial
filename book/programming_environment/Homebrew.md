# Homebrew

- Author: *{{Fu}}*
- Update: *July 25, 2022*
- Reading: *10 min*

---


## Introduction

[**Homebrew**](https://brew.sh/index_zh-cn.html) is the most popular third-party package manager for macOS, consisted of the following 4 parts:


|        Name       |       Purpose       |
|    ------------   |    -------------    |
| `brew`            | Homebrew 源代码仓库   |
| `homebrew-core`   | Homebrew 核心源      |
| `homebrew-cask`   | 提供 macOS 应用(用户图形界面)和大型二进制文件的安装 |
| `homebrew-bottles`| 预编译二进制软件包     |

---




## Install

:::::{tab-set}
::::{tab-item} Foreign
:::{note}
Please check [Homebrew](https://brew.sh/index_zh-cn.html) webpage for more info.
:::
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
::::


::::{tab-item} China
:::{note}
- 针对国内用户的 Homebrew 安装和配置指南来自于 https://brew.idayer.com/ 与 https://seismo-learn.org/seismology101/computer/macos-setup/
- Homebrew 以及通过 Homebrew 安装的所有软件包都会被安装到特定目录下, 通常是 `/usr/local/` 目录. 而在 Apple M1 芯片的 Mac 下， 这一目录为 `/opt/homebrew/`
:::

- 如果你是初次安装，这里使用中科大源:
```bash
# 1.执行安装脚本
$ export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
$ export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"

# 2.安装完成后设置 bottles 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```

- 如果你已经安装过，需要换源:
```bash
# 1. 设置中科大源
$ git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
$ git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
$ git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

# 2. 设置 bottles 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```

- 恢复默认源
```bash
$ git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git
$ git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git
$ git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git
```
`homebrew-bottles` 配置只能手动删除，将 `~/.zshrc` 文件中的 `HOMEBREW_BOTTLE_DOMAIN=https://mirrors.xxx.com` 内容删除，并执行 `source ~/.zshrc`
::::
:::::






## Uninstall



:::::{tab-set}
::::{tab-item} Foreign
:::{note}
More information please refer to: 
[https://docs.brew.sh/FAQ](https://docs.brew.sh/FAQ) and
[https://github.com/homebrew/install#uninstall-homebrew](https://github.com/homebrew/install#uninstall-homebrew)
:::

Uninstall script from the Homebrew/install repository

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

If you want to run the Homebrew uninstaller non-interactively, you can use:

```bash
$ NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```
::::


::::{tab-item} China
使用官方脚本同样会遇到uninstall地址无法访问问题，可以使用下面脚本:
```bash
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/uninstall.sh)"
```
::::
:::::



## Manual
Once Homebrew is installed, you can use the brew commands provided by Homebrew.  Check [documentation](https://docs.brew.sh/Manpage) for detailed manual.


```bash
# 模糊搜索与 wget 相关的软件
$ brew search wget

# 安装 wget 软件包
$ brew install wget

# 安装 Visual Studio Code, 其是带图形界面的软件，因而这里需要使用 --cask 选项
$ brew install --cask visual-studio-code

# 升级某个软件
$ brew upgrade xxx

# 卸载某个软件
$ brew uninstall xxx

# Brew 安装列表
$ brew list

# 查看brew配置信息
$ brew config

# 查看安装了多少package
$ brew info
```


:::{tip}
Look through https://formulae.brew.sh/ to check useful package.
:::



:::{dropdown} Homebrew 相关名词解释
:color: info
:icon: info

使用 Homebrew 时会碰到很多名词。这里做简单解释，
更详细的解释请查看[官方文档](https://docs.brew.sh/Formula-Cookbook#homebrew-terminology)。

**brew**

- Homebrew 提供的命令，用于查询、安装、卸载、升级以及管理软件包。

**Formula**

- 软件的描述文件，包含了软件的基本信息和编译安装方法。
  Homebrew 根据 Formula 提供的信息，即可编译或安装软件。
  每个软件对应一个 Formula。例如，git 对应的 Formula 是
  {file}`/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/git.rb`

**Bottle**

- 预先编译好的二进制软件包。使用 Bottle 安装软件，
  比从源码编译和安装更快。如果一个软件仓库包含预编译的软件包，使用 `brew install`
  时会自动使用它。

**Tap**

- 一个含有一系列软件的 git 仓库。使用
  [brew tap](https://docs.brew.sh/Taps#the-brew-tap-command)
  命令查看已启用的仓库列表或启用仓库。已启用的仓库位于
  {file}`/usr/local/Homebrew/Library/Taps/homebrew/` 目录。
  常见软件仓库有 [homebrew-core](https://github.com/Homebrew/homebrew-core)
  和 [homebrew-cask](https://github.com/Homebrew/homebrew-cask)。
  其中，homebrew-core 是内置核心仓库，
  homebrew-cask 仓库则含有各种 macOS 系统下带图形界面的应用程序。

**Cask**

- Homebrew 的扩展功能，用于安装 macOS 下的图形界面应用程序。
  使用 `brew list --cask` 命令可以查看已安装的 casks。

**Cellar**

- 所有软件的安装目录，即 {file}`/usr/local/Cellar`。

**Keg**

- 某一软件的安装目录，如 {file}`/usr/local/Cellar/git/2.30.0`。
:::



## My brew list
|        Name       |       Purpose       |
|    ------------   |    -------------    |
| `git`            | ...   |
| `zsh`            | ...   |
| `pfetch`            | ...   |
| `neofetch`            | ...   |
| `ncurses`            | I forget...   |
| ``            | ...   |







