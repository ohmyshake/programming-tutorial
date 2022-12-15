# Shell Manual


## ln
```bash
# Print all links
ls -al

# Create a link, file2 is the link of file1.
ln -s file1 file2
```


## scp
```bash
scp
```

## rsync
```bash
rsync
```


## mamba/conda
```bash
# check all packages
conda list

# install package
conda install xxx
```


## ssh/sshfs
```bash
# ssh -p port -X user@hostname
ssh -p 22 -X fy21@nots.rice.edu
ssh nots

# sshfs NOTS HPC in Rice
sshfs -o follow_symlinks fy21@nots.rice.edu:/ /Users/yinfu/share1/

# set alias before in '~/.zshrc'
alias sshfs-nots='sshfs -o follow_symlinks -p 22 fy21@nots.rice.edu:/ /Users/yinfu/share1/'
alias resshfs-nots='diskutil umountDisk /Users/yinfu/share1; sshfs-nots'
sshfs-nots 
resshfs-nots
```



## mount/umount 
Use `diskutil` on MacOS, `mount/umount` on Linux. 
Disk softwares on Mac, such as `Disk Utility`, `Tuxera`...

```bash
# List the partitions of a disk
diskutil list

# mount a single volume
diskutil mount [IDENTIFIER]
diskutil mountDisk disk2s1

# mount an entire disk
diskutil mountDisk [IDENTIFIER]/[PATH]
diskutil mountDisk disk2s1
diskutil mountDisk /dev/disk2

# umount a single volume
diskutil umount [IDENTIFIER]
diskutil umount disk2s1

# umount an entire disk
diskutil umountDisk [IDENTIFIER]/[PATH]
diskutil umountDisk disk2s1
diskutil umountDisk /dev/disk2

# umount sshfs
diskutil umountDisk [PATH]
diskutil umountDisk /Users/yinfu/share1
```


```{figure} ./files/diskutil-list.jpg
---
scale: 30%
align: center
name: diskutil-list
---
My `diskutil list`
```

## df
`df` full name is `disk free`.

```bash
# The space size of each currently mounted directory
df -h

# -ll: display bytes || -lh: display KB/MB/G/T...
ls -ll
ls -lh

# Display total file size in current directory
du -sh

# View the size of each file and folder in the current directory
du -h --max-depth=1
du -h --max-depth=1*
```




## cat
```bash
cat
```


## wc
`wc` full name is `word count`

```bash
# Find the lines, words, bytes, filenames of the file
wc file

# Find the lines of the file
cat file | wc -l
```

## head/tail

```bash
head

tail
```




## top
```bash
top

#quit
q
```


## kill

```bash
ps -ef | grep yinfu | awk '{ print $2 }' | xargs kill -9
```


## nohup

```bash
nohup 
```




## poetry

follow the instructions below: https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry/

1. use `conda` create a new environment, only install `python`

    ```bash
    conda env create -f environment.yml  # create env according to .yml file
    conda env export > environment.yml  # export .yml file
    conda activate jupiter-dev  # activate env
    ```

2. use `poetry` install other python package

install poetry first
```bash
curl -sSL https://install.python-poetry.org | python3 - # do not use pip

mkdir $ZSH_CUSTOM/plugins/poetry # add poetry into oh-my-zsh plugins
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```


```bash
poetry config virtualenvs.create false  # do not allow poetry create env
poetry init  # this command will create pyproject.toml file
poetry install  # this command will install some package mentioned in 'pyproject.toml', and also generate a 'poetry.lock' file
# Now you can change 'pyproject.toml' by hand
poetry update # update the new info in 'pyproject.toml' into 'poetry.lock' file
```



## Otter



How to perform real-time transcription of meeting and video content?
I use `AirPods` + `Otter` + `Loopback` + `BlackHole-2ch`.

:::{dropdown} Do you know **Loopback** and **BlackHole-2ch**?
:color: info
:icon: info
**BlackHole** is a virtual audio device that converts audio output into audio input. BlackHole redirect sounds an app plays on BlackHole to another app using BlackHole as input.

**Loopback** is an audio routing software that can take multiple audio output streams, mix them, and split them into multiple output streams. It works as a virtual audio device as well as BlackHole.

More info can be found in https://blog.tai2.net/how-to-use-otter-en.html
:::

1. Firstly install `BlackHole-2ch` using `brew`, and the github repository is [here.](https://github.com/ExistentialAudio/BlackHole)

    ```bash
    brew install blackhole-2ch
    ```

2. Download `Loopback` software. You can download it from its official [website](https://rogueamoeba.com/loopback/) or other ways.

3. Set sound environment in your Macbook as following:

```{figure} ./files/otter.jpg
---
scale: 40%
align: center
name: diskutil-list
---
My `Loopback` setting
```

```{figure} ./files/input.jpg
---
scale: 30%
align: center
name: diskutil-list
---
My `Sound` input setting
```

```{figure} ./files/output.jpg
---
scale: 30%
align: center
name: diskutil-list
---
My `Sound` output setting
```


Now if you use `Zoom`, you need set Microphones same as system as following:

```{figure} ./files/zoom.jpg
---
scale: 60%
align: center
name: diskutil-list
---
My `Zoom` setting
```

If you want view video from webpage or local, the above setting also can work. 
It is worth mentioning that if you use `Chrome`, you can use `Live Caption` function
provided by Chrome itself.



## FwiFlow
Install `miniconda` firstly, use pip install `jill` which is a juila installer.
Then use jill install julia@1.3 version and quit the conda environment.
Other verison will be failed.

```bash
# install julia
jill install 1.3

# quit conda env
conda deactivate

# install FwiFlow
julia > using Pkg
julia > Pkg.add("FwiFlow")
julia > Pkg.build("FwiFlow")

```


## Seis4CCS

```bash
julia > ] add https://github.com/slimgroup/Seis4CCS.jl.git
julia > ] add ColorSchemes@3.19
julia > ] add https://github.com/slimgroup/SlimPlotting.jl.git
```