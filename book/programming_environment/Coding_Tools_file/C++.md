# C++

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---


## Introduction



## Install

There are 2 options here:
1. `clang` compiler + `openmp` + `openmpi` (notice: don't have `gfortran` compiler)
2. `gcc` compiler + `openmp` + `openmpi`

### 1.`clang` compiler + `openmp`

The clang compiler doesn't bring **`openmp`** package, and install openmp for clang compiler

```bash
# Install
$ brew install openmp

# For compilers to find libomp you may need to set for Makefile
$ export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
$ export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"

# Or compile directly (eg: c++ script)
$ clang++ openmp.cpp -o openmp -Xpreprocessor -fopenmp -lomp -I/opt/homebrew/opt/libomp/include  -L/opt/homebrew/opt/libomp/lib 
```


:::{dropdown} The example **`openmp.cpp`** file is here:
:color: info
:icon: info
```c++
#include <iostream>  
#include <omp.h>  

using namespace std;  
  
int main(){  
    omp_set_num_threads(15);
    #pragma omp parallel  
    {  
        cout << "Hello World!\n";  
    }  
    return 0;  
}  
```
:::


:::{dropdown} Compile error?
:color: info
:icon: info
The first time I compile the `cpp with openmp` code, I got an error as following
```bash
Undefined symbols for architecture arm64:
  "___kmpc_fork_call", referenced from:
      _main in main-4f8dcc.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

Then run the following command, it worked well now
```bash
$ ln -s /opt/homebrew/opt/libomp/lib/libomp.dylib /usr/local/lib/libomp.dylib
```

Refer to https://stackoverflow.com/questions/71061894/how-to-install-openmp-on-mac-m1 
:::




### 2. `gcc` compiler + `openmp` 

After install Command Line Tools for Xcode, M1 chip use clang to compile **`.c file`** and clang++ to compile **`.cpp file`**. 
And at this moment M1 chip also has gcc and g++, but they are the **`soft links`** to clang compiler.

To install `gcc` in M1 chip (it will also install `gfortran`), which will bring `openmp` package.

```bash
$ brew search gcc
$ brew install gcc

# To compile code directly (different from clang compiler)
$ g++ openmp.cpp -o openmp -fopenmp
```

Set the environment variables as following:

```bash
$ open ~/.zhsrc

# >>> brew's gcc (GNU) >>>
alias gcc='gcc-12'
alias g++='g++-12'
# <<< brew's gcc (GNU) <<<
```

Refer to https://trinhminhchien.com/install-gcc-g-on-macos-monterey-apple-m1/





### 3. Install `openmpi`

Then install **`openmpi`** (I think brew will use `clang` to compile openmpi package).

```bash
$ brew install open-mpi
```

Check installation using following command:

```bash
# Check openmpi version
$ mpic++ --version

# Check the detail of mpic++ command
$ mpic++ -showme

# Compile code using mpicc
$ mpic++ openmpi.cpp -o openmpi

# Run code
$ mpirun -np 4 ./openmpi
```

:::{dropdown} The example **`openmpi.cpp`** file is here:
:color: info
:icon: info
```c++
#include <iostream>  
#include <mpi.h>

using namespace std;  
int main(int argc, char **argv) {
    int ierr, num_procs, my_id;

    /* find out MY process ID, and how many processes were started. */
    ierr = MPI_Init(&argc, &argv);
    ierr = MPI_Comm_rank(MPI_COMM_WORLD, &my_id);
    ierr = MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    cout<< "Hello world! I'm process "<< my_id << " out of " << num_procs << " processes" << endl;

    ierr = MPI_Finalize();
    return 0;
}
```
:::



```bash
# Set openmpi's compiler before using mpi to compile code
# [1] C++ language
$ export OMPI_CXX=clang++
$ export OMPI_CXX=g++-12
# [2] C language
$ export OMPI_CC=clang
$ export OMPI_CXX=gcc-12

# Then use mpi to compile [c/c++] code
$ mpic++ openmpi.cpp -o openmpi
$ mpicc xx.c -o xx

# Run code
$ mpirun -np 4 openmpi
```

## Configuration




### VSCode

Download the plugin, `C/C++`, in VSCode Extensions

- Manual refer to [`Miscrosoft docs`](https://code.visualstudio.com/docs/python/python-tutorial)


## Makefile






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
| ``   | ...       |      |
| ``   | ...       |      |

**Seismology package**:

|     Name     |    Purpose    |     Way       |     
| ------------ | ------------- | :-----------: |
| ``   |        |      |
| ``   |        |      |



## Resource


- [C 语言教程](https://wangdoc.com/clang/)
- [C 语言教程](https://www.runoob.com/cprogramming/c-tutorial.html)（较全面、系统）
- [X 分钟速成 C](https://learnxinyminutes.com/docs/zh-cn/c-cn/)（简要）
- [Building programs](https://fortran-lang.org/learn/building_programs)（简要）
- [跟我一起写 Makefile](https://seisman.github.io/how-to-write-makefile/)（较全面、系统）
- [X 分钟速成 make](https://learnxinyminutes.com/docs/zh-cn/make-cn/)（简要）