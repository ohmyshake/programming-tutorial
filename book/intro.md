# Introduction ✨

Welcome to **Programming Notebook**, a notebook mainly about my scientific notes and gain in learning **Programming** and **Geophysics**, and I am very glad if it is helpful for your researches. 

**Enjoy** 👋👋👋

```{margin} About Author
I'm [**Fu Yin**](https://yinfu.info/), a geophysics graduate student at Rice University.
```

:::{admonition} Admonition
There is no guarantees of correctness and if you spot an error or a doubtful statement, kindly let me know.
:::

The main content of the notebook as follows:



::::{card-carousel} 10

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://www.inferentialthinking.com/
**Inferential Thinking**
^^^
```{image} https://inferentialthinking.com/_static/favicon.png
:height: 100
```

The textbook used by UC Berkeley's popular Data 8 class.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://python.quantecon.org/

**QuantEcon**
^^^
```{image} https://python.quantecon.org/_static/qe-logo-large.png
:height: 100
```

A free online book to teach computational economics with open source tools.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://the-turing-way.netlify.app

**The Turing Way**
^^^
```{image} https://the-turing-way.netlify.app/_static/logo.jpg
:height: 100
```

A guidebook for best-practices in reproducible and community-driven science.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://inria.github.io/scikit-learn-mooc/

**The SciKit Learn MOOC**
^^^
```{image} https://inria.github.io/scikit-learn-mooc/_static/scikit-learn-logo.png
:height: 100
```

A large online course for machine learning with the PyData stack.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://uwdata.github.io/visualization-curriculum/intro.html

**Data Science @ UW**
^^^
```{image} https://uwdata.github.io/visualization-curriculum/_static/altair-hist.png
:height: 100
```

Interactive data visualization with Python, as taught at the University of Washington.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://py-pkgs.org/

**Py-Pkgs**
^^^
```{image} https://d33wubrfki0l68.cloudfront.net/9ff174183b5af5c3a177bfccd4796454883bc1f7/86cde/_static/py-pkgs-hex.png
:height: 100
```

A book describing how to create and use modern packages in the Python ecosystem.
+++
Explore this book {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: https://geographicdata.science/book/intro.html

**Geographic Data Science**
^^^
```{image} https://geographicdata.science/book/_static/logo.png
:height: 100
```

Solving geographic data problems with modern open source tools.
+++
Explore this book {fas}`arrow-right`
:::
::::



#######################
#######################
::::{grid}
:gutter: 1

:::{grid-item-card} Health
:columns: 4
Body health.
:::

:::{grid-item-card} Cook
:columns: 4
Cooking study.
:::

:::{grid-item-card} Information
:columns: 4
Certificate.
:::

:::{grid-item-card} PhD_application
:columns: 4
...
:::

:::{grid-item-card} Photo
:columns: 4
...
:::

:::{grid-item-card} Rice-file
:columns: 4
...
:::

:::{grid-item-card} USTC-file
:columns: 4
...
:::
::::




---
**Programming:**

1. **Programming Environment**: configure the programming environment in MacOS.

2. **Programming Manual and Scripts**: some common and useful code scripts.

3. **Parallel Computing and Hybrid Programming**: common strategies for parallel computing and hybrid programming between Python and C++.

4. **Seismic Data Processing**: seismic data processing process included *read/write/filter/trim...* and so on.

---




## About the Book

The Seismology Notebook is powered by [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), which use [MyST](https://sphinx-design.readthedocs.io/en/sbt-theme/grids.html) Markdown syntax.


All the source file are edited by VSCode, `run_jb_build.py` is a Python script to build the HTML and fresh it in Chrome browser automatically. 

- `run_jb_build.py` uses `git` to check whether any of the files have been changed. If something changed, it will rebuild the notebook and refresh the HTML in Chrome browser.

- `run_jb_build.py` uses `git` in `dev` branch, and after modifying all files, you need switch to `main` branch, and push it to Github.

- put `run_jb_build.py` in the root directory of your notebook project, and run it before you edit anytime.

::::{toggle}
```bash
#!/Users/yinfu/opt/miniconda3/bin python3
# -*- coding: utf-8 -*-
"""
Use jupyter-book generate html automatically.
    1. Download Chrome-driver Plug-in for selenium package from https://chromedriver.chromium.org/
    2. Make sure the project have 'dev' branch
    3. Run this script in the root directory of book-project

@Author: Fu Yin || Fri Jul 22 21:59:08 2022
"""

import os
import time
import subprocess
from selenium import webdriver

#%% Functions
def jb_build(driver,book):
    print("Start:", time.ctime())
    os.system(f"jb build {book}")
    driver.refresh()

def git_status():
    cmd_git = subprocess.Popen(['git status -s'], shell = True, \
        stdin = subprocess.PIPE, stdout = subprocess.PIPE, cwd = "./")  
    cmd_out_raw = cmd_git.stdout.read()
    cmd_git.wait()
    cmd_git.stdout.close()
    cmd_out = cmd_out_raw.decode()
    out = cmd_out.split("\n")
    return out

def git_commit():
    os.system(""" git add . """)
    os.system(""" git commit -m "auto" """)

def main():
    driver= webdriver.Chrome()
    driver.get(url)
    os.system("git switch dev")
    jb_build(driver, book)
    while True:
        time.sleep(sleep_time)
        out = git_status() 
        if len(out) != 1:
            print("Change number = ", len(out))
            jb_build(driver, book)
            git_commit()
        else:
            print("No change and continue...")
            continue

#%% Main
url = "file:///Users/yinfu/code/1-Notebook/Notebook/book/_build/html/intro.html"
book= "./book"         # jupyter-book build ./book
sleep_time = 0.1        # unit/s

if __name__ == '__main__':
    main()
```
::::



<!-- ```{tableofcontents}
```

Here is my nifty citation {cite}`holdgraf_evidence_2014`.

```{bibliography}
``` -->




