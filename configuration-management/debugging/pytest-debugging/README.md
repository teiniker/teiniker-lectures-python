# Debugging PyTest Tests  

Typically, `pytest` tests are run from the command line. However, if we want 
to debug individual test functions or entire test classes directly in the IDE, 
we need to add an appropriate configuration to the `launch.json` file. 

```json
    "configurations": [
        {
            "name": "Debug Pytest (Active Folder)",
            "type": "debugpy",
            "request": "launch",
            "module": "pytest",
            "args": [
                "${fileDirname}"
            ],
            "console": "integratedTerminal"
        }
    ]
```

This allows us to start the debugger with the desired test target and inspect 
the test execution step by step.

* `"name": "Debug Pytest (Active Folder)"`

    This is the label shown in the VS Code Run and Debug menu. It is the name 
    we select when we want to start this debug configuration.

* `"type": "debugpy"`

    This specifies the debugger backend. `debugpy` is the Python debugger used 
    by VS Code for Python applications.

* `"request": "launch"`

    This means VS Code should start a new debugging session by launching 
    a process, rather than attaching to an already running one.

* `"module": "pytest"`

    Instead of running a Python script directly, VS Code runs Python with 
    the pytest module.
    In effect, this is similar to executing:

    ```bash
    $ python -m pytest
    ```

* `"args": [ "${fileDirname}" ]`

    These are the command-line arguments passed to pytest.
    `${fileDirname}` is a VS Code variable that resolves to the directory 
    of the currently open file.

* `"console": "integratedTerminal"`

    This tells VS Code to run the command in the built-in terminal inside 
    the editor.
    That way, we can see the normal `pytest` output, interact with the 
    process if needed, and view any print statements or input prompts there.



*Egon Teiniker, 2020-2026, GPL v3.0*