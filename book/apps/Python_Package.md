# Python Package 


setup.py poetry github-action sphnix  || Buy and Bind Domain Name with Github Pages


## poetry

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

