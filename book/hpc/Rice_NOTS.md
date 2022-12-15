# Nots

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
