# Pandas

Python Pandas is a widely used open-source data manipulation and analysis library. It provides powerful data structures and data analysis tools for efficiently working with structured data. 

Pandas offers a wide range of functionality, including **data manipulation, cleaning, filtering, reshaping, merging, grouping, and aggregating data**. 
It provides flexible indexing and slicing capabilities, making it convenient to access and modify data. Additionally, pandas supports reading and writing data in various formats such as CSV, Excel, SQL databases, and more.

Pandas is built on top of the **NumPy** library and provides two primary data structures: 

* A **Series** is a one-dimensional labeled array capable of holding any data type. It is similar to a column in a spreadsheet or a traditional database table. Each value in a Series is associated with a unique label or index.

* A **DataFrame** is a two-dimensional table of data with rows and columns. It is similar to a spreadsheet or a SQL table. A DataFrame can be thought of as a collection of Series objects, where each Series represents a column of the DataFrame.

## Setup Pandas

Pandas can be installed via pip from PyPI:

```
$ pip3 install pandas
$ pip3 install openpyxl
```
The `openpyxl` package is only needed if we want to handle Excel files as well.

To load the pandas package and start working with it, **import the package**. 
The community agreed alias for pandas is `pd`:

```Python
import pandas as pd
```

## Data Series

A Pandas Series is a **one-dimensional labeled data structure**. 

It is designed to handle data in a vectorized manner, similar to a NumPy array, but with additional functionalities and labeled indexing capabilities.

A Pandas Series can hold a sequence of values, such as integers, floats, strings, or even complex objects. 
It consists of two main components: the **data** itself and an **associated index**. 
The index provides a label or name for each element in the Series, which allows for easy and efficient access to the data.

You can think of a Pandas Series as a column in a spreadsheet or a single column of data in a table. 
It has a similar structure to a Python dictionary or an array, but with additional functionality and performance optimizations specifically designed for data analysis and manipulation tasks.

_Example:_ Create a Series from a list of values

```Python
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

0    10
1    20
2    30
3    40
4    50
dtype: int64
```
The Series is displayed with its index on the left and the corresponding values on the right. 
By default, Pandas assigns a numeric index starting from 0, but we can also specify our own custom 
index.

The Pandas `Series` data structure provides various methods and operations for data manipulation, filtering, aggregation, and analysis. 
It is a fundamental building block for working with tabular data in Pandas, as it serves as the foundation 
for creating more complex data structures like `DataFrames`.


## Data Frame
A Pandas `DataFrame` is a **two-dimensional labeled data structure**. 

It is a highly versatile and powerful data structure that represents data in a tabular format, 
similar to a spreadsheet or a SQL table.

A Pandas `DataFrame` consists of rows and columns, where each column can hold different data types 
(e.g., numeric, string, boolean) and each row represents a unique observation or record. 
It can be thought of as a collection of Pandas `Series` objects, where each Series represents a column of data.

The DataFrame provides a comprehensive set of functionalities and operations for data manipulation, cleaning, exploration, analysis, and visualization. It allows for efficient indexing, filtering, joining, grouping, reshaping, and aggregation of data.

_Example:_ Create a DataFrame from a dictionary

```Python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)

      Name  Age      City
0    Alice   25  New York
1      Bob   30     Paris
2  Charlie   35    London
3    David   40     Tokyo
```

Each key in the dictionary represents a column name, and the corresponding values form the data for each column. 
By default, Pandas assigns a numeric index starting from 0 for the rows, but you can also specify your own custom index if desired.



## Comma Separated Values (CSV) Files 

import pandas as pd

df = pd.read_csv("file.csv")

df.head(number_of_lines)
df.tail(number_of_lines)


## Tab Separated File

df = pd.read_csv("file.txt", delimiter='\t')



## Excel Files 

df = pd.read_excel("file.xlsx")


## References
* [YouTube (Keith Galli): Complete Python Pandas Data Science Tutorial!](https://youtu.be/vmEHCJofslg)

* [Pandas: User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

* YouTube (Corey Schafer): [Python Pandas Tutorials](https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&si=_O8qdsRy8o261vXV)
    * [Getting Started with Data Analysis - Installation and Loading Data](https://youtu.be/ZyhVh-qRZPA)
    * [DataFrame and Series Basics - Selecting Rows and Columns](https://youtu.be/zmdjNSmRXF4)

*Egon Teiniker, 2020-2025, GPL v3.0*


