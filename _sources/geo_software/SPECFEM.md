# SPECFEM


 <!-- # adjtomo  https://github.com/adjtomo/seisflows -->

## Specfem 2D

Make sure you have installed `gcc`, `gfortran` and `openmpi` in advance.
To suppress any potential limit to the size of the Unix stack, add `ulimit -S -s unlimited` to `~/.zshrc`.
Then go to specfem2d folder, and run following command to install:

```bash
# Download 
git clone --recursive --branch devel https://github.com/SPECFEM/specfem2d.git

# Configure in single precision
./configure FC=gfortran CC=gcc MPIFC=mpif90 MPI_INC=/opt/homebrew/include --with-mpi

# Configure in double precision, solver's speed will be decreased
./configure FC=gfortran CC=gcc MPIFC=mpif90 MPI_INC=/opt/homebrew/include --with-mpi --enable-double-precision

# Compile with CUDA (not finished)
./configure --with-cuda=cuda5 CUDA_FLAGS=.. CUDA_LIB=.. CUDA_INC=.. MPI_INC=..

# Make
make
```

Add executable command to environment variable:

```bash
open ~/.zshrc

# >>> specfem2d >>>
# To suppress any potential limit to the size of the Unix stack.
ulimit -S -s unlimited

# bin
export PATH=/Users/yinfu/package/specfem2d/bin:${PATH}
# <<< specfem2d <<<
```


:::{warning}
- Must download by the following command (from devel branch), otherwise it will be failed in installation in **M1 chip**.
- When you run code in **M1 chip**, must use `mpirun -np 1 xmeshfem2D/xspecfem2D/...`, instead of `xmeshfem2D/xspecfem2D/...`, otherwise it will be failed.
:::



## Specfem 3D