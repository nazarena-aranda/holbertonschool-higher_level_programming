# <a  href="https://www.mysql.com/"> <img src="https://d1.awsstatic.com/asset-repository/products/amazon-rds/1024px-MySQL.ff87215b43fd7292af172e2a5d9b844217262571.png" alt="MySQL" width=18%></img></a> **SQL - Introduction**


This project is part of the **Full Stack Software Engineering** program at Holberton School. We will learn about **databases, SQL, and MySQL**, including how to **create databases and tables, manipulate data, and perform advanced queries**.

---

## 📌 Project Objectives

✔️ Understand what a database is and how MySQL works.  
✔️ Differentiate **relational databases** from other types of databases.  
✔️ Use **DDL (Data Definition Language)** and **DML (Data Manipulation Language)**.  
✔️ Create, modify, and delete **tables and records** in MySQL.  
✔️ Learn how to use **subqueries and functions in MySQL**.

---

## 🛠 MySQL Installation

### 💎 **Ubuntu**  
```bash
sudo apt update
sudo apt install mysql-server -y
sudo service mysql start
```
### 💎 **MacOS**  
```bash
brew install mysql
brew services start mysql
```
### 💎 **Check Installation**  
```bash
mysql --version
```
🔗 **[Help Video](https://www.youtube.com/watch?v=9h3ctGFTz9w)**  

---

## 🏆 Essential SQL Commands

| Command                                  | Description                   | Example                                                          |
|-----------------------------------------|------------------------------|------------------------------------------------------------------|
| `SHOW DATABASES;`                        | List all databases           | `SHOW DATABASES;`                                                |
| `CREATE DATABASE name;`                  | Create a database            | `CREATE DATABASE hbtn_0c_0;`                                     |
| `DROP DATABASE name;`                    | Delete a database            | `DROP DATABASE hbtn_0c_0;`                                       |
| `USE name;`                              | Select a database            | `USE hbtn_0c_0;`                                                 |
| `CREATE TABLE name (...);`               | Create a table               | `CREATE TABLE first_table (id INT, name VARCHAR(256));`          |
| `INSERT INTO name (...) VALUES (...);`   | Insert data into a table     | `INSERT INTO first_table (id, name) VALUES (89, "Best School");` |
| `SELECT * FROM name;`                    | Show all records             | `SELECT * FROM first_table;`                                     |

✚ **More commands: [MySQL Cheat Sheet](https://devhints.io/mysql).**

---



## 💪 How to Run the Scripts

To run any script in MySQL, use the following command:

```bash
cat script_name.sql | mysql -uroot -p
```

Example:
```bash
cat 0-list_databases.sql | mysql -uroot -p
```

---

## 🔗 Additional Resources

-  [What is Database & SQL?](https://www.youtube.com/watch?v=9h3ctGFTz9w)  
-  [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)  
-  [MySQL Cheat Sheet](https://devhints.io/mysql)  

---

## ❓ General Questions

✔️ **What is a database?**  
A **database** is an organized collection of structured data that can be easily accessed, managed, and updated.

✔️ **What is a relational database?**  
A **relational database** organizes data into tables with rows and columns, allowing relationships between tables using **primary and foreign keys**.

✔️ **What does SQL stand for?**  
SQL stands for **Structured Query Language**, which is used to interact with databases.

✔️ **What is MySQL?**  
MySQL is an **open-source relational database management system (RDBMS)** that uses SQL for querying and managing data.

✔️ **How to create a database in MySQL?**  
Use the `CREATE DATABASE` command:
```sql
CREATE DATABASE database_name;
```

✔️ **What does DDL and DML stand for?**  
- **DDL (Data Definition Language)**: Commands that define database structures, such as `CREATE`, `ALTER`, `DROP`.
- **DML (Data Manipulation Language)**: Commands that manipulate data, such as `INSERT`, `UPDATE`, `DELETE`.

✔️ **How to CREATE or ALTER a table?**  
To create a table:
```sql
CREATE TABLE users (id INT, name VARCHAR(255));
```
To modify an existing table:
```sql
ALTER TABLE users ADD COLUMN age INT;
```

✔️ **How to SELECT data from a table?**  
```sql
SELECT * FROM users;
```

✔️ **How to INSERT, UPDATE or DELETE data?**  
- Insert:
```sql
INSERT INTO users (id, name) VALUES (1, 'John');
```
- Update:
```sql
UPDATE users SET name = 'Jane' WHERE id = 1;
```
- Delete:
```sql
DELETE FROM users WHERE id = 1;
```

✔️ **What are subqueries?**  
A **subquery** is a query inside another query. Example:
```sql
SELECT name FROM users WHERE id = (SELECT MAX(id) FROM users);
```

✔️ **How to use MySQL functions?**  
MySQL functions are built-in commands to perform calculations. Example:
```sql
SELECT COUNT(*) FROM users;
```

---

## ✍️ Author

👩‍💻 **[Nazarena Aranda](https://github.com/nazarena-aranda)**  
