# Python HPC

- Author: *{{Fu}}*
- Update: *Dec 26, 2022*
- Reading: *120 min*

---

## Introduction

`Parallel Computing` is the general name  `Cluster Computing`, `Distributed Computing`, and `Cloud Computing`.

- `Cluster Computing`: the most common cluster is `High-performance clusters (HPC)`

:::{admonition} Admonition
The following are the main three ways for hpc computing:

- `OpenMP` the full name is open multi-processing, support `c`, `c++`, and `fortran` language, `gcc` and `clang` of compilers. **Share memory** for same process.

- `OpenMPI` the full name is open message passing interface. Do **not share memory**, send message between different processes.

- `CUDA` the full name is compute unified device architecture. Have more threads for computing, but we need to write `kernel function` to run code in those threads.
:::



- `Distributed Computing`:

- `Cloud Computing`:



Parallel computing share-memory for communication

distributed computing share-nothing, communicate via network (spark, hadoop)



## Multiple Threading




## Multiple Processing



## Mpi4py 




## Numba 


## Cupy 



## Ray







