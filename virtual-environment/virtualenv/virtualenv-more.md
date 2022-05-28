# Set Up

## Create a virtual environment for a project

```bash
cd project_folder
virtualenv venv
```

- `virtualenv venv` will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages.
- The name of the virtual environment (in this case, it was `venv`) can be anything; omitting the name will place the files in the current directory instead.

- You can also use the Python interpreter of your choice

```bash
virtualenv -p /usr/bin/python2.7 venv
```

## activate the virtual environment

```bash
source venv/bin/activate
```

- The name of the current virtual environment will now appear on the left of the prompt to let you know that it’s active.

```bash
(venv)Your-Computer:project_folder UserName$)
```

- From now on, any package that you install using pip will be placed in the `venv` folder, isolated from the global Python installation.
- If you are done working in the virtual environment for the moment, you can deactivate it:

```bash
deactivate
```

- This puts you back to the system’s default Python interpreter with all its installed libraries.
- To delete a virtual environment, just delete its folder.

## Other

- Running virtualenv with the option --no-site-packages will not include the packages that are installed globally. This can be useful for keeping the package list clean in case it needs to be accessed later.
- In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages.

```bash
pip freeze > requirements.txt
```

- This will create a requirements.txt file, which contains a simple list of all the packages in the current environment, and their respective versions.
- You can see the list of installed packages without the requirements format using `pip list`.
- Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

```bash
pip install -r requirements.txt
```

- This can help ensure consistency across installations, across deployments, and across developers.
