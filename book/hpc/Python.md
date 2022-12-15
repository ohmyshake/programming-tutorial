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




## Subprocess

### Manual

### Case-1

```{code-cell} ipython3
:tags: [hide-output,output_scroll,remove-stderr,raises-exception]

import sys
print("this is some stdddout")
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
print(a)
```