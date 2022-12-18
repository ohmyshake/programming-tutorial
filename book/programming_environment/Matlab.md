# Matlab


## Install Matlab in NOTS

Download `matlab` in Rice [webpage](https://kb.rice.edu/page.php?id=69000),
and then install in NOTS.
I don't have the `sudo` permission, so I need to change the authority of `install` script. 
Take my pkg for example, `matlab_R2022b_glnxa64` is the installation pkg, and `MATLAB_R2022b` is the folder after installing.


```bash
# install matlab without sudo mode
cd /PathToMatlab/matlab_R2022b_glnxa64/bin/
chmod -R 777 install
./install

# actiavte the license
cd /PathToMatlab/MATLAB_R2022b/bin
./activate_matlab.sh

```

## Run Matlab in VSCode 

Install the extensions, `Matlab`, `matlab-formatter`, `Matlab Snippets`, and `Matlab Code Run`. Set the env variable in `settings.json` as following:

```bash
$ open settings.json

# insert
"matlab.mlintpath": "/Applications/MATLAB_R2022b.app/bin/maci64/mlint",
"matlab.matlabpath": "/Applications/MATLAB_R2022b.app/bin/matlab",
"files.associations": {
        "*.m": "matlab"
    }
```

matlab-setting.jpg

## reference

- https://zhuanlan.zhihu.com/p/257625690

- https://muzing.top/posts/52276c1/