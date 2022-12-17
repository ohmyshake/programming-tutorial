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



## REPL Mode



共4中模式(官网是5种模式)，按住 ] 进入包管理模式

按住 ; 进入shell模式，可以使用bash中存在的shell命令，如ls,cd..

按住 ？进入help模式，输入任意函数，即可返回使用说明

所有模式通过 ’删除键‘返回

reference: https://docs.juliacn.com/latest/stdlib/REPL/#Pkg-mode




## Run Scripts

	
a. Bash terminal: julia 脚本名称.jl   

b. Julia REPL: include("脚本名称.jl")   # 可以查看变量的值，推荐

c. IDE 中，见后文 VScode 内容




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

## Package Managment

```bash

versioninfo() 			# 查看Julia配置信息，版本和下载源路径等

using XXX 			# 使用某个包


```

Package managment mode:

```bash
status or st			# 查看所有安装包的版本
# 等价于 using Pkg; Pkg.status()

add XXX 			# 安装包
# help 模式下查看 Pkg.add 说明文档，可安装指定版本与本地包
# add XXX@1.6.2 安装指定版本？

rm XXX 				# 删除包

update XXX  			# 更新包

test XXX 			# 测试包

add SeisIO; build [Package]; precompile # 构建与预编译包?

```




安装本地开发包：

	包管理模式下: dev .  或者给定包的路径 dev folder_name




7. VScode IDE for Julia
###########################
另外可选的 atom 或者 jupyterlab or jupyter notebook

	a. 首先需要在自己环境中配置好 Julia，将其加入环境变量中

	b. 安装 VScode 中的 Julia 插件，如果 Julia 在环境变量中，VScode 会自动找到并配置好；如果想自己配置或者修改 julia 解释器路径，在 setting 中搜索 Julia Extensions, 找到 Julia: Executable Path 修改即可，例如修改为 /Users/yf/.local/bin/julia-1.6

	c. VScode 中执行 Julia 脚本有两种方式：点击执行三角符号，在 bash 中执行；同时按住 shift+回车，在 Julia REPL 中执行，此时可以查看变量（推荐）

	d. Control+回车，会打开 VScode 中 Julia 的 REPL






8. Jupyter IDE for julia
###########################

	a. 安装插件 add IJulia 	# 我已经安装了 conda jupyter 不需要再使用 IJulia 安装一次 jupyter 
	
	b. Bash 中直接运行：jupyter lab or jupyter notebook, 可选择Julia解释器

	c. 注意 jupyter 似乎只能识别最高版本的 Julia kernal? 我暂时没有解决方案

	reference: https://julialang.github.io/IJulia.jl/stable/manual/usage/
		   https://zhuanlan.zhihu.com/p/158912631




9. Julia 常用安装包
###########################

--. 地震学包：
	
	SeisIO			# 地震数据输入输出

	SeisNoise 		# ambient noise 互相关

	


--. 其他包：

	Revise			# VScode 中调用 Julia ？？ Hot-fix 在线修复，必须第一个加载然后再加载别的包；VScode自带Revise; 但其不是万能的，不能修改常量以及结构体的定义，这种情况仍然需要重启 Julia 
	
	PkgServerClient  	# 自动匹配最优网络镜像

	Plots 			# 画图包

	IJulia 			# for jupyter

	OhMyREPL 		#

	Latexify			#

	PowerMonitor		#

	BenchmarkTools 		#

	Cthulhu			# 

	Debugger			#

	ThreadPools		# 多线程包






10. Julia 使用注意事项
###########################

	a. Julia community 发展很快，一些包的接口会经常发生变化，导致不同版本之间的不兼容情况，例如：
		
		- 使用 “SeisIO” Project.toml 文件说明需要 HDF5 = "0.12.3, 0.13" 版本

		- 但使用 “SeisNoise” 需要使用 “Plots” 包，新版本的 “Plots” 不支持 HDF5 = "0.12.3, 0.13" 这些老版本，code can run but warning

		- 解决办法是，使用老版本的 “Plots” 或者忽略 warning

	reference: https://github.com/JuliaPlots/Plots.jl/issues/3235


	b. Julia 的 JIT 技术导致第一次运行 code 时，速度很慢，所以适合在 IDE 中写代码，且对画图plot不太友好，建议用matplotlib可视化









