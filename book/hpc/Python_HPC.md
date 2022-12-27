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
:::




:::{dropdown} How the CPU works? The concept of `thread`, `process`, `Round-robin scheduling`, `CPU-bound`, `I/O bound`, `disk read speed` and `bandwidth`, and how many threads and processes we use are appropriate?
:color: info
:icon: info

`Round-robin (RR) scheduling` is one of the algorithms employed by process and network schedulers in computing. As the term is generally used, time slices (also known as time quanta) are assigned to `each process` in equal portions and in circular order, handling all processes without priority (also known as cyclic executive). 

```{figure} ./files/Round_Robin_Schedule_Example.jpg
---
scale: 50%
align: center
name: Round_Robin_Schedule_Example
---
Round Robin Schedule Example from Wikipedia
```

One `process` can generate many `thread` missions, and a process is cheap than a thread. Why? When a process is suspended, it needs to record the state at this time. When a process resumes, it needs to collect the state of the previous moment and then execute the program. We call this working time is `context switching` time.


Due to the `Round-robin scheduling`, a CPU core will only execute one thread at same time. For a task, not only `cpu computing` takes the time, but `Network I/O` and `Disk I/O` also take the time.


- `CPU-bound`: `computing cores + 1`, or `computing cores * 2`. I'd like personally to use computing cores + 1 choice.

- `Network I/O`: it depends, the empirical formula is `computing cores / 0.1`, for example in a network IO task, the whole process is `send requestion via CPU` --> `send back data via network (network IO)` --> `parse requestion vis cpu`. But after you send the request via CPU, your CPU is free, and the work is to wait network to send back data, so the utilization rate of CPU is not high at this time. 
    - If you use `a process` to do this task, you must need to wait network IO time, and after that you can run next step code. 
    - If you use `multi-threads` to do this task, when you wait the response of network, you can run other threads to send requests, and thus enhance the utilization rate of CPU. 
    - If you use `multi-processes`  to do this task, if will also save much time as same as `multi-threads` approach. But creating many processes is more expensive (in memory and time aspects) than creating multi threads. Why? At this time, the working time of multiple processes is spent on `context switching`, because the CPU has time slicing and runs different processes at different times. So multi-process will use more time then multi-thread.
    - The limitation is `bandwidth` (network transmission speed, e.g. 100 MB/s), because the bandwidth is a constant number, it is useless to use more threads. Imagine there are 10 lanes on a road, and a car runs on each lane. (a lane is a thread)

- `Disk bound (small data files)`: same as network I/O, for example, you need to read many data files to do computing, the whole process is `send read data mission via CPU` --> `IO system reads data into memory` --> `do computing task`. When you read many small files, the `disk read speed` and `bandwidth` is not the limitation factor, and the main time is spent on other operations such as finding the address of the small file (`seek time`). So when IO system reads data into memory, your CPU is free at this time, you can use `multi-threads` to enhance the efficiency.

- `Disk bound (big data files)`: single thread or process is well. Under this circumstance, the limitation is the `disk read speed` and `bandwidth`, and the multi-threads reading will not significantly increase the speed. 

:::


:::{dropdown} 
:color: info
:icon: info



:::








:::{dropdown} What is the `node`,`physical cores`, `computing cores`, and `Hyper-Threading Technology`?
:color: info
:icon: info

- For clusters, a cluster has multiple node nodes, each node can have multiple CPUs (`physical cores`), each CPU can have multiple cpu cores (`computing cores`), and each core can run two threads which is called `Hyper-Threading Technology`. 

- Because a thread belongs to a process, **a single process can only run under a single node**, so **threads cannot share memory across nodes**. As for the physical core, the laptop we buy has a cpu chip, which is a single physical core, but this chip may have 4 cores, and there are 4 computing cores.
:::




:::{dropdown} `OpenMP` and `OpenMPI`, which one is more suitable for parallel computing?
:color: info
:icon: info

`CPU-bound`, utilizes multiple processes, and takes full advantage of multiple CPUs. Maybe, you will have doubts, since multi-threading can be executed in parallel, isn't it also suitable for computing-intensive tasks? 

- In theory, `multi-process` is more suitable. It means that when the amount of data is relatively large and there is no logical dependence between computing tasks, multi-process is more suitable. Because **each process will have its own process memory space, each process is naturally isolated**. 

- While `multiple threads` share the same memory space, synchronization between threads must be considered. None of these problems are necessary for computationally intensive tasks (`CPU-bound`). So we say that computing-intensive tasks are more suitable for multi-processing.
:::






:::{dropdown} What is the **`openmpi+openmp hybrid`** mode?
:color: info
:icon: info

- For large-scale operations of cluster jobs: `openmpi+openmp hybrid`. Usually, `MPI` is used for communication between `nodes`, and `OpenMP` is used for calculation within a `single node`. The communication speed within the node is fast, and is slow between nodes. 

- For example, in the seismic forward simulation in the petroleum industry, N nodes are opened at the same time, each node is forwarded with one shot, and each shot uses several CPUs for calculation.
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







