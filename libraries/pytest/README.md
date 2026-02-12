# PyTest 

PyTest is currently the industry standard for Python testing, widely preferred over the built-in `unittest` 
module due to its simplicity, scalability, and powerful ecosystem.

When we run the `pytest` command, it performs the following steps:

* **Collection**: It searches your current directory and subdirectories for files starting with 
    `test_` or ending with `_test.py`.

* **Setup**: It initializes any necessary fixtures.

* **Execution**: It runs your test functions.

* **Teardown**: It cleans up fixtures.

* **Reporting**: It outputs a summary of passed, failed, and skipped tests.


## Setup 

```bash 
$ pip install pytest 

$ pytest --version
```



## References

* [YouTube: Pytest Tutorial - How to Test Python Code](https://youtu.be/cHYq1MRoyI0?si=HkkHzKJwXz1GQiyO)

* [pytest](https://docs.pytest.org/en/stable/)

*Egon Teiniker, 2020-2026, GPL v3.0*