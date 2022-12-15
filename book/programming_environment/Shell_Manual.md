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


## conda/mamba
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