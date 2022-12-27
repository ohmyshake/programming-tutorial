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

- `OpenMP` the full name is open multi-processing, support `c`, `c++`, and `fortran` language, `gcc` and `clang` of compilers. 
**Shared memory** (all threads can access all thread variables, just call the variable name), belongs to the same process, and cannot work on multiple nodes in the cluster (distributed memory), only on a single node. The programming is simple, just divide the for loop. If you read a variable into memory and open multiple threads to access a certain part of this variable at the same time, it will not be affected. As long as multiple threads do not write at the same time, it is safe. If you want to write, you need to lock it.

- `OpenMPI` the full name is open message passing interface. **Not share memory**, send messages between different processes.

- `CUDA` the full name is compute unified device architecture. GPU has many many threads for computing, and we need to write `kernel function` to run code in those threads. GPU computing is not independent, usually the data is send to GPU via CPU, and this process is called `heterogeneous computing`.
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







