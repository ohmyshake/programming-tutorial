---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python HPC

- Author: *{{Fu}}*
- Update: *Dec 26, 2022*
- Reading: *120 min*

---


## Multiple Threading



### Global Interpreter Lock

Because of the existence of `Global Interpreter Lock (GIL)`, multi-threads code in multi-cores system can only run one thread at a time. Each thread needs to `acquire` a lock before it can run, and after the thread finishes running, the lock is `released`, and another thread acquires the lock again. So multiple threading is sutiable for `IO bound` mission, not the `CPU bound` mission

```{figure} ./files/python_gil.webp
---
scale: 60%
align: center
name: python_gil
---
GIL in python
```



<!-- :tags: [hide-input] -->


```{code-cell} ipython3
import threading

#def main():


def thread_job():
    print('This is a thread of %s \n' % threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job,)
    thread.start()
    # see how many threads is running now
    print("There are", threading.active_count(), 'threads is running now\n') 

    # see the thread list
    print("The running threads list is:", threading.enumerate(), '\n') 

    # which one thread is running now
    print("The thread", threading.current_thread(), 'is running now\n') 
if __name__ == '__main__':
    main()

```

### Thread Pool

A `thread pool` maintains multiple threads waiting for tasks to be allocated for `concurrent` execution by the supervising program. By maintaining a pool of threads, the model increases performance and avoids latency in execution due to frequent creation and destruction of threads for short-lived tasks. The number of available threads is tuned to the computing resources available to the program, such as a parallel task queue after completion of execution.


One benefit of a thread pool over creating a new thread for each task is that **thread creation and destruction overhead is restricted to the initial creation of the pool**, which may result in better performance and better system stability. Creating and destroying a thread and its associated resources can be an expensive process in terms of time. An excessive number of threads in reserve, however, wastes memory, and context-switching between the runnable threads invokes performance penalties.

```{figure} ./files/thread_pool.png
---
scale: 20%
align: center
name: thread_pool
---
Thread pool in python
```




## Multiple Processing



## Mpi4py 




## Numba 


## Cupy 



## Ray







