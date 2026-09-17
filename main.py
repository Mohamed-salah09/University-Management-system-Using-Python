from Studentmanagementsystem import StudentManagementSystem
from User import User
from Student import Student
from Professor import Professor
from Admin import Admin
from Course import Course
from Department import Department
from DataBase.Admin_db import add_admin


def main():

    print("========== START TEST ==========\n")

    # ==========================================
    # 1. Create System
    # ==========================================

    system = StudentManagementSystem()

    print("System created successfully.\n")


    # ==========================================
    # 2. Create Department
    # ==========================================

    department = Department(
        1,
        "Computer Science",
        "Computer Science Department",
        system
    )

    admin = Admin(
        1,
        "Admin",
        "1990-01-01",
        "admin@gmail.com",
        "1234",3008,
        system
    )

    admin.add_department(department)

    print("Department added.")


    # ==========================================
    # 3. Add Admin to Database
    # ==========================================

    from DataBase.User_db import add_user

    add_user(admin)
    add_admin(admin)

    print("Admin added to database.")


    # ==========================================
    # 4. Create Student
    # ==========================================

    student = Student(
        2,
        "Mohamed Salah",
        "2005-01-01",
        "mohamed@gmail.com",
        "1234",
        1001,
        3,
        department,
        system
    )

    add_user(student)
    admin.add_student(student)

    print("Student added.")


    # ==========================================
    # 5. Create Professor
    # ==========================================

    professor = Professor(
        3,
        "Dr. Ahmed",
        "1980-01-01",
        "ahmed@gmail.com",
        "1234",
        2001,
        department,
        "Software Engineering",
        system
    )

    add_user(professor)
    admin.add_professor(professor)

    print("Professor added.")


    # ==========================================
    # 6. Create Course
    # ==========================================

    course = Course(
        101,
        "Software Engineering",
        "SWE101",
        3,
        "Introduction to Software Engineering",
        department
    )

    admin.add_course(course)

    print("Course added.")


    # ==========================================
    # 7. Assign Professor to Course
    # ==========================================

    course.assign_professor(professor)

    print("Professor assigned to course.")


    # ==========================================
    # 8. Student Enrolls in Course
    # ==========================================

    student.enroll_course(
        5001,
        course,
        "Fall 2026"
    )

    print("Student enrolled in course.")


    # ==========================================
    # 9. View Student Courses
    # ==========================================

    print("\nStudent Courses:")

    for c in student.view_courses():
        print(c.course_name)


    # ==========================================
    # 10. Professor Views Students
    # ==========================================

    print("\nProfessor Students:")

    for s in professor.view_students():
        print(s.name)


    # ==========================================
    # 11. Professor Adds Grade
    # ==========================================

    enrollment = system.enrollments[0]

    professor.add_grade(enrollment, "A")

    print("\nGrade added:", enrollment.grade)


    # ==========================================
    # 12. Student Views Grades
    # ==========================================

    print("Student Grades:")

    for grade in student.view_grades():
        print(grade)


    # ==========================================
    # 13. Calculate GPA
    # ==========================================

    print("\nStudent GPA:", student.calculate_GPA())


    # ==========================================
    # 14. Student Drops Course
    # ==========================================

    student.drop_course(course)

    print("\nCourse dropped.")

    print("Enrollment status:", enrollment.status.value)


    # ==========================================
    # 15. Test Login
    # ==========================================

    print("\nLogin Test:")

    student.login()

    print("\nWrong Login Test:")

    wrong_student = User(
        999,
        "Test",
        "2000-01-01",
        "wrong@gmail.com",
        "wrong"
    )

    wrong_student.login()


    # ==========================================
    # 16. Database Users Test
    # ==========================================

    from DataBase.User_db import get_all_users

    users = get_all_users()

    print("\nUsers in Database:")

    for user in users:
        print(user.user_id, user.name, user.email)


    print("\n========== TEST FINISHED ==========")


if __name__ == "__main__":
    main()