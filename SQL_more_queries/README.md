# <a  href="https://www.mysql.com/"> <img src="https://d1.awsstatic.com/asset-repository/products/amazon-rds/1024px-MySQL.ff87215b43fd7292af172e2a5d9b844217262571.png" alt="MySQL" width=18%></img></a> **SQL - More Queries**


This project is part of the **Full Stack Software Engineering** program at Holberton School. In this module, we will learn about **advanced SQL queries, user management, and permissions in MySQL, primary and foreign keys, constraints, and queries with multiple tables**.

---

## 📌 Project Goals

✔️ Create and manage **users in MySQL**.  
✔️ Manage **permissions** in databases and tables.  
✔️ Understand the use of **PRIMARY KEY and FOREIGN KEY**.  
✔️ Apply **constraints** like NOT NULL and UNIQUE.  
✔️ Retrieve data from **multiple tables in one query**.  
✔️ Understand and use **subqueries**.  
✔️ Use **JOIN and UNION** to combine data from multiple tables.  

---

## 🛠 Install and Setup MySQL

### 💎 **Ubuntu**  
```bash
sudo apt update
sudo apt install mysql-server -y
sudo service mysql start
```
### 💎 **MacOS (Homebrew)**  
```bash
brew install mysql
brew services start mysql
```
### 💎 **Check Installation**  
```bash
mysql --version
```

🔗 **[Help Video](https://www.mysql.com/downloads/)**

---

## 🏆 Essential SQL Commands

| Command | Description | Example |
|---------|------------|---------|
| `CREATE USER` | Create a new user in MySQL | `CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';` |
| `GRANT` | Give permissions to a user | `GRANT SELECT ON database.* TO 'user'@'localhost';` |
| `SHOW GRANTS` | Show permissions of a user | `SHOW GRANTS FOR 'user'@'localhost';` |
| `REVOKE` | Remove permissions from a user | `REVOKE INSERT ON database.* FROM 'user'@'localhost';` |
| `CREATE TABLE` | Create a table | `CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));` |
| `ALTER TABLE` | Modify an existing table | `ALTER TABLE users ADD COLUMN age INT;` |
| `DROP TABLE` | Delete a table | `DROP TABLE users;` |
| `INSERT INTO` | Add data to a table | `INSERT INTO users (id, name) VALUES (1, 'John');` |
| `UPDATE` | Change data in a table | `UPDATE users SET name = 'Jane' WHERE id = 1;` |
| `DELETE FROM` | Remove data from a table | `DELETE FROM users WHERE id = 1;` |
| `JOIN` | Combine data from multiple tables | `SELECT users.name, orders.amount FROM users JOIN orders ON users.id = orders.user_id;` |
| `SUBQUERY` | Query inside another query | `SELECT name FROM users WHERE id = (SELECT MAX(id) FROM users);` |
| `UNION` | Combine results of multiple queries | `SELECT name FROM users UNION SELECT name FROM employees;` |

✚ **More commands:  [MySQL Cheat Sheet](https://devhints.io/mysql).**

---

## 🔍 SQL Joins Cheat Sheet

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Nrjozs1i0XIiACKd.png" alt="SQL Joins Cheatsheet">
</p>


| JOIN Type        | Description |
|-----------------|-------------|
| **INNER JOIN** | Returns only the records with matches in both tables. |
| **LEFT JOIN** | Returns all records from the left table and the matched records from the right table. |
| **RIGHT JOIN** | Returns all records from the right table and the matched records from the left table. |
| **FULL OUTER JOIN** | Returns all records when there is a match in either the left or right table. |
| **LEFT JOIN with NULL filter** | Returns only records from the left table that have no match in the right table. |
| **RIGHT JOIN with NULL filter** | Returns only records from the right table that have no match in the left table. |
| **CROSS JOIN** | Returns the Cartesian product of both tables (all possible combinations). |



---

## 💪 How to Run the Scripts

To run any script in MySQL, use this command:

```bash
cat script_name.sql | mysql -uroot -p
```

Example:
```bash
cat 0-privileges.sql | mysql -uroot -p
```

---

## 🔗 Additional Resources

- [Create and manage users in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)  
- [SQL JOIN types](https://www.w3schools.com/sql/sql_join.asp)  
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)  
- [MySQL Cheat Sheet](https://devhints.io/mysql)  

---

## ❓ General Questions

✔️ **How to create a new user in MySQL?**  
```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

✔️ **How to give permissions to a user?**  
```sql
GRANT SELECT, INSERT ON database.* TO 'new_user'@'localhost';
```

✔️ **What is a PRIMARY KEY?**  
It is a unique identifier for each record in a table.
```sql
CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));
```

✔️ **What is a FOREIGN KEY?**  
It is a key that creates a relationship between two tables.
```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

✔️ **How to use JOIN to combine data from multiple tables?**  
```sql
SELECT users.name, orders.amount
FROM users
JOIN orders ON users.id = orders.user_id;
```

✔️ **What is a subquery?**  
It is a query inside another query.
```sql
SELECT name FROM users WHERE id = (SELECT MAX(id) FROM users);
```

✔️ **What is the difference between JOIN and UNION?**  
- **JOIN** combines rows based on a relationship between tables.
- **UNION** merges results from multiple queries without table relationships.

✔️ **How to delete a user in MySQL?**  
```sql
DROP USER 'new_user'@'localhost';
```

---

## ✍️ Author

👩‍💻 **[Nazarena Aranda](https://github.com/nazarena-aranda)**  
