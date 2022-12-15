# Python

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---

:::{warning}
Python is an interpreted language that requires the interpreter to execute Python code. Although the Python interpreter is built into Linux/macOS systems, it is recommended that users do not use it to avoid damaging the built-in Python and causing system problems.
:::


## Install
It is recommended to install [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) and use its `conda` to manage and install Python and its packages.

::::{dropdown} What's the difference between Python, Anaconda, and Miniconda?
:color: info
:icon: info

**Python**

- The [Python](https://www.python.org/downloads/) installation package downloaded from the official Python website only provides a Python interpreter, which contains only Python's core packages and libraries. Installing the Python interpreter is equivalent to installing the `Python interpreter` + `core packages/libraries`.

**Anaconda**

- [Anaconda](https://www.anaconda.com/) is a distribution of Python, not only provides a Python interpreter, but also built-in many Python development tools and many scientific computing related libraries. It formed an out-of-the-box Python scientific computing environment, eliminating the problem to configure the scientific computing environment.
- Anaconda also provides a powerful package manager, `conda`, which makes it easy to install packages and manage environments.
Installing Anaconda is equivalent to installing the `Python interpreter` + `core packages/libraries` + `hundreds of scientific computation-related packages` + `package manager conda`
- But Anaconda occupies a large amount of hard disk space (usually more than 3 GB), and it installs many packages that are not normally used, which may cause version conflicts when installing new packages.

**Miniconda**

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a shortened version of Anaconda. It inherits the virtues of Anaconda while avoiding its bloat. The installation package is only about 50 MB and usually takes only tens of seconds to install. Installing Miniconda is equivalent to installing the `Python interpreter` + `core packages/libraries` + `package manager conda`.
::::


1. Download [Miniconda3 macOS Intel x86 64-bit bash](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh).
2. Install Miniconda
    ```bash
    bash Miniconda3-latest-MacOSX-x86_64.sh
    ```
    Miniconda will be installed into `~/miniconda3` path in M1 by default. The installation package will write the initialization statement to the `shell`'s configuration file, e.g. `~/.zshrc` in my Mac.

    :::{toggle}
    ```bash
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
    ```
    :::


::::{dropdown} How to uninstall Miniconda?
:color: info
:icon: info
```bash
# delete install directory
rm -rf ~/miniconda3

# delete environment variable
vim ~/.zshrc

# delete configuration files
rm -rf ~/.condarc ~/.conda ~/.continuum
```
::::


## Configuration


### Package Manager

It is recommended to use `mamba` to manage packages. Sometimes `mamba` may not work, you can consider to use `conda` or `pip`.

::::{dropdown} What's the difference between pip, conda and mamba?
:color: info
:icon: info

[`pip`](https://pip.pypa.io/)
- `pip` is the official package manager provided by Python. It can be used to install Python packages from the [`Python package Index`](https://pypi.org/) (pypi) website or to install Python packages from source code.

[`conda`](https://docs.conda.io/)
- `conda` is provided by `Anaconda/Miniconda` that allows you to install not only Python packages, but also packages written in other languages (or any software). Another important feature is the management of Python environments, which can be used to install multiple different versions of Python interpreters or packages within a system.
- But the biggest drawback is **slowness**. Before installing software packages, it takes a lot of time to resolve version dependencies between software packages, and it is also slow to download and install software packages.

[`mamba`](https://mamba.readthedocs.org/)
- `mamba` is an alternative to `conda`, which not only resolves software version dependencies very quickly (its core code is written in C++ language), but also can download and install software packages in parallel, which greatly reduces the time of software installation. The usage of `mamba` is almost exactly the same as that of conda.
::::

Install `mamba`

:::::{tab-set}

::::{tab-item} Foreign
To get `mamba` via `conda`, just install it into the base environment from the `conda-forge` channel:
```bash
conda install mamba -n base -c conda-forge
```
::::

::::{tab-item} China
`mamba` uses the configuration file of `conda`. Therefore, you need to configure `~/.condarc` file  before using Mamba.
Use [Tsinghua](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/) mirror to speed up the download of softwares.
Here is my `~/.condarc` file:

```bash
cat ~/.condarc

# output
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
Then you can use `conda` to install `mamba`, and just install it into the **base environment** from the `conda-forge` channel:
```bash
conda install mamba -n base -c conda-forge
```
::::

:::::

Now you can use `mamba` to manage your packages, e.g.:
```bash
mamba install numpy
```

:::{warning}
Installing `mamba` into any other environment than base can cause unexpected behavior
:::



### VSCode
Download the plugin, `Python`, in VSCode Extensions

- Manual refer to [`Miscrosoft docs`](https://code.visualstudio.com/docs/python/python-tutorial)


## Package

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 50%;
}
table th:nth-of-type(2) {
    width: 20%;
}
</style>


**scientific computation-related package**:

|    Name       |    Purpose    |    Way       |     
| ------------  | ------------- | :----------: |
| `mamba`       | ...           | conda        |
| `numpy`       | ...           | conda  |
| `matplotlib`  | ...           | conda  |
| `scipy`       | ...           | conda  |
| `pandas`      | ...           | conda  |
| `jupyter book`| ...           | conda  |
| `jupyterlab`  | ...           | conda  |
| `jupyter notebook` | ...        | conda  |
| `jupyterlab_myst`   |  ...       | pip     |
| `h5py`   |  ...      |   pip   |
| `jill`   | for installing Julia       | pip     |
| `openpyxl`   | read excel       | pip     |
| ``   |        |      |


**geophysics package**:

|     Name     |    Purpose    |     Way       |     
| ------------ | ------------- | :-----------: |
| `obspy`       | ...           | conda   |
| `pygmt`       | ...           | conda   |
| `cartopy`     | Geo-Map       | conda   |
| `pyfk`        | ...           | pip           |
| ``   |        |      |
| ``   |        |      |




## Resource

Here are some resources for learning about Python and common scientific computing modules:

- [Python](https://www.python.org/)
  - [Python Documentation](https://docs.python.org/zh-cn/3/)
  - [廖雪峰的 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [NumPy](https://numpy.org/)
  - [NumPy Documentation](https://numpy.org/doc/stable/)
  - [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/)
- [Matplotlib](https://matplotlib.org/)
  - [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/)
  - [Scientific Visualization: Python + Matplotlib](https://github.com/rougier/scientific-visualization-book)
- [pandas](https://pandas.pydata.org/)
  - [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/)
- [SciPy](https://scipy.org/)
  - [SciPy Documentation](https://docs.scipy.org/doc/scipy/tutorial/)


