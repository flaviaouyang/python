# Python Virtual Environment

Imagine you run Python 3.6, but your project requires Python 2.7, otherwise the application won't run.

One solution to resolve these circumstances is to create a virtual environment for your project.

Virtualenv creates a self-contained folder which contains all the required executables to use the packages that a Python project would require in its project.

## Purpose

The main purpose of using virtualenv (virtual environment tool) is to resolve the issues of dependencies, versions (of python packages) and indirectly permissions.

## Requirements

- Python and `pip` installed
- install `virtualenv`

```bash
pip install virtualenv
```

## Creating Virtual Environments

- Navigate to directory

```bash
python3 -m venv myenv
```

- This will create a new folder `myenv` with directories and files.

```pseudo-code
├── Include
│ ├── abstract.h
│ ├── accu.h
│ ├── asdl.h
│ ├── ast.h
│ ├── bitset.h
………
├── Lib
│ ├── __future__.py
│ ├── __pycache__
│ ├── _bootlocale.py
│ ├── _collections_abc.py
│ ├── _dummy_thread.py
│ ├── _weakrefset.py
│ ├── abc.py
│ ├── base64.py
│ ├── bisect.py
│ ├── codecs.py
……
├── pip-selfcheck.json
├── Scripts
│ ├── activate
│ ├── activate.bat
│ ├── activate.ps1
│ ├── activate_this.py
│ ├── deactivate.bat
│ ├── easy_install.exe
│ ├── easy_install-3.6.exe
│ ├── pip.exe
│ ├── pip3.6.exe
│ ├── pip3.exe
│ ├── python.exe
│ ├── python36.dll
│ ├── pythonw.exe
│ └── wheel.exe
```

- `Include`: C headers that compile the Python package
- `Scripts`: files that interact with the virtual environment
- `Lib`: contains the Python version copy and site-packages directory where each dependency is installed

## Activate the environment

```bash
.\myenv\Scripts\activate
```

- Once the environment is activated, install project related packages and other dependencies
- Once dine working, deactivate by `deactivate`
