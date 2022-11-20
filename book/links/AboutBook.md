# About the Book

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

