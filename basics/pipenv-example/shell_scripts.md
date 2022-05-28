# Set Up

## Installing Pipenv

```bash
pip install --user pipenv
```

## Installing packages for your project

```bash
$ cd project_folder
$ pipenv install requests

flaviaouyang@MacBook-Pro example % pipenv install requests
Installing requests...
Adding requests to Pipfile's [packages]...
✔ Installation Succeeded
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success!
Updated Pipfile.lock (a290a1)!
Installing dependencies from Pipfile.lock (a290a1)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

## Run

```bash
flaviaouyang@MacBook-Pro example % pipenv run python main.py
Your IP is 184.160.34.213
```

- Using `pipenv run` ensures that your installed packages are available to your script.
- It’s also possible to spawn a new shell that ensures all commands have access to your installed packages with `pipenv shell`.
