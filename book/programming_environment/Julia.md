# Julia

- Author: *{{Fu}}*
- Update: *Dec 17, 2022*
- Reading: *30 min*

---



## Installation

- (**not recommend**)  Download `dmg` package from official website with MacBook，click install, and then add the env variable in `~/.zshrc` as following:

    ```bash
    # >>> Julia >>>
    export PATH="/Applications/Julia-1.6.app/Contents/Resources/julia/bin/:$PATH"
    # <<< Julia <<<
    ```

- (**recommend**) Using [jill.py](https://github.com/johnnychen94/jill.py) to download julia and manage multiple versions. Use `pip install jill` firstly, then:

    ```bash
    # install julia with version 1.8
    jill install 1.8 		

    # check all versions you have installed
    jill list  			

    # set the default version to 1.6
    jill switch 1.6 		
    ```

::::{dropdown} Do you know how to uninstall julia?
:color: info
:icon: info

- If you install the `pkg` package into Applications, you can delete `~/.Julia` folder and the env variable.

- If you use `jill` to install multiple versions of julia, just want to delete one version.
Remove the symlinks in symlink_dir, e.g., `~/.local/bin/julia-1.6`.
::::


::::{dropdown} Wether to delete `~/.julia` folder?
:color: info
:icon: info

* All Julia packages are installed in ~/.julia/packages/ in version-agnostic manner; whether a specific package version is used depends on the environment you're using. For instance, ~/.julia/environments/v1.6/Manifest.toml specifies all julia package versions. There isn't ~/.julia/packages/v1.6 stuff. Thus you don't need to worry about this at all.

* If you want to cleanup some spaces, you can try pkg> gc in Pkg mode. Or if you insist, another way is to manually remove ~/.julia/packages folder and then pkg> instantiate to rebuild it.

reference：https://github.com/johnnychen94/jill.py/issues/96
::::


## startup.jl  
The `startup.jl ` is initialization file of julia REPL.
Open the `~/.julia/config/startup.jl` file, and then add the following info for example:

```julia
if VERSION >= v"1.4"
    try
        using OhMyREPL
    catch e
        @warn "error while using OhMyREPL" e
    end
end
```


## Three Modes in REPL



Open the julia firstly, and then

- type `]` will into the pkg managment mode.

- type `;` will into the shell mode.

- type `?` will into help mode.

- type `delete` will return the last mode.




## Run Scripts

	
- Open the terminal, and then run `julia name.jl`.   

- In Julia REPL, type `include("name.jl")`












## VScode IDE for Julia

- Install julia extensions, and set the interpreter that you want to use.

- The `shift` + `return` will run the code in REPL,
and `control` + `return` will open the REPL in VScode.



## Package

```julia
$ julia

# check the default info of julia
versioninfo()

# using pkg
using XXX 			


# install the local pkg
$ ]
dev folder_name

# check all pkgs installed
$ ]
status or st

# install pkg with the specifical version
$ ]
add XXX@1.6.2 		

# remove pkg
$ ]
rm XXX 			

# update pkg
$ ]
update XXX  

# test pkg
$ ]
test XXX 			

```



**geophysics package**:

|     Name     |    Purpose    |     Way       |     
| ------------ | ------------- | :-----------: |
| `Revise`       | ...           |    |
| `PkgServerClient`   | Set mirror servers for China region      |      |
| `Plots`   |        |      |
| `OhMyREPL`   |        |      |
| `BenchmarkTools`   |        |      |
| ``   |        |      |

**scientific computation-related package**:

|    Name       |    Purpose    |    Way       |     
| ------------  | ------------- | :----------: |
| `SeisIO`       | Seismic data process          | pkg       |
| `SeisNoise`   |  Ambient noise cc      | Pkg     |
| `FwiFlow`   | CO2 simulation       |      |
| ``   |        |      |


