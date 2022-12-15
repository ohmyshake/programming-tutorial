# Latex

- Author: *{{Fu}}*
- Update: *July 29, 2022*
- Reading: *30 min*

---

## Introduction

**`TEX`** is software developed by **Donald E. Knuth** for typesetting words and mathematical formulas.
**`LaTeX`** is a `Format` that uses the `TEX` software as the typesetting engine, which can be roughly interpreted as an encapsulation of `TEX`.

::::{dropdown} Do you know the concept of "Distribution", "Compiler", "Macro-package", and "Editor" in LaTeX?
:color: info
:icon: info

**Layout Engine**(排版引擎):
- a program that compiles source code and generates documents, such as `pdftex`, `xetex`, and `luatex`. Sometimes also called the compiler.

**Format**(格式):
- a set of code that defines a set of commands. `LaTeX` is one of the most widely used formats.

**Compiling Command**(编译命令): 
- a program which combines `Engine` and `Format` to read source files and outputs PDFs. For example, the `xelatex` command is that combines the `xetex Engine` and `LaTeX Format`.

| Compiling Command | Concept        |      
|  ------------   |  ------------- |  
| `latex`    | The engine of the underlying invocation is actually `pdftex`. This command generates a Device Independent (DVI) file |
| `pdflatex` | The engine of the underlying invocation is actually `pdftex`. This command generates a PDF file    |
| `xelatex`  | The engine for the underlying invocation is `xetex`, which supports `UTF-8` encoding and `TrueType/OpenType` fonts. Current **Chinese typesetting solutions** are based on `xelatex`   |
| `lualatex` | The engine for the underlying invocation is `luatex` which is an evolution of the `pdftex` engine. In addition to supporting `UTF-8` encoding and `TrueType/OpenType` fonts, also supports the extension of `tex` functionality through the `Lua` language |
---

:::{note}
The Compiling Command `latex`  and the Format `LaTeX` are often confused.
:::


**Macro-package**(宏包):  
- LaTeX code package to enable extended functionality, such as `fontspec` and `natbib`

**Distribution**(发行版): 
- a collection of compilers, macro packages, editors, and other tools, such as `TeX Live`, `MacTeX` and `MikTeX`


**Editor**(编辑器):  
- a tool for editing LaTeX source files, such as `TeXShop`, `TeXworks`, `WinEdt` and `VSCode`
::::


The following are the major `Distribution`s in different systems:

| Distribution | Linux | macOS | Windows|
|---|---|---|---|
|TeX live | yes | yes | yes|
|MacTeX | | yes |
|MikTeX | yes | yes | yes|
---


The common file format in `LaTex`:

- **`.tex`**: source file

- **`.bib`**: the references document, and the `.bbl` is the file after using `BibTex` compiling`

- **`.sty`**: the package file, usually imported using `\usepackage`

- **`.cls`**: the class file, usually imported through the `\documentclass` command at the beginning of the document

A learning Latex chinese [website](https://www.latexstudio.net/articles/)



## Install 

The full **`LaTeX`** distribution are recommended, and install it via [TexLive](https://github.com/scottkosty/install-tl-ubuntu) on Linux, and via [MacTex](https://www.tug.org/mactex/) on MacOS.

- MacTex Webpage: https://www.tug.org/mactex/

- MacTex Mirror in USTC: http://mirrors.ustc.edu.cn/CTAN/systems/mac/mactex/MacTeX.pkg

:::{note}
The full software of **MacTex** is very large, and it takes about **7.98G** space. However, the lightweight [**TinyTeX**](https://yihui.org/tinytex/) (< 100MB) is not recommended because it need install all the packages by yourself.
:::





::::{dropdown} How to uninstall?
:color: info
:icon: info

If you want to upgrade **`LaTeX`** to the latest version and want to reclaim space by erasing the old distribution, you need to uninstall it and reinstall. ([`Scrolling Update`](https://www.tug.org/texlive/upgrade.html) are not recommended)

:::{dropdown} Why `tlmgr` command cannot be used for upgrade?
The Latex distribution is updated once a year. After each update, the `tlmgr` command cannot be used because the remote repository has been changed to the latest version. For example the version from "2021" to "2022", so the corresponding remote repository cannot be found.
:::

The uninstallation instructions provided by the [official website](https://www.tug.org/mactex/uninstalling.html):

```bash
# Uninstalling TeX
sudo rm -r /usr/local/texlive/2022 # In general, we can also see that there is another directory called "texmf-local" under TexLive path. It is just an empty directory tree according to offical website. If you are obsessive-compulsive, delete it.

# Uninstalling the GUI Applications
sudo rm -r /Applications/Tex 

# Uninstalling the TeX Distribution Data Structure
sudo rm -r /Library/TeX
```
::::


## Configration

### Latexmk

If you use `cross-references` or use `BibTeX` for your bibliography, you often have to run compiling command such as `xelatex` to do those work, which need **compile multiple times**. 

The following code is about how to compile the document with `BibTex` references, refer to the [example](https://www.cnblogs.com/yifdu25/p/8330652.html).

```bash
xelatex -shell-escape file.tex
bibtex file.aux
xelatex -shell-escape file.tex
xelatex -shell-escape file.tex
```

::::{dropdown} Why it need compile multiple times?
:color: info
:icon: info

- `TEX` needs to refer to the document itself (`tex` -> `tex`). Those information can only be known once you run it one time. For example, I want to know what page Chapter 2 starts on, and what a particular formula is in the document.

- `TEX` needs to use the output of other programs, and the input of other programs is `TEX`'s output (`tex` -> `other` -> `tex`). For example, `references` (tex -> bibtex -> tex), `indexes`, etc.. 
::::

[Latexmk](https://ctan.org/pkg/latexmk?lang=en), a `Perl` script, only needs compile one time. It completely automates the process of generating a `LaTex` document. `Latexmk` is part of `MacTeX` and `MikTeX` and it is bundled with many Linux Distributions.


**`Running latexmk`**
```bash
latexmk file.tex
```

**`Cleaning Up`**

```bash
latexmk -c
```

**`Specify "xelatex" Compile`**

```bash
latexmk -xelatex file.tex
```


### Makefile

You can run `make` and `make clean` for your `main.tex` document. The following is the content of `Makefile` file:

::::{toggle}
```bash
$ cat Makefile
MAIN = main
LATEXMK = latexmk -xelatex -shell-escape

all: main clean

main:
	$(LATEXMK) $(MAIN).tex

clean: 
	latexmk -c $(MAIN).tex
	rm -r _minted-main
	rm -r *.bbl
```
::::



### VSCode

Download the plugin, **`LaTex Workshop`**, in VSCode Extensions. 
- For each Latex project, put the `.vscode/settings.json` file in the root directory.
- Please check `latex-workshop.latex.tools` and `latex-workshop.latex.recipes` options in `.vscode/settings.json` file.

Here is my `.vscode/settings.json` file:
::::{toggle}
```bash
{
    "latex-workshop.intellisense.package.enabled": true,
    "latex-workshop.intellisense.unimathsymbols.enabled": true,
    "latex-workshop.latex.build.forceRecipeUsage": true,
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk -xelatex",
            "tools": ["latexmk -xelatex"]
        }
    ],
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",   // "/Library/TeX/texbin/xelatex"
            "args": [
                "-shell-escape",    // use pygments to highlight syntax code
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "latexmk -xelatex",
            "command": "latexmk",   // "/Library/TeX/texbin/latexmk"
            "args": [
                "-xelatex",
                "-shell-escape",    // use pygments to highlight syntax code
                "-file-line-error",
                "-halt-on-error",
                "-interaction=nonstopmode",
                "-synctex=1",
                "-pv-",
                "-pvc-",
                "-outdir=%OUTDIR%",
                "%DOCFILE%"
            ],
            "env": {}
        }
    ]
}
```
::::



### Overleaf

[Overleaf](https://www.overleaf.com/) is a collaborative cloud-based LaTeX editor used for writing, editing and publishing scientific documents. It partners with a wide range of scientific publishers to provide official journal LaTeX templates, and direct submission links.




## Manual

- The detailed manual, please refer to the book: 一份不太简短的 LaTeX2e 介绍（[lshort-zh-cn](http://mirrors.ustc.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf)).

- [Latex-Template-Rice-USTC](https://github.com/OUCyf/Latex-Template-Rice-USTC) is my `Latex` project , which is a template including book, thesis, and assignment for Rice and USTC university. You can use it via Overleaf https://www.overleaf.com/latex/templates/latex-template-rice-ustc/tkdscxhkympd

- [CV](https://github.com/OUCyf/CV) is my academic CV powered by `LaTeX`.




## Reference

1. [USTC LaTeX 新手入门指南](https://github.com/ustctug/ustcthesis/wiki/%E6%96%B0%E6%89%8B%E6%8C%87%E5%8D%97)

1. Book: 一份不太简短的 LaTeX2e 介绍（[lshort-zh-cn](http://mirrors.ustc.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf)）

1. Book: LaTeX 入门（[亚马逊](https://www.amazon.cn/图书/dp/B00D1APK0G/)）




