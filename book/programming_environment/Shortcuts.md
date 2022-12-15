# Shortcuts

<style>
table th:first-of-type {
    width: 40%;
}
table th:nth-of-type(2) {
    width: 60%;
}
</style>



## Mac

|      Function     |    Shortcuts    |      
| :--------------:  | :-------------: |
| `Force Quit Application` | {kbd}`ESC` + {kbd}`Option` + {kbd}`Command`   |
| `Copy`            | {kbd}`Command` + {kbd}`C`   |
| `Paste`           | {kbd}`Command` + {kbd}`V`   |
| `Cut`             | {kbd}`Command` + {kbd}`X`   |
| `Save`            | {kbd}`Command` + {kbd}`S`   |
| `Quit`            | {kbd}`Command` + {kbd}`Q`   |
| `Close`           | {kbd}`Command` + {kbd}`W`   |
| `Big++`           | {kbd}`Command` + {kbd}`+`   |   
| `Small--`         | {kbd}`Command` + {kbd}`-`   |
| `Switch Language Input` | {kbd}`Command` + {kbd}`Option`   |
| `View Hidden files` | {kbd}`Shift` + {kbd}`Command` + {kbd}`.`  |
|    |    |

## Finder

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `New Tab`         | {kbd}`Command` + {kbd}`T`   |
| `As Icons`        |  {kbd}`Command` + {kbd}`1`  |
| `As List`         | {kbd}`Command` + {kbd}`2`   |
| `As Columns`      |  {kbd}`Command` + {kbd}`3`  |
| `As Gallery`      | {kbd}`Command` + {kbd}`4`   |
| `Delete`          | {kbd}`Command` + {kbd}`Delete` |
|    |    |



## Xnip

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `Screenshot`      |  {kbd}`Command` + {kbd}`Control` + {kbd}`X`  |
|    |    |



## AltTab

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `Switch`          |  {kbd}`Option` + {kbd}`Tab`  |
|    |    |



## 有道翻译

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `Screenshot Translation`  | {kbd}`Command` + {kbd}`Option` + {kbd}`X`   |
|    |    |



## Paste

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `Clipboard`   | {kbd}`Command` + {kbd}`V` + {kbd}`Shift`   |
| `Left Choose`   | {kbd}`Command` + {kbd}`[`   |
| `Right Choose`  | {kbd}`Command` + {kbd}`]`   |
|    |    |



## PDF Expert

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `New Tab`         | {kbd}`Command` + {kbd}`T`|
| `Single Page`     |  {kbd}`Command` + {kbd}`1`  |
| `Two Pages`       | {kbd}`Command` + {kbd}`2`   |
| `Split Vertical`  | {kbd}`Command` + {kbd}`3`   |
| `Split Horizontal` |  {kbd}`Command` + {kbd}`4`  |
| `Underline`       |  {kbd}`Option` + {kbd}`1`  |
| `Highlight`       |  {kbd}`Option` + {kbd}`2`  |
| `Text`            |  {kbd}`Option` + {kbd}`3`  |
|    |    |


Follow the process to set shortcuts: `System Preferences` -> `Keyboard` -> `Shortcuts` -> `App Shortcuts` -> `+ Applicaiton` -> `PDF Expert`
:::{toggle}
```{figure} ./Shortcuts_file/Shortcuts-1.jpg
---
scale: 100%
align: center
name: shortcuts-1
---
PDF Expert Shortcuts
```
:::


## Iterm2

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `New Tab`         | {kbd}`Command` + {kbd}`T`   |
| `Split Vertical`  | {kbd}`Command` + {kbd}`D`   |
| `Split Horizontal` | {kbd}`Command` + {kbd}`D` + {kbd}`Shift`   |
| `First Tab`       |  {kbd}`Command` + {kbd}`1`  |
| `Second Tab`      | {kbd}`Command` + {kbd}`2`   |
|    |    |

## Jupyter Lab/notebook


Double-click to open `ipynb` file in Mac.

:::{toggle}
```{figure} ./Shortcuts_file/Shortcuts-2.jpg
---
scale: 50%
align: center
name: shortcuts-2
---
JupyterLab_launcher
```
:::

- Open up `Automator` app, click `New Document`, then click `Application` and choose `Run Shell Script`.

- Set the `Pass Input` option to `as arguments`

- Copy and paste the following code
    ```bash
    variable="'$1'"
    the_script='tell application "terminal" to do script "jupyter lab '
    osascript -e "${the_script}${variable}\""
    ```

- Finally, save the file as `JupyterLab_launcher` and choose `File Format` as `Application`.




Now you can double-click a `.ipynb` file and it will be opened with JupyerLab. It's the same as `juoyter notebook`. More info can refer to https://samedwardes.com/2020/01/31/open-ipynb-with-double-click/


## VSCode
Open two screens:
- {kbd}`Command` + {kbd}`Shift` + {kbd}`P`: `> Workspace: Duplicate As Workspace in New Window`

|    Function       |    Shortcuts    |      
| :------------:    | :-------------: |
| `Universal Shortcut Key` | {kbd}`Command` + {kbd}`Shift` + {kbd}`P`   |
| `Annotation`      | {kbd}`Command` + {kbd}`/`   |
|    |    |



