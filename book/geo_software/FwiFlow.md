# FwiFlow




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


