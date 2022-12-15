# PyGMT

- Author: *{{Fu}}*
- Update: *July 30, 2022*
- Reading: *10 min*

---

## Introduction


[PyGMT](https://github.com/GenericMappingTools/pygmt) is a library for processing geospatial and geophysical data and making publication quality maps and figures. It provides a Pythonic interface for the [Generic Mapping Tools (GMT)](https://github.com/GenericMappingTools/gmt), a command-line program widely used in the Earth Sciences.



## Installation
It's recommended to install `Pygmt` into `base` environment.

:::::{tab-set}
::::{tab-item} conda

Simple installation using conda:
```bash
$ conda install --channel conda-forge pygmt
```
::::

::::{tab-item} mamba
If you use mamba:
```bash
$ mamba install --channel conda-forge pygmt
```
::::
:::::



## Data Set Config
<!-- 269.69 -->

The directory that GMT automatically downloads the data file from the server is `~/.gmt/server`. About the detailed info, please check [GMT Chinese Manual about Geodata set session](https://docs.gmt-china.org/latest/dataset/usage/#gmt)

**Mirror**
    
The `GMT` data server currently has multiple [mirrors](https://www.generic-mapping-tools.org/mirrors/) around the world. 
Run the following command to set your mirror channel:

```bash
# If you are in China
$ gmt set GMT_DATA_SERVER http://china.generic-mapping-tools.org

# If you are in US West Coast
$ gmt set GMT_DATA_SERVER http://sdsc-opentopography.generic-mapping-tools.org

# Show URL of the remote GMT data server
$ gmt --show-dataserver
```
Then the above command will generate a `gmt.conf` file in your current path, copy it to the `GMT` user directory `~/.gmt`.




**GMT Built-in Data**

- [GSHHG: Global high-resolution shoreline data](https://docs.gmt-china.org/latest/dataset/gshhg/): includes coastlines, rivers and borders.

- [DCW: Digital Chart of the World](https://docs.gmt-china.org/latest/dataset/dcw/): includes the boundary of seven continents, the boundary of 250 countries or regions in the world, and the provincial/state boundary of 8 major countries.





**GMT Romote Data**

- [Earth_relief](https://docs.gmt-china.org/latest/dataset/earth-relief/): global relief data, automatically download into `~/.gmt/server/earth/earth_relief` directory
- [Earth_age](https://docs.gmt-china.org/latest/dataset/earth-age/): the age of the earth's oceanic crust, automatically download into `~/.gmt/server/earth/earth_age` directory
- More info please check [GMT Chinese Manual ...](https://docs.gmt-china.org/latest/dataset/#id2)

I have downloaded the `Earth_relief` dataset into `~/.gmt/server/earth/earth_relief` directory, with the resolution is `30s` which equal to `1 kilometer`(size of ~778M). Download data by the following command `gmt get`:

```bash
$ gmt get -Ddata=earth_relief -I30s
```

**Custom Data**

Users can also customize their own database directory to store their own data in it, compared with the default directory `~/.gmt/server`. My database directory is `~/data/GMTDB/`, add the following lines into your configuration file.

```bash
$ vim ~/.zshrc
# >>> pygmt(base) initialize >>>
export GMT_DATADIR=/Users/yinfu/data/GMTDB/
# <<< pygmt(base) initialize <<<
```
 
Then you can check the whether it has successed:

```bash
# Show full path of user's ~/.gmt dir
$ gmt --show-userdir

# Show directory/ies with user data.
$ gmt --show-datadir
```



## My Data List

:::{toggle}
|    Name       |    From       |   Directory  |     
| ------------  | ------------- | :----------: |
| `Earth_relief with 30s`   | GMT remote data       |  `~/.gmt/server/earth/earth_relief`    |
| ``   | ...       |  `~/data/GMTDB/`    |

:::



## Parameters Setting


Please check [GMT Chinese Manual about parameter configuration](https://docs.gmt-china.org/latest/conf/overview/)


`pygmt` use `pygmt.config` to set the default parameters.

```python
import pygmt

pygmt.config(PARAMETER = value)
```
 
