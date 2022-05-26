# `conda`

Conda is an open source package management system and environment management system.

It quickly installs, runs, and updates packages and their dependencies.

Conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

## commands

- Some useful commands:

```bash
conda --help

# create environment
conda create

# install package
conda install $PACKAGE_NAME

# update package
conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME

# update package manager
conda update conda

# uninstall a package
conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME

# search available packages
conda search $SEARCH_TERM

# list installed packages
conda list --name $ENVIRONMENT_NAME

# Create requirements file
conda list --export

# list all environments
conda info --envs

# activate
conda activate $ENVIRONMENT_NAME

# deactivate
conda deactivate
```

## packages

- A conda package is a compressed tarball file or `.conda` file that contains:
  - system-level libraries
  - Python or other modules
  - executable programs and other components
  - metadata under the `info/` directory
  - a collection of files that are installed directly into an `install` prefix
- Using packages:
  - search for a package: `conda search`
  - install a package: `conda install`
  - build a package: `conda build`
