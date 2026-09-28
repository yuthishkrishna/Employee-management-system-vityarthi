# Employee Management System

## 1. Problem Statement

Managing employee information manually can become difficult and time-consuming as the number of employees increases. Maintaining employee names, ages, departments, salaries, employee IDs, genders, and dates of joining through paper records or manually edited files can lead to duplication, incorrect information, difficulty in searching records, and inefficient data management.

The **Employee Management System** is a Python-based, menu-driven application developed to provide a structured solution for managing employee information. The system allows users to add, display, update, delete, search, sort, and analyze employee records. Employee information is stored in a CSV file named `Employee_Records.csv`, allowing the data to remain available even after the program is closed. The application uses Python and Pandas for data processing and file management. The implemented system maintains employee records using an in-memory data structure and saves them to the CSV file when required. 

The main purpose of the project is to simplify employee record management and provide users with a convenient way to perform common employee-related operations through a simple console interface.

---

## 2. Objectives

The major objectives of the Employee Management System are:

- To provide a simple system for maintaining employee records.
- To reduce the effort required to manage employee information manually.
- To provide CRUD operations such as adding, viewing, updating, and deleting records.
- To allow users to search employees by name or department.
- To allow employee records to be sorted according to different attributes.
- To provide basic analysis such as finding employees with minimum or maximum age or salary.
- To provide persistent storage using a CSV file.
- To provide basic input validation and error handling.
- To demonstrate practical implementation of Python, Pandas, data structures, and file handling.

---

## 3. Scope of the Project

The project focuses on basic employee record management for small-scale or educational use.

The system supports the following activities:

- Adding new employee information.
- Automatically generating an employee ID.
- Displaying all employee records.
- Updating employee information.
- Deleting employee records.
- Searching for an employee by name.
- Searching for employees by department.
- Sorting records by age, salary, department, or date of joining.
- Finding employees with minimum or maximum age.
- Finding employees with minimum or maximum salary.
- Clearing all employee records.
- Loading previously saved records when the application starts.
- Saving employee information to `Employee_Records.csv`.

The current project is a local, console-based application. It does not currently provide a web interface, graphical interface, cloud database, or simultaneous multi-user access.

---

## 4. Target Users

The system is intended for:

### Small Organizations
Small organizations can use the system to maintain basic employee records without requiring a complex enterprise management system.

### Administrative Staff
Administrative staff can use the application to add, update, search, display, and delete employee information.

### HR Personnel
HR personnel can use the system for maintaining basic employee information and performing simple employee-data analysis.

### Students and Learners
The project can also be used as an educational application for understanding Python programming, Pandas, file handling, CRUD operations, object-oriented programming, and data processing.

---

## 5. High-Level Features

The major features of the system are:

1. **Employee Registration** – Add employee information and automatically assign an employee ID.
2. **Employee Display** – View stored employee records in a structured tabular format.
3. **Employee Update** – Modify employee information.
4. **Employee Deletion** – Remove an employee record.
5. **Employee Search** – Search by employee name or department.
6. **Employee Sorting** – Sort records by age, salary, department, or date of joining.
7. **Employee Analysis** – Find minimum and maximum age and salary.
8. **Data Persistence** – Store and retrieve records through a CSV file.
9. **Record Clearing** – Remove all employee records when required.

---

## 6. Functional Requirements

### FR1: Add Employee

The system shall allow the user to enter the employee's name, age, department, salary, date of joining, and gender. A unique employee ID shall be generated automatically.

### FR2: Display Employee Records

The system shall allow the user to display all available employee records in a tabular format.

### FR3: Update Employee

The system shall allow the user to update information belonging to an existing employee.

### FR4: Delete Employee

The system shall allow the user to delete an existing employee record.

### FR5: Search Employee

The system shall allow users to search for employee records using the employee's name or department.

### FR6: Sort Records

The system shall allow employee records to be sorted by age, salary, department, or date of joining.

### FR7: Analyze Records

The system shall allow users to find employees having minimum or maximum age and salary.

### FR8: Clear Records

The system shall provide an option to clear all employee records.

### FR9: Save Records

The system shall save employee information to `Employee_Records.csv`.

### FR10: Load Records

The system shall load previously saved employee information when the application starts.

---

## 7. Non-Functional Requirements

### Performance
The application should perform common employee management operations efficiently for a small to moderate number of records.

### Security
The application should avoid unnecessary exposure of employee data and should provide controlled operations through the application interface.

### Usability
The menu-driven interface should be simple and understandable for users with basic computer knowledge.

### Reliability
Employee information should be preserved by saving modifications to the CSV file.

### Maintainability
The program should use separate methods for different operations so that individual functionality can be modified without redesigning the entire application.

### Error Handling
The system should provide meaningful messages when invalid input is provided, an employee cannot be found, or no records are available.

### Resource Efficiency
The system uses local CSV storage and does not require a separate database server.

### Data Integrity
Employee information and automatically generated IDs should remain associated with the correct employee records during normal operations.

---

## 8. Major Functional Modules

The system can be logically divided into four major modules:

### Module 1: Employee Record Management
Handles adding, displaying, updating, and deleting employee records.

### Module 2: Search and Retrieval
Handles searching for employees by name or department and displaying specific employee information.

### Module 3: Employee Analysis
Handles sorting records and finding minimum or maximum age and salary.

### Module 4: Data Persistence
Handles loading records from the CSV file, saving changes, and clearing stored records.

---

## 9. Input and Output

### Input

The application accepts information through the console. Employee input includes:

- Name
- Age
- Department
- Salary
- Employee ID
- Date of Joining
- Gender

The user also provides menu selections to determine which operation should be performed.

### Output

The system produces:

- Employee records
- Search results
- Sorted employee information
- Minimum and maximum analysis results
- Success messages
- Error messages
- Record-clearing confirmations

---

## 10. Storage Design

The project uses a CSV file named:

`Employee_Records.csv`

The employee record contains:

| Field | Description |
|---|---|
| Name | Employee name |
| Age | Employee age |
| Department | Employee department |
| Salary | Employee salary |
| ID | Unique employee identifier |
| Date of Joining | Employee joining date |
| Gender | Employee gender |

The application loads the CSV data when it starts and converts the information into a Python data structure for processing. Changes are written back to the CSV file so that employee records can be retained between program executions.

---

## 11. Project Workflow

The basic workflow of the system is:

```text
Start
  |
  v
Load Employee Records
  |
  v
Display Main Menu
  |
  v
Select Operation
  |
  +--> Add Employee
  |
  +--> Display Employees
  |
  +--> Update Employee
  |
  +--> Delete Employee
  |
  +--> Search Employee
  |
  +--> Sort Employee Records
  |
  +--> Find Minimum/Maximum
  |
  +--> Clear All Records
  |
  v
Save Changes
  |
  v
Continue?
  |
  +---- Yes ---> Main Menu
  |
  +---- No ----> Exit
