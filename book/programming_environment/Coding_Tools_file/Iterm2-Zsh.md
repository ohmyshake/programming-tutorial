# Iterm2 & Zsh

- Author: *{{Fu}}*
- Update: *July 25, 2022*
- Reading: *10 min*

---

My terminal configuration in Mac.

**Requirements:**
- [Iterm2](https://iterm2.com/)
- [Zsh](https://www.zsh.org/)
- [Oh-My-Zsh](https://github.com/ohmyzsh/ohmyzsh)
- [Tmux](https://github.com/tmux/tmux)


**Preview:**

```{figure} ./img/Iterm2-Zsh-1.jpg
---
scale: 25%
align: center
name: preview
---
Terminal preview
```

**My `~/.zshrc`**


::::{toggle}
```bash
#-------------------------------------------------------------#
#----------- <<< Fu Yin set --- oh-my-zsh+p10k <<<------------#
#-------------------------------------------------------------#
echo "\n~ Hi! you can use *neofetch* for detailed info (from Fu Yin ~/.zshrc)"

# [1].source .bash_profile (activate environment variable)
# source ~/.bash_profile
# source ~/.bashrc

# [2].set font and close INSTANT PROMPT
POWERLEVEL9K_MODE="nerdfont-complete" 
POWERLEVEL9K_INSTANT_PROMPT="off"

# [3].pfetch and neofetch
pfetch
# neofetch

# [4].plugins download by Fu Yin
# Add wisely, as too many plugins slow down shell startup.
plugins=(git
	extract
	autojump
	zsh-autosuggestions
	zsh-syntax-highlighting)
# activate autojump
[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh

# [5].use p10k theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# [6].use colors
alias lc='colorls -lA --sd'

# [7]. If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# [8]. Path to your oh-my-zsh installation.
export ZSH=$HOME"/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
source $ZSH/oh-my-zsh.sh


#------------------------------------------------------#
#----------- <<< Fu Yin set -- software <<<------------#
#------------------------------------------------------#
# >>> yinfu_code path >>>
export PATH=/Users/yinfu/bin:${PATH}
# >>> yinfu_code path >>>

# >>> Homebrew mirrors >>>
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles
# >>> Homebrew mirrors>>>

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/yinfu/opt/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/yinfu/opt/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/yinfu/opt/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/yinfu/opt/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# >>> sac >>>
export SACHOME=/usr/local/sac
export SACAUX=${SACHOME}/aux
export PATH=${SACHOME}/bin:${PATH}
export SAC_DISPLAY_COPYRIGHT=1
export SAC_PPK_LARGE_CROSSHAIRS=1
export SAC_USE_DATABASE=0
# <<< sac <<<

# >>> brew's git >>>
export GIT=/usr/local/Cellar/git/2.37.1
export PATH=$GIT/bin:$PATH
# <<< brew's git <<<

```
::::




## Iterm2
Iterm2 is a replacement for terminal in Mac.

- Download [`Iterm2`](https://iterm2.com/) and install it like other App. Or you can use `brew install cask iterm2`.
- Download [`Dracula`](https://draculatheme.com/iterm) theme for Iterm2.

:::{admonition} Activating `Dracula` Theme!
:class: tip, dropdown
- iTerm2 > Preferences > Profiles > Colors Tab
- Open the Color Presets... drop-down in the bottom right corner
- Select Import... from the list
- Select the Dracula.itermcolors file
- Select the Dracula from Color Presets...
:::



## Zsh

Type `Zsh --version` in terminal. If the ZSH version is displayed, then ZSH is installed. Otherwise, you need to install Zsh.

```bash
$ brew install zsh
```


Run the following command to set the default Shell to Zsh:

```bash
$ chsh -s $(which zsh)
```


:::{note}
- Since macOS Catalina (10.15), the default Shell of macOS has changed from Bash to Zsh.
- The configuration file of Zsh is `~/.zshrc`, and of Bash is `~/.bashrc`.
:::






## Oh-My-Zsh

Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.

```bash
# install
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

This command will create the `~/.oh-my-zsh` directory, downloads oh my zsh to this directory, and generates the default Zsh configuration file `~/.zshrc`. The backup of the old configuration will be moved to a file like `~/.zshrc.pre-oh-my-zsh`.


### set theme

To use a different theme, modify the **ZSH_THEME** variable in the `~/.zshrc` configuration file.
For example, I use [Powerlevel10k](https://github.com/romkatv/powerlevel10k) theme.

```bash
# install
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k

# then open `~/.zshrc` and set `ZSH_THEME`:
ZSH_THEME="powerlevel10k/powerlevel10k
```

Run the following command to start the automatic configuration process:

```bash
$ p10k configure
```

After executing the command, p10k is initialized: `~/.p10k.zsh` is generated in the root directory, and some code will be written at the bottom of `~/.zshrc` as following:

```bash
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
```
To disable the p10k configuration, you only need to delete `~/.p10k.zsh` file and the preceding code.

### download font

- [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) is a project that patches developer targeted fonts with a high number of glyphs (icons). You can use brew to install, but it's too large. So you can just download serveal file as following:
open [https://github.com/ryanoasis/nerd-fonts/releases](https://github.com/ryanoasis/nerd-fonts/releases), and find `Hack.zip` in **Assets** part. 
- Double click to install those `ttf` file in your Mac, or you can <a href="./fonts.zip" download>download</a> here.
And set the font option in `~/.zshrc` as following.

```bash
POWERLEVEL9K_MODE="nerdfont-complete"
```


### add plugin

Download different plugins to `~/.oh-my-zsh/plugins` directory, and modify the plugins variable in the `~/.zshrc` configuration file as following:

```bash
plugins=(
    git
    extract
    autojump
    zsh-autosuggestions
    zsh-syntax-highlighting
)
```

- [extract](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/extract): use the `x abc.zip` syntax to decompress almost all compressed files, such as `.tar.gz`, `.tar.bz2`, `.zip`, `.7z`, `.rar`.

- [autojump](https://github.com/wting/autojump): a faster way to navigate your filesystem. Jump to a directory that contains `foo`. Before enabling autojump, install firstly:

::::{tab-set}

:::{tab-item} Use
```bash
$ j foo
```
:::


:::{tab-item} Source Code
```bash
# download 'autojump' to '/.oh-my-zsh/custom'
$ git clone git://github.com/wting/autojump.git $ZSH_CUSTOM/plugins/autojump

# go to 'autojump' folder
$ cd $ZSH_CUSTOM/plugins/autojump

# python install.py:
$ ./install.py
```
:::


:::{tab-item} Brew
```bash
$ brew install autojump
```
:::
::::


- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions): command auto-complete plug-in, when you enter several letters of a command, it will automatically complete the command according to the historical input.
```bash
$ git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
```


- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting): highlight available Zsh commands.

```bash
$ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

# This plug-in needs to be the last bit in the list of plug-ins in the configuration file ~/.zshrc
plugins=([plugins...] zsh-syntax-highlighting)
```



- [colorls](https://github.com/athityakumar/colorls): File directory beautification plug-in

```bash
# install
$ gem install colorls

# set alias in ~/.zshrc file
alias lc='colorls -lA --sd'

# use
$ lc
```



## Terminal in VSCode (??)
VSCode terminal can comes with a consistent interface, that just simply sets the font in VSCode setting as:

```bash
# set in vscode setting
terminal font = MesloLGS NF
```


## Tmux
working...







## References

1. [zhihu-超全教程](https://www.zhihu.com/column/p/145437836) (**_推荐_**)
1. [个性化p10k配置](https://suixinblog.cn/2019/09/beautify-terminal.html)
1. [个性化p10k配置](https://www.packetmania.net/2021/11/13/iTerm2-OMZ-Powerlevel10k/)
1. [少数派Ternimal主题推荐](https://sspai.com/post/53008)
1. [B站详细视频讲解](https://www.bilibili.com/video/BV19Z4y1P7ZL/?spm_id_from=autoNext)
1. [B站讲解tmux](https://www.bilibili.com/video/BV1rb411t7kd?from=search&seid=15827394807027530041&spm_id_from=333.337.0.0)
1. [大佬参考配置GitHub](https://github.com/wangshub/dotfile)
1. [大佬参考配置GitHub](https://github.com/thehalfspace/dotfiles2)
1. [洪鹤庭CSDN](https://blog.csdn.net/icestars/article/details/121098804?spm=1001.2014.3001.5501)
