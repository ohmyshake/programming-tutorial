# Python HPC

- Author: *{{Fu}}*
- Update: *Dec 26, 2022*
- Reading: *120 min*

---


## Multiple Threading


Because of the existence of `Global Interpreter Lock (GIL)`, multi-threads code in multi-cores system can only run one thread at a time. Each thread needs to `acquire` a lock before it can run, and after the thread finishes running, the lock is `released`, and another thread acquires the lock again. So multiple threading is sutiable for `IO bound` mission, not the `CPU bound` mission

```{figure} ./files/python_gil.webp
---
scale: 70%
align: center
name: python_gil
---
GIL in python
```

## Multiple Processing



## Mpi4py 




## Numba 


## Cupy 



## Ray







