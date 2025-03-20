# Using SQLite in Python 


The **sqlite3** module provides a SQL interface compliant with the **DB-API 2.0** specification 
described by **PEP 249**.

To use the module, you must first create a `Connection` object that represents the database.
We can also supply the special name `:memory:` to create a database in RAM.
```Python
conn = sqlite3.connect(DATABALE_NAME)
```

Once we have a `Connection`, we can create a `Cursor` object and call its `execute()` method 
to perform SQL commands:

```Python
cursor = conn.cursor()
# Create a database table
cursor.execute("CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))")

# Insert data into the database table
cursor.execute("INSERT INTO user (id,username, password) VALUES (1, 'homer' '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')")

# Commit the changes and close the connection
conn.commit()
conn.close()
```

Usually our SQL operations will need to **use values from Python variables**. 
We shouldn’t assemble our query using Python’s string operations because doing so is insecure; it makes your program vulnerable to an **SQL injection attack**.

We put `?` as a **placeholder** wherever we want to use a value, and then 
provide a **tuple of values** as the second argument to the cursor’s `execute()` method. 
```
parameters = ('m%',)
cursor.execute("SELECT * FROM user WHERE username LIKE ?", parameters)
table = cursor.fetchall()
```

To retrieve data after executing a `SELECT statement`, we can either treat the 
cursor as an iterator, call the cursor’s `fetchone()` method to retrieve a single matching row, or call `fetchall()` to get a list of the matching rows.

* **fetchone()**: 
    Fetches the next row of a query result set, returning a **tuple**, or None when no more data is available.

* **fetchall()**:
Fetches all (remaining) rows of a query result, returning a **list of tuples**. Note that the cursor’s arraysize attribute can affect the performance of this operation. An empty list is returned when no rows are available.


## References

* [YouTube (Corey Schafer): Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries](https://youtu.be/pd-0G0MigUA?si=7Kd1-TSwEZsbmrBJ)

* [Youtube: SQLite Databases With Python](https://youtu.be/byHcYRpMgI4)

* [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3.8/library/sqlite3.html)


*Egon Teiniker, 2020-2025, GPL v3.0*
