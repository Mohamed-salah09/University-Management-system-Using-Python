from Studentmanagementsystem import StudentManagementSystem
from Student import Student
from Professor import Professor
from Course import Course
from Department import Department
from Admin import Admin


system = StudentManagementSystem()

admin = Admin(
    1,
    "Admin",
    "1980-01-01",
    "admin@test.com",
    "1234",
    system
)


# =========================
# Test Department
# =========================

department = Department(
    1,
    "Computer Science",
    "CS Department",
    system
)

admin.add_department(department)

print("Departments:", len(system.departments))


# =========================
# Test Student
# =========================

student = Student(
    1,
    "Mohamed",
    "2005-01-01",
    "mohamed@test.com",
    "1234",
    1001,
    3,
    department,
    system
)

admin.add_student(student)

print("Students:", len(system.students))


# =========================
# Test Professor
# =========================

professor = Professor(
    2,
    "Dr Ahmed",
    "1980-01-01",
    "ahmed@test.com",
    "1234",
    2001,
    department,
    "Software Engineering",
    system
)

admin.add_professor(professor)

print("Professors:", len(system.professors))


# =========================
# Test Course
# =========================

course = Course(
    1,
    "Software Engineering",
    "CS301",
    3,
    "Software Engineering Course",
    department
)

admin.add_course(course)

print("Courses:", len(system.courses))


# =========================
# Test Remove
# =========================

print("\nRemoving student...")

result = admin.remove_student(1001)

print("Remove result:", result)
print("Students:", len(system.students))


print("\nRemoving professor...")

result = admin.remove_professor(2001)

print("Remove result:", result)
print("Professors:", len(system.professors))


print("\nRemoving course...")

result = admin.remove_course(1)

print("Remove result:", result)
print("Courses:", len(system.courses))


print("\nRemoving department...")

result = admin.remove_department(1)

print("Remove result:", result)
print("Departments:", len(system.departments))