# Matlab


## Install Matlab in NOTS

Download `matlab` in Rice [webpage](https://kb.rice.edu/page.php?id=69000),
and then install in NOTS.
I don't have the `sudo` permission, so I need to change the authority of `install` script. 

The `matlab_R2022b_glnxa64` is the installation pkg, and `MATLAB_R2022b` is the folder after installing.


```bash
# install matlab
cd /PathToMatlab/matlab_R2022b_glnxa64/bin/
chmod -R 777 install
./install

# actiavte matlab
cd /PathToMatlab/MATLAB_R2022b/bin
sh activate_matlab.sh

```

## Run Matlab in VSCode 

Install the extensions, `Matlab`, `matlab-formatter`, `Matlab Snippets`, and `Matlab Code Run`.

```bash
# change the permission 
chmod -R 777 /Path_to_matlab_pkg/bin/glnxa64

# install without sudo mode
./install

# activate the license
./activate_matlab.sh
```

## reference

- https://zhuanlan.zhihu.com/p/257625690

- https://muzing.top/posts/52276c1/