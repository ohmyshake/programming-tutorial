# Python Package 

- Author: *{{Fu}}*
- Update: *Dec 15, 2022*
- Reading: *30 min*

---



## Setup Tool



## Poetry

follow the instructions below: https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry/

1. use `conda` create a new environment, only install `python`

    ```bash
    conda env create -f environment.yml  # create env according to .yml file
    conda env export > environment.yml  # export .yml file
    conda activate jupiter-dev  # activate env
    ```

2. use `poetry` install other python package

install poetry first
```bash
curl -sSL https://install.python-poetry.org | python3 - # do not use pip

mkdir $ZSH_CUSTOM/plugins/poetry # add poetry into oh-my-zsh plugins
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```


```bash
poetry config virtualenvs.create false  # do not allow poetry create env
poetry init  # this command will create pyproject.toml file
poetry install  # this command will install some package mentioned in 'pyproject.toml', and also generate a 'poetry.lock' file
# Now you can change 'pyproject.toml' by hand
poetry update # update the new info in 'pyproject.toml' into 'poetry.lock' file
```



## Sphnix




## Github Action





## Buy and Bind Domain Name with Github Pages


### Buy from Namesilo
The default domain-name in github pages is `your_name.github.io`, but you can set your own domain-name. Firstly, buy a domain-name; I got `yinfu.info` domain-name from [**Namesilo**](https://www.namesilo.com/), the purchase process is showing below:

Create an account and check your favorite domain-name whether be used or not, then just buy it. Now use **Namesilo** to resolve the domain-name: click on the `blue ball` to edit `DNS`; you can set by yourself or using the template provided below. Generally setting `example.com` and `www.example.com` to point to your own server IP address is sufficent, set `A` and `CNAME`:


- **My domain-name information:**


```{figure} ./files/2022-02-21-2.jpg
---
scale: 50%
align: center
name: diskutil-list
---
My `diskutil list`
```

- **For `A`:**


| HOSTNAME  | TYPE      | ADDRESS/VALUE |
| :-------: | :-------: | :-----------: |
| none      | A         | 185.199.108.153 |


\note{Use `ping OUCyf.github.io` to get id of ADDRESS/VALUE}

- **For `CNAME`:**


| HOSTNAME | TYPE | ADDRESS/VALUE|
|-----------|-----------|-----------|
| www | CNAME | oucyf.github.io |


- **The screenshot of my setting:**


```{figure} ./files/2022-02-21-1.jpg
---
scale: 50%
align: center
name: diskutil-list
---
My `diskutil list`
```

- **Renew domains**

    Click `Renew Domains` then `CHECKOUT`.




### Bind with Github

Add the `CNAME` file to the github Pages repository at root directory and write your domain name inside:


```{figure} ./files/2022-02-21-3.jpg
---
scale: 50%
align: center
name: diskutil-list
---
My `diskutil list`
```

Or set `custom domain` directly to `Github Pages` in `Settings` of github. Github will automatically adds the `CNAME` file.


```{figure} ./files/2022-02-21-4.jpg
---
scale: 50%
align: center
name: diskutil-list
---
My `diskutil list`
```

Enforce `HTTPS` which provides a layer of encryption that prevents others from snooping on or tampering with traffic to your site. When `HTTPS` is enforced, your site will only be served over `HTTPS` instead of `HTTP`.




## References
1. [Segmentfault](https://segmentfault.com/a/1190000011203711)
1. [Zhihu](https://www.zhihu.com/question/31377141)
1. [Namesilo website](https://www.namesilo.com/)




