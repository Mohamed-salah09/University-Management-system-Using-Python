# University Management System

A Python-based University Management System built using Object-Oriented Programming (OOP) and SQLite.

The project focuses on designing a simple university management system and connecting the OOP classes with a relational database to store and manage the system's data.

---

## Project Overview

The system represents the main entities of a university such as:

- Users
- Students
- Professors
- Admins
- Courses
- Departments
- Enrollments

The main goal of the project was not only to create the OOP classes, but also to connect these classes with a database so that the data can be stored persistently.

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- SQLite
- SQL
 

---

## OOP Design

The project is divided into several classes, where each class represents a specific entity or responsibility.

### User

The base class for users in the system.

It contains common information such as:

- User ID
- Name
- Date of birth
- Email
- Password

It also provides common operations such as:

- Login
- Logout
- View profile

### Student

`Student` inherits from `User`.

A student has:

- Student ID
- Department
- Level
- System reference

Main operations:

- Enroll in a course
- Drop a course
- View enrolled courses
- View grades
- Calculate GPA

### Professor

`Professor` also inherits from `User`.

A professor has:

- Professor ID
- Department
- Specialization
- System reference

Main operations:

- View courses
- View students
- Add grades
- Update grades

### Admin

`Admin` inherits from `User`.

The admin is responsible for managing the university entities.

Main operations:

- Add / remove students
- Add / remove professors
- Add / remove courses
- Add / remove departments

### Course

Represents a university course.

It contains:

- Course ID
- Course name
- Course code
- Credits
- Description
- Department
- Assigned professor

### Department

Represents a university department.

It contains:

- Department ID
- Department name
- Description

It can also retrieve the courses belonging to the department.

### Enrollment

Represents the relationship between a student and a course.

An enrollment contains:

- Enrollment ID
- Student
- Course
- Semester
- Grade
- Status

The enrollment status can be:

- Active
- Dropped
- Completed

---

## System Manager

The `StudentManagementSystem` class manages the objects during program execution.

It contains collections for:

```text
students
professors
courses
departments
enrollments
