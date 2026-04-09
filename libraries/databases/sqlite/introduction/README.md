# Introduction to SQLite 

SQLite is a software package that provides a **relational database management 
system (RDBMS)**. 

> Relational database systems are used to store user-defined records in large 
> tables. In addition to data storage and management, a database engine can
> process complex **query commands** that combine data from multiple tables 
> to generate reports and data summaries.

SQLite is defined by the following features: 

* **Serverless**: SQLite does not require a separate server process or system to operate. 
    The SQLite library accesses its storage files directly. 
    
* **Zero Configuration**: No server means no setup. 
    Creating an SQLite database instance is as easy as opening a file. 
    
* **Cross-Platform**: The entire database instance resides in a single cross-platform file, 
    requiring no administration. 
    
* **Self-Contained**: A single library contains the entire database system, which integrates 
    directly into a host application.

* **Small Runtime Footprint**: The default build is less than a megabyte of code and requires only 
    a few megabytes of memory. With some adjustments, both the library size and memory use can be 
    significantly reduced. 
    
* **Transactional**: SQLite transactions are fully ACID-compliant, allowing safe access from 
    multiple processes or threads. 
    
* **Full-Featured**: SQLite supports most of the query language features found in the **SQL92 standard**. 

## Setup 

Install the SQLite command-line program with:

```bash
$ sudo apt install sqlite3

$ sqlite3 --version
```

Note that in the Debian VM, SQLite3 is already installed.

## Command Line Interface

To start SQLite from the command line:

```bash
$ sqlite3 testdb.db
sqlite> 
```

If we run `sqlite3` with **no filename**, SQLite opens a temporary in-memory 
database. 

If we give a **filename**, it opens that database, and creates it if it does 
not already exist.


## Common SQLite Commands

The following special SQLite commands are available in the command-line 
interface:

* `.quit`: Exit the SQLite command-line interface.

* `.tables`: Display all tables in the current database.

* `.schema`: Show the SQL CREATE statements for all tables.

* `.headers on`: Enable column headers in query results.

* `.mode column`: Format output as aligned columns for better readability.


We can also run one command directly from Bash without entering the interactive shell:

```bash
$ sqlite3 test.db "SELECT sqlite_version();"

# List tables
$ sqlite3 mydb.db ".tables"    

# Show schema
$ sqlite3 mydb.db ".schema"    
```


## Tutorials

* [YouTube (Corey Schafer): Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries](https://youtu.be/pd-0G0MigUA)


## References

* [SQLite: Tutorial](https://www.sqlitetutorial.net/)
* [SQLite:In-Memory Databases](https://www.sqlite.org/inmemorydb.html)

* Jay A. Kreibich. **Using SQLite: Small. Fast. Reliable. Choose Any Three.** O'Reilly Media, 2010. 

*Egon Teiniker, 2020-2026, GPL v3.0*