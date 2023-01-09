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

# Basic Command

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---


File-IO Subprocess Numpy h5py 


## File IO

**read file:**


If the `file.txt` is like the following format whose each line has a separate content:

```bash
UTC190419001218.sgy
UTC190419001233.sgy
UTC190419001248.sgy
UTC190419001303.sgy
```

Read it into a `list`

```python
file = "./file.txt"
with open(file, "r") as f:
    allfile = []
    for readline in f:
        onefile = readline.rstrip('\n')
        allfile.append(onefile)
```

**write file:**

```python
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


## Pathlib

```python
from pathlib import Path

output_path = "./DAS_DATA"

Path(output_path).is_dir()

Path.mkdir(Path(output_path))

abs_path = Path(output_path).joinpath(url.split('/')[-1]).absolute()
abs_filename = str(abs_path)

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

