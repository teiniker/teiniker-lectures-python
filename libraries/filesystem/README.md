# File Handling

One of the most common tasks that you can do with Python is reading and writing files. 

Whether it’s writing to a simple text file, reading a complicated server log, or even 
analyzing raw byte data, all of these situations require reading or writing a file.

* [Text Files](text-files/)

* [Binary Files](binary-files/)

* [CSV Files](csv-files/)

* [JSON Files](json-files/)


## VS Code Path Setting 

When executing a Python script with Code Runner, the file's directory should 
be set as the working directory.

To enable this setting, add the following configuration to the `settings.json` 
file:

```json
  //...
  "code-runner.fileDirectoryAsCwd": true,
  //...
```

We may need to restart VS Code for the changes to take effect.


## Tutorials 

* [YouTube (Corey Schafer): Context Managers - Efficiently Managing Resources](https://youtu.be/-aKFBoZpiqA)
* [YouTube (Corey Schafer): File Objects - Reading and Writing to Files](https://youtu.be/Uh2ebFW8OYM)
* [YouTube (Corey Schafer): CSV Module - How to Read, Parse, and Write CSV Files](https://youtu.be/q5uM4VKywbA)

*Egon Teiniker, 2020-2026, GPL v3.0*

