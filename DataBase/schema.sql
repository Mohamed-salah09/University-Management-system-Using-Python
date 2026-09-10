
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date_birth TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);


 
CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE,
    description TEXT
);


 
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    level INTEGER NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
);



CREATE TABLE IF NOT EXISTS Professors (
    professor_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    specialization TEXT,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
);


 
CREATE TABLE IF NOT EXISTS Admins (
    admin_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
);


 
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_code TEXT NOT NULL UNIQUE,
    credits INTEGER NOT NULL,
    description TEXT,

    department_id INTEGER NOT NULL,
    professor_id INTEGER,

    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id),

    FOREIGN KEY (professor_id)
        REFERENCES Professors(professor_id)
);


 
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY,

    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,

    semester TEXT NOT NULL,
    grade REAL,
    status TEXT NOT NULL DEFAULT 'ACTIVE',

    FOREIGN KEY (student_id)
        REFERENCES Students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES Courses(course_id),

    UNIQUE (student_id, course_id, semester)
);