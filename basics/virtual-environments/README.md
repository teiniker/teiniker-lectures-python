# Virtual Environments

A **virtual environment** (`venv`) in Python is an isolated environment 
that allows you to manage dependencies separately for different projects. 
It helps prevent conflicts between project dependencies and ensures that 
each project has the specific libraries and package versions it requires.

* **Dependency Isolation**: Each project can have its own dependencies, 
    avoiding version conflicts.

* **Prevent Global Installation Issues**: Packages installed in one 
    environment won’t affect another.

* **Easier Collaboration**: A `requirements.txt` file can be shared, 
    ensuring that others can recreate the same environment.

* **Safer Experimentation**: You can test libraries without affecting 
    system-wide packages.

Using `venv` is a best practice in Python development. It ensures that 
our projects remain manageable, dependency conflicts are avoided, and 
our Python setup remains clean. 

Whether we are working on a single project or multiple, `venv` is an 
essential tool for Python developers. 🚀


## Creating a Virtual Environment

We can create a virtual environment using the `venv` module (built 
into Python 3.3+):

```bash
$ python3 -m venv venv
```
This will create a directory named `venv`, containing the necessary files 
for an isolated Python environment.

## Activating the Virtual Environment

```bash
$ source venv/bin/activate
```

After activation, we will see `(venv)` at the beginning of your terminal prompt, 
indicating that the virtual environment is active.

Also, in the new environment, the `python` command will point to the Python
interpreter in the virtual environment.

```bash
$ which python
/home/student/sandbox/venv/bin/python

$ python --version
Python 3.11.2

$ pip --version
pip 23.0.1 from /home/student/sandbox/venv/lib/python3.11/site-packages/pip (python 3.11)
```


## Installing Packages in the Virtual Environment

Once activated, we can install packages using `pip`:
```bash
$ pip install package_name
```

## List All Installed Packages 

To list all installed packages in the virtual environment:
```bash
$ pip list
```

## Saving and Recreating Dependencies

To save installed packages into a file:
```bash
$ pip freeze > requirements.txt
```
To recreate the environment in another system:
```bash
$ pip install -r requirements.txt
```

## Deactivating the Virtual Environment

To exit the virtual environment, simply run:
```bash
$ deactivate
```
This will return you to the global Python environment.



## References

* [YouTube (Corey Schafer): VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module](https://youtu.be/Kg1Yvry_Ydk?si=GDD5uxD9AyOJynIc)

*Egon Teiniker, 2020-2025, GPL v3.0*
