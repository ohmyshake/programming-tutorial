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

Now let's introduce the `threading` package in python.


#### **Create a thread, start a thread, and join function:**

```{code-cell} ipython3
import threading
import time

def thread_job():
    print('thread_job start\n')
    print('This is a thread of %s \n' % threading.current_thread())
    print('thread_job finish\n')

def main():
    # add a new thread
    thread = threading.Thread(target=thread_job, name="thread_job")

    # start a thread
    thread.start()

    # wait this thread finished running, then run following code. Also called `block thread`
    thread.join()

    # see how many threads is running now
    print("There are", threading.active_count(), 'threads is running now\n') 

    # see the thread list
    print("The running threads list is:", threading.enumerate(), '\n') 

    # which one thread is running now
    print("The thread", threading.current_thread(), 'is running now\n') 

if __name__ == '__main__':
    main()
```

#### **Quene function: get the results from multiple threads** 

```{code-cell} ipython3
import threading
import time
from queue import Queue

# do a function: square a number
def job(l,q):
    new_list = l.copy()
    for i in range(len(l)):
        new_list[i] = l[i]**2
    q.put(new_list)

def multithreading():
    # create a quene
    q = Queue()

    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

    # create 4 threads
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    
    # get the results from multi-threads
    results = []
    for _ in range(4):
          results.append(q.get())
    print("Input:", data)
    print("Output:", results)

if __name__ == '__main__':
    multithreading()
```


#### **GIL is not suitable for `CPU bound` task:**

```{code-cell} ipython3
import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
```


#### **GIL lock function:**

```{code-cell} ipython3
import threading

def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
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

Now let's introduce `concurrent.futures` package in python.


#### **Create a thread pool, submit a task, get the results**

```{code-cell} ipython3
import time
from concurrent.futures import ThreadPoolExecutor

def down_video(times):
    time.sleep(times)
    print("down video {}s finished".format(times))
    return times

# create a thread pool with max_workers threads
executor = ThreadPoolExecutor(max_workers=2)

# submit a task into thread pool，and submit function will return immediately with blocking
task1 = executor.submit(down_video, (3))
task2 = executor.submit(down_video, (2))

# `done` function is used to check whether the task is finished
print("任务1是否已经完成：",task1.done())

# `cancel` function is used to cancel the task before the thread put into thread-pool 
print("取消任务2：",task2.cancel())

time.sleep(4)
print("任务1是否已经完成：",task1.done())

# `result` is used to get the results of a thread
print("task1's results: ", task1.result())
```


#### **s**
```{code-cell} ipython3
from concurrent.futures import ThreadPoolExecutor

```

## Multiple Processing



## Mpi4py 




## Numba 


## Cupy 



## Ray







