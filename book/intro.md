# Introduction ✨

Welcome to **Programming Notebook**, a notebook mainly about my scientific notes and gains in learning **Programming** and **Geophysics**, and I am very glad if it is helpful for your researches. 

**Enjoy!!** 👋👋👋

```{margin} About Author
I'm [**Fu Yin**](https://yinfu.info/), a geophysics graduate student at Rice University.
```

:::{admonition} Admonition
There is no guarantees of correctness, and if you spot an error or a doubtful statement, kindly let me know.
:::


---
The main content of the notebook is as follows:
::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 2

:::{grid-item-card}
:link: ./programming_environment/Overview.html
:class-body: text-center
:class-header: bg-light text-center
**Programming Environment**
^^^
```{image} ./intro_files/macos.jpg
:height: 100
```
Configure the programming environment in MacOS.
:::

:::{grid-item-card}
:link: https://github.com/orgs/executablebooks/discussions
:class-body: text-center
:class-header: bg-light text-center
**App Development**
^^^
```{image} ./intro_files/pyside6.png
:height: 100
```
Develop a python package, GUI, and Dashboards.
:::

:::{grid-item-card}
:link: https://github.com/orgs/executablebooks/discussions
:class-body: text-center
:class-header: bg-light text-center
**Parallel Computing & HPC Platform**
^^^
```{image} ./intro_files/hpc.webp
:height: 100
```
Parallel computing skills in Python and C++, and HPC tutrials.
:::

:::{grid-item-card}
:link: https://github.com/orgs/executablebooks/discussions
:class-body: text-center
:class-header: bg-light text-center
**Machine Learning & Deep Learning**
^^^
```{image} ./intro_files/network.jpg
:height: 100
```
Machine learning and deep learning approaches in Python.
:::

:::{grid-item-card}
:link: https://github.com/orgs/executablebooks/discussions
:class-body: text-center
:class-header: bg-light text-center
**Daily Software**
^^^
```{image} ./intro_files/software.webp
:height: 100
```
Useful softwares in MacOS system.
:::

:::{grid-item-card}
:link: https://github.com/orgs/executablebooks/discussions
:class-body: text-center
:class-header: bg-light text-center
**Geophysics Software**
^^^
```{image} ./intro_files/specfem3d.jpg
:height: 100
```
Useful geophysics softwares.
:::
::::

---



## Sponsoring ✨
**If you enjoy the blog, please consider sponsoring 🍿 :**

⏬ &nbsp; For Chinese guys:

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 2

:::{grid-item-card}
:class-body: text-center
:class-header: bg-light text-center
**Alipay**
^^^
```{image} ./intro_files/Alipay.jpg
:height: 150
```
:::

:::{grid-item-card}
:class-body: text-center
:class-header: bg-light text-center
**WeChat**
^^^
```{image} ./intro_files/WeChat.jpg
:height: 150
```
:::

::::



⏬ &nbsp; For Non-Chinese guys:

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 2

:::{grid-item-card}
:link: https://www.buymeacoffee.com/yinfu
:class-body: text-center
:class-header: bg-light text-center
**Coffee**
^^^
```{image} https://user-images.githubusercontent.com/1376749/120938564-50c59780-c6e1-11eb-814f-22a0399623c5.png
:height: 70
```
:::

:::{grid-item-card}
:link: https://www.paypal.me/yinfu123
:class-body: text-center
:class-header: bg-light text-center
**PayPal**
^^^
```{image} https://cdn.jsdelivr.net/gh/twolfson/paypal-github-button@1.0.0/dist/button.svg
:height: 100
```
:::

::::




## About the Book ✨

The notebook is powered by [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), which use [MyST](https://sphinx-design.readthedocs.io/en/sbt-theme/grids.html) Markdown syntax.


All the source file are edited by VSCode, `run_jb_build.py` is a Python script to build the HTML and fresh it in Chrome browser automatically. 

- `run_jb_build.py` uses `git` to check whether any of the files have been changed. If something changed, it will rebuild the notebook and refresh the HTML in Chrome browser.

- `run_jb_build.py` uses `git` in `dev` branch, and after modifying all files, you need switch to `main` branch, and push it to Github.

- put `run_jb_build.py` in the root directory of your notebook project, and run it before you edit anytime.

::::{toggle}
```python
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












