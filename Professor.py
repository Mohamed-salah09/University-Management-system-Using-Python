from User import User
class Professor(User):

    def __init__(self, user_id, name, date_birth, email, password,
                 professor_id, department, specialization, system):

        super().__init__(user_id, name, date_birth, email, password)

        self.professor_id = professor_id
        self.department = department
        self.specialization = specialization
        self.system = system

    def view_students(self):

        students = []

        for enrollment in self.system.enrollments:

            if enrollment.course.professor == self:

                if enrollment.student not in students:
                    students.append(enrollment.student)

        return students

    def view_courses(self):

        courses = []

        for course in self.system.courses:

            if course.professor == self:
                courses.append(course)

        return courses

    def add_grade(self, enrollment, grade):
        from DataBase.Enrollment_db import update_grade

        enrollment.grade = grade
        update_grade(enrollment.enrollment_id, grade)

    def update_grade(self, enrollment, new_grade):
        from DataBase.Enrollment_db import update_grade

        enrollment.grade = new_grade
        update_grade(enrollment.enrollment_id, new_grade)