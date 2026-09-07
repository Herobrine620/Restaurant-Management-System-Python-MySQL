# RESTAURANT MANAGEMENT SYSTEM

### Class XII – Computer Science Project

### CBSE Board

### Kamal Model Sr. Sec. School

---

## 1. Project Overview

The **Restaurant Management System** is a Python-based project developed as a part of the **Class 12 Computer Science curriculum under the CBSE Board**.

The project is designed to manage basic restaurant operations such as viewing the menu, placing orders, checking orders, cancelling orders, managing menu items, and collecting customer feedback.

The project uses **Python programming language** for the main application and **MySQL** for storing and managing data.

---

## 2. Objectives of the Project

The main objectives of this project are:

* To understand the practical implementation of **Python programming**.
* To learn how Python can be connected with a **MySQL database**.
* To store and retrieve restaurant-related information efficiently.
* To provide separate options for the **Owner and Customer**.
* To reduce manual work involved in managing restaurant orders.
* To apply concepts such as **functions, conditional statements, loops, SQL queries, and database connectivity**.

---

## 3. Main Features

### Owner Module

The owner can:

* Add new dishes to the menu.
* Update the price of an existing dish.
* View the complete restaurant menu.
* View customer orders.
* View customer feedback.
* Access the owner section using a password.

### Customer Module

The customer can:

* View the available menu.
* Place an order.
* Enter customer details.
* View previous/recent orders.
* Cancel an order.
* Submit feedback.
* Exit the system.

---

## 4. Technologies Used

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| **Python**                 | Development of the main program |
| **MySQL**                  | Storage and management of data  |
| **mysql.connector**        | Connecting Python with MySQL    |
| **Command Line Interface** | Interaction with the user       |

---

## 5. Database

The project uses a MySQL database named:

```text
Restaurant
```

The main tables used in the project are:

### `menu`

Stores information about restaurant dishes.

* Dish ID
* Item Name
* Price
* Item Type

### `cusdet`

Stores customer order details.

* Dish ID
* Quantity
* Customer Name
* Mobile Number
* Address
* Total Price

### `feedback`

Stores customer feedback.

* Customer Name
* Feedback

---

## 6. Program Flow

```text
                    START
                      |
                      ↓
                WELCOME PAGE
                      |
          ┌───────────┼───────────┐
          ↓           ↓           ↓
        OWNER      CUSTOMER      EXIT
          |           |
          ↓           ↓
    Owner Menu    Customer Menu
          |           |
    ┌─────┼─────┐   ┌─┼───────────────┐
    ↓     ↓     ↓   ↓ ↓ ↓ ↓ ↓
  Menu  Orders Feedback View Book Cancel Feedback
          |           |
          └─────┬─────┘
                ↓
           MySQL DATABASE
                |
                ↓
               EXIT
```

---

## 7. Python Concepts Used

The project demonstrates several important Class 12 Computer Science concepts:

* Variables and data types
* Input and output
* `if-elif-else` statements
* `while` loops
* User-defined functions
* MySQL database connectivity
* SQL `SELECT` statements
* SQL `INSERT` statements
* SQL `UPDATE` statements
* SQL `DELETE` statements
* Fetching records using `fetchall()`
* Database transactions using `commit()`

---

## 8. How to Run the Project

### Step 1 – Install Python

Install Python on the computer.

### Step 2 – Install MySQL Connector

Open Command Prompt and run:

```bash
pip install mysql-connector-python
```

### Step 3 – Create Database

Create a MySQL database named:

```sql
CREATE DATABASE Restaurant;
```

Create the required tables according to the project structure.

### Step 4 – Configure Database Connection

The Python program contains the MySQL connection details:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="Restaurant"
)
```

Change the password according to the MySQL setup on your computer.

### Step 5 – Run the Program

Save the Python file and execute:

```bash
python restaurant.py
```

---

## 9. Advantages

* Simple and easy-to-use interface.
* Reduces manual record keeping.
* Stores information in a database.
* Allows separate Owner and Customer operations.
* Demonstrates practical use of Python and MySQL.
* Suitable for managing basic restaurant operations.

---

## 10. Limitations

* The current project uses a command-line interface.
* It is designed for basic restaurant management.
* Payment processing is not included.
* Multiple-item orders are not handled in a single transaction.
* The system does not include an online ordering facility.

---

## 11. Future Scope

The project can be improved in the future by adding:

* Graphical User Interface (GUI)
* Online food ordering
* Digital payment options
* Order tracking
* Multiple-item cart system
* Automatic bill generation
* Admin login system
* Better database security
* Online customer accounts

---

## 12. Conclusion

The **Restaurant Management System** successfully demonstrates the practical application of **Python and MySQL** in solving a real-world problem.

Through this project, concepts of programming, functions, decision-making, loops, SQL commands, and database connectivity can be understood and applied practically.

This project was developed as a **Class 12 Computer Science project under the CBSE Board** at **Kamal Model Sr. Sec. School**.

---

## 13. Project Information

**Project Title:** Restaurant Management System
**Subject:** Computer Science
**Class:** XII
**Board:** CBSE
**School:** Kamal Model Sr. Sec. School
**Programming Language:** Python
**Database:** MySQL

---

### Acknowledgement

I would like to express my sincere gratitude to my Computer Science teacher and **Kamal Model Sr. Sec. School** for providing me with the opportunity to develop this project. This project helped me understand the practical applications of Python programming and MySQL database management.

I also thank my teachers, classmates, and everyone who provided guidance and support during the development of this project.
