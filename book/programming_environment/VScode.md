# VSCode

- Author: *{{Fu}}*
- Update: *July 28, 2022*
- Reading: *10 min*

---


## Install


Download [VSCode](https://code.visualstudio.com/download) (Visual Studio Code) and install directly.


## Sign-in and Sync

Recommend to use `Microsoft` account to sign in, and `Github` account is not worked now (until July 28, 2022).

```{figure} ./files/VSCode-2.jpg
---
scale: 100%
align: center
name: vscode-account
---
My `Microsoft` account to sign in VSCode
```

Refer to [Microsoft sync docs](https://code.visualstudio.com/docs/editor/settings-sync) before use `sync` function.


## Theme
- My color theme: `Monokai`

- My file icon theme: `VSCode icons`



## Plugin

**Universal shortcut key**: {kbd}`Command` + {kbd}`Shift` + {kbd}`P`. 

- It's a command line-like interface, which will be automatically open with an `>` symbol. 

- We can input various plugins command to check their options and settings. If you delete `>` symbol, you can search file's location.


```{figure} ./files/VSCode-1.jpg
---
scale: 70%
align: center
name: vscode-shortcut
---
{kbd}`Command` + {kbd}`Shift` + {kbd}`P`
```

**My plugins list**
:::{toggle}
<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

|        Name       |       Purpose       |      
|    ------------   |    -------------    |  
|   `Remote-SSH`    | Open any folder on a remote machine using SSH and take advantage of VS Code's full feature set |  
|   `MyST-Markdown` | The official Markdown syntax extension for MyST (Markedly Structured Text) |
|   `Python`        | IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests... |
| `Pylance` | A performant, feature-rich language server for Python in VS Code |
|   `Jupyter`       | Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more |
|   `Live Preview`  | Hosts a local server in your workspace for you to preview your webpages on |
| `reStructuredText`| reStructuredText language support (RST/ReST linter, preview, IntelliSense and more) |
|   `vscode-pdf`    | Display pdf file in VSCode |
|   `vscode-icons`  | Icons for Visual Studio Code |
|   `CMake Tools`         | Extended CMake support in Visual Studio Code |
|   `Julia`         | Julia Language Support |
|   `C/C++`              | C/C++ IntelliSense, debugging, and code browsing.                    |
| `C/C++ Themes` | UI Themes for C/C++ extension.  |
| `C/C++ Extension Pack` | Popular extensions for C++ development in Visual Studio Code.  |
| `LaTeX Workshop` | Boost LaTeX typesetting efficiency with preview, compile, autocomplete, colorize, and more. |
| `Makefile Tools` | Provide makefile support in VS Code: C/C++ IntelliSense, build, debug/run.  |

:::



### Remote-SSH
After configuring the `SSH key`, use `Remote-SSH` plugin.

:::{tip}
If the Shell used by the remote is `Bash`, and the local machine is `Zsh`, you may experience failure to boot VSCode terminal problem. In this case, you need to modify the configuration file of VSCode to restart the terminal correctly.

Open the command panel, input the `Remote-SSH: Settings`, search `terminal.integrated.shell.linux`, and change `/bin/zsh` to `/bin/bash`. Please refer to
[microsoft/vscode-remote-release issues #38](https://github.com/microsoft/vscode-remote-release/issues/38)
:::




## Reference

