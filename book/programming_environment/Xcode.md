# Xcode

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---


## Introduction

[Xcode](https://developer.apple.com/cn/xcode/) is an integrated development environment (IDE) for MacOS, similar to [Microsoft Visual Studio](https://visualstudio.microsoft.com/) for Windows. `Command Line Tools for Xcode` is a part of Xcode which contains common development tools, such as C/C++ compiler (`gcc`, `g++`), `make`, `git`, etc. It is a necessary software for programming in MacOS.



## Install

Type the following command in terminal to install `Command Line Tools for Xcode`

```bash
xcode-select --install
```

:::{warning}
`Xcode` also can be installed in `App Store`, but is so large usually needed >10G. So we recommend to install `Command Line Tools for Xcode`.
:::

- The `Command Line Tools for Xcode` installed here may not be the latest version. Click the Apple icon in the upper left corner of your desktop and check for updates in Software Updates under System Preferences. If so, upgrade it to the latest version. 

- After the MacOS is updated, sometimes you need to reinstall the `Command Line Tools for Xcode` and run the preceding commands again.

```{figure} ./img/Xcode-1.jpg
---
scale: 70%
align: center
name: xcode
---
Update Xcode
```



[**How can I uninstall the command-line tools?**](https://developer.apple.com/library/archive/technotes/tn2339/_index.html#//apple_ref/doc/uid/DTS40014588-CH1-HOW_CAN_I_UNINSTALL_THE_COMMAND_LINE_TOOLS_)


```bash
# print the install path which usually is "/Library/Developer/CommandLineTools"
$ xcode-select --print-path

# delete it
$ sudo rm -rf /Library/Developer/CommandLineTools
```
