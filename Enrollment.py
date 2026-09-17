from enum import Enum


class EnrollmentStatus(Enum):
    ACTIVE = "Active"
    DROPPED = "Dropped"
    COMPLETED = "Completed"


class Enrollment:

    def __init__(self, enrollment_id, student, course, semester):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.semester = semester
        self.grade = None
        self.status = EnrollmentStatus.ACTIVE

    def update_status(self, status):
        from DataBase.Enrollment_db import update_status

        self.status = status
        update_status(self.enrollment_id, status)

    def view_enrollment_info(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student": self.student.name,
            "course": self.course.course_name,
            "semester": self.semester,
            "grade": self.grade,
            "status": self.status.value
        }