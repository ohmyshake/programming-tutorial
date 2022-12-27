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
**Shared memory** (all threads can access all variables, just call the variable name), belongs to the **one process**, and cannot work on multiple nodes in the cluster (distributed memory), but work only on a single node. As long as multiple threads do not write at the same time, it is safe, and if you want to write, you need to use `lock` function.

- `OpenMPI` the full name is open message passing interface. Each processes has **independent memory**, and different processes can communicate (with performance memory overhead), suitable for various tasks such as large clusters with multiple nodes.

- `CUDA` the full name is compute unified device architecture. GPU has many many threads for computing, and we need to write `kernel function` to run code in those threads. GPU computing is not independent, usually the data is send to GPU via CPU, and this process is called `heterogeneous computing`.

**Note:**

- For large-scale operations of cluster jobs: openmpi+openmp hybrid. Usually, `MPI` is used for communication between `nodes`, and `OpenMP` is used for calculation within a `single node`. The communication speed within the node is fast, and between nodes is slow. For example, in the forward simulation in the petroleum industry, N nodes are opened at the same time, each node is forwarded with one shot, and each shot uses several CPUs for calculation.

- For clusters, a cluster has multiple node nodes, each node can have multiple CPUs (physical cores), each CPU can have multiple cpu cores (computing cores), and each core can run two threads. Because a thread belongs to a process, a single process can only run under a single node, so threads cannot share memory across nodes. As for the physical core, the laptop we buy has a cpu chip, which is a single physical core, but this chip may have 4 cores, and there are 4 computing cores.
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







