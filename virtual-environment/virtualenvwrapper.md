# `virtualenvwrapper`

`virtualenvwrapper` provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place.

## Quick Start

1. Run `workon`: A list of environments, empty, is printed.
2. Run `mkvirtualenv temp`: A new environment, temp is created and activated.
3. Run `workon`: This time, the temp environment is included.

## Basic Usage

- create a virtual environment: `mkvirtualenv project_folder`
- Work on a virtual environment: `workon project_folder`
- `workon` also deactivates whatever environment you are currently in, so you can quickly switch between environments.
- deactivate is the same
- delete: `rmvirtualenv venv`

## Useful Commands

- `lsvirtualenv`: List all of the environments.
- `cdvirtualenv`: Navigate into the directory of the currently activated virtual environment, so you can browse its site-packages, for example.
- `cdsitepackages`: Like the above, but directly into site-packages directory.
- `lssitepackages`: Shows contents of site-packages directory.
