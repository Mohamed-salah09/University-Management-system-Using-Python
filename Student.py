from User import *
from Enrollment import *


class Student(User):

    def __init__(self, user_id, name, date_birth, email, password,
                 student_id, level, department, system):

        super().__init__(user_id, name, date_birth, email, password)

        self.student_id = student_id
        self.level = level
        self.department = department
        self.system = system

    def enroll_course(self, enrollment_id, course, semester):

        enrollment = Enrollment(
            enrollment_id,
            self,
            course,
            semester
        )

        self.system.enrollments.append(enrollment)

    def drop_course(self, course):

        for enrollment in self.system.enrollments:

            if enrollment.student == self and enrollment.course == course:
                enrollment.update_status(EnrollmentStatus.DROPPED)

    def view_grades(self):

        grades = []

        for enrollment in self.system.enrollments:

            if enrollment.student == self:
                grades.append(enrollment.grade)

        return grades

    def view_courses(self):

        courses = []

        for enrollment in self.system.enrollments:

            if enrollment.student == self:
                courses.append(enrollment.course)

        return courses

    def calculate_GPA(self):

        grade_points = {
            "A": 4.0,
            "B+": 3.5,
            "B": 3.0,
            "C+": 2.5,
            "C": 2.0,
            "D+": 1.5,
            "D": 1.0,
            "F": 0.0
        }

        total_points = 0.0
        total_credits = 0.0

        for enrollment in self.system.enrollments:

            if enrollment.student == self:

              if enrollment.grade in grade_points:

                    credit = enrollment.course.credits

                    total_points += (
                        grade_points[enrollment.grade] * credit
                    )

                    total_credits += credit

        if total_credits == 0:
            return 0.0

        return total_points / total_credits

    def view_profile(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "date_birth": self.date_birth,
            "email": self.email,
            "student_id": self.student_id,
            "level": self.level,
            "department": self.department.department_name
        }