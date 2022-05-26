# Anaconda Basics

## Manage `conda`

```bash
conda --version

# update
conda update conda

# check if auto activate is true
conda config --show | grep auto_activate_base

# set it to false
conda config --set auto_activate_base False

# get help
conda --help

# list all packages
conda list

# install
conda install
```

- We can use `conda` to install non-python packages and dependencies

## Virtual Environments

```bash
# create a new environment
conda create --name my_app flask sqlalchemy
# specify Python version
conda create --name my_app python=2.7 flask sqlalchemy

# activate environment
source activate my_app

# check python
which python

# deactivate
source deactivate

# show all created virtual environments
conda env list

# remove an environment
conda remove --name my_app all
```
