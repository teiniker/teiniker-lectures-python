# Python Style Guide

This document gives coding conventions for the Python code.

Note that many projects have their own coding style guidelines.
In the event of any conflicts, such project-specific guides take precedence for that project.

## Naming Conventions
The naming conventions of Python's library are a bit of a mess,
so we'll never get this completely consistent -- nevertheless, here are the currently
recommended naming standards.

Identifiers used in the standard library must be ASCII compatible as described in the policy section of PEP 3131.

* **Package and Module Names**:
    Modules should have **short, all-lowercase** names. **Underscores can be used** in the module name
    if it improves readability. Python packages should also have short, all-lowercase names,
    although the use of underscores is discouraged.

* **Class Names**:
 	Class names should normally use the **CapWords** convention.

 * **Exception Names**:
    Because exceptions should be classes, the **class naming** convention applies here.
    However, you should use the **suffix "Error"** on your exception names
    (if the exception actually is an error).

 * **Function and Variable Names**:
    Function names should be **lowercase**, with words separated by **underscores** as
    necessary to improve readability.
    Variable names follow the same convention as function names.

 * **Function and Method Arguments**:
    Always use self for the first argument to instance methods.
    Always use cls for the first argument to class methods.

 * **Method Names and Instance Variables**:
    Use the function naming rules: **lowercase** with words separated by **underscores** as
    necessary to improve readability.
    Use one **leading underscore** only for non-public methods and instance variables.
    To avoid name clashes with subclasses, use two leading underscores to invoke Python's
    name mangling rules.

  * **Global Variable Names**:
    The conventions are about the same as those for functions.

  * **Constants**:
    Constants are usually defined on a module level and written in
    **all capital letters with underscores** separating words.\
    _Examples_: MAX_OVERFLOW and TOTAL.


## References
* [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)


*Egon Teiniker, 2020-2025, GPL v3.0*
