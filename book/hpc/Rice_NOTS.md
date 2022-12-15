# NOTS

- Author: *{{Fu}}*
- Update: *Dec 15, 2022*
- Reading: *10 min*

---


## File Management

The following is my data managerment, more info please refer to [Rice CRC Tutorial](https://kb.rice.edu/108237).


| **Filesystem**   | **Use** | **Physical Path** | **Size** | **Quota** | **Type** | **Purge Policy** | 
| :-----| :---- | :---- | :----: | :----: |:----: |:----: | 
| Home directories | <font color=red>Only configuration file (eg. `.zshrc` `.vscode-server`)</font> |/home | 5 TB | 10 GB | NFS |none | 
|Group Project directories| <font color=red>Not use now</font> |/projects |20 TB |100 GB per group |NFS| none |  
|Work storage space |	<font color=red> Install software and store small data </font>|	/storage/hpc/work|	456 TB|	2 TB per group|	NFS	|none | 
|Shared Scratch high performance I/O | <font color=red> Workspace </font>|/scratch |157 TB |None|Lustre|14 days| 
|Local Scratch on each node| <font color=red> Not use now </font>|/tmp|4 TB|None|Local|at the end of each job | 



`/scratch` is not permanent storage

$SHARED_SCRATCH is to be used only for job I/O.  Delete everything you do not need for another run at the end of the job or move to $WORK for analysis. Staff may periodically delete files from the $SHARED_SCRATCH file system even if files are less than 14 days old.



## Computing Resources

```{figure} ./files/cpu_gpu.jpg
---
scale: 50%
align: center
name: cpu_gpu
---
NOTS Resources 
```

## NOTS Cluster

NOTS is a Red Hat linux system, the default shell is `bash`.
Becasue I'm not the administrator, so I don't have the root permissions,
which means I can't use `yum` to install packages. 
I must install `zsh` by myself.
In addition, I can't change the default Shell from `bash` to `zsh`.

```bash
# use wget to download source package 
wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download

# decompress the package
xz -d zsh.tar.xz
tar -xvf zsh.tar

# configuration
cd zsh
./configure --prefix=/storage/hpc/work/ja62/fy21/software/zsh/bin/zsh

# install
make 
make install

# auto launch when login bash
vim ~/.bashrc
export PATH=/storage/hpc/work/ja62/fy21/software/zsh/bin:$PATH
```
