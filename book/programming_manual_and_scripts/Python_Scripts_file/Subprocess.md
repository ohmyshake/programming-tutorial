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

# Subprocess

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---

## Manual




## Case-1
<!-- ,remove-output -->
```{code-cell} ipython3
:tags: [hide-input,hide-output,output_scroll,remove-stderr,raises-exception]

import sys
print("this is some stdddout")
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
print(a)
```

## Case-2




## Case-3











<!-- :tags: [remove-stderr]  -->
<!-- [raises-exception] -->

<!-- ```{code-cell} ipython3
:tags: [hide-input,remove-stderr,raises-exception]

import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
print(a)
```

```{code-cell} ipython3
:tags: [hide-input]

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

data = np.random.randn(2, 100)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=100*np.abs(data[0]));
``` -->
