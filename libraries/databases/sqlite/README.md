# SQLite 

SQLite is a software package that provides a **relational database management system (RDBMS)**. 
Relational database systems are used to store user-defined records in large tables. 
In addition to data storage and management, a database engine can process complex **query commands** 
that combine data from multiple tables to generate reports and data summaries.

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



## Structured Query Language 

The Structured Query Language (SQL) is the main means of interacting with nearly all modern 
relational database systems. 
SQL provides commands to configure the tables, indexes, and other data structures within the 
database. 
SQL commands are also used to insert, update, and delete data records, as well as query those 
records to look up specific data values.

All interaction with a relational database is done through the SQL language. 
This is true when **interactively typing commands** or when using the **programming API**.


## References
* [SQLite: Tutorial](https://www.sqlitetutorial.net/)
* [SQLite:In-Memory Databases](https://www.sqlite.org/inmemorydb.html)

*Egon Teiniker, 2020-2025, GPL v3.0*