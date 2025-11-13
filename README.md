# Overview

The software developed is a Recipes Database Management System written in Python. The program allows users to add, view, edit, and delete recipes, while storing all data in a SQL Relational Database(SQLite). It integrated Python with SQLite using the splite3 library, demonstrating CRUD(create, read, update, and delete) operations and relational database management.

Users interact with the program via a menu-driven command-line interface. The program provides options to view all recipes, see detailed instructions, add new recipes, edit existing recipes, delete recipes, and view recipes along with their categories. The relational database stores recipe information in a recipes table and links recipes to a categories table via foreign key, enabling queries that combine information from multiple tables.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The project uses SQLite, a lightweight, embedded relational database stored in a single file. 

### Table structure
- recipes table: 
1. id - unique recipe ID
2. name - recipe name
3. ingredients - ingredients for the recipe
4. instructions - cooking instructions


# Development Environment

Tools Used:
- Python 3.13+ - The main programming language used to develop the recipe database software.
- SQLite3 - A lightweight, file-based database system used to store and manage rercipe data. 
- Visual Studio Code - Used as the code editor for writing and debugging Python scripts.

Proggramming Language and Libraries:
- Python - Chosen for its simplicity, readability, and strong support for database operations.
- sqlite3  (Python standard library) - Provides functions to create, read, and delete data from the SQLite database.

Note:
- The software is cross platform and can run on Windows, macOS, or Linux without additional database installation, because SQLite is embedded.
- Python scripts handle database creation, data insertion, updates, deletions, and queries.

# Useful Websites

- [TutorialsPoint](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
- [Python SQLite](https://www.geeksforgeeks.org/python/python-sqlite/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Add search functionality by name or ingredient
- Add user authentication for personal recipe collections
- Expand the database with additional tables such as 'Categories' or 'Rating'