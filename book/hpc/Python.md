---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---


File-IO Subprocess Numpy h5py 


## File IO

### read files

```python
file = "./file.txt"
with open(file, "r") as f:
    allfile = []
    for readline in f:
        onefile = readline.rstrip('\n')
        allfile.append(onefile)
```



```python
### read files


### write files
fout = open("input.txt", 'w') 
fout.write('# i \t i+0.5 \n')
for i in range(0,10):
  fout.write(str(i)) 
  fout.write('\t')
  fout.write(str(i+0.5)) 
  fout.write('\n')
fout.close()
```

## Numpy

```python
import numpy as np

a = np.ones(10)
```


## Subprocess


```{code-cell} ipython3
:tags: [hide-input,hide-output,output_scroll,remove-stderr,raises-exception]

import sys
print("this is some stdddout")
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
print(a)
```

## Multithreading Speeds Up Downloading Files

http://dong.sh/posts/pythonftpparallelsdownload/

