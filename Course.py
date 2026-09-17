class Course:

    def __init__(self, course_id, course_name, course_code,
                 credits, description, department):

        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.description = description
        self.department = department
        self.professor = None

    def assign_professor(self, professor):
        from DataBase.Course_db import update_professor

        self.professor = professor
        update_professor(self.course_id, professor.professor_id)

    def remove_professor(self):
        from DataBase.Course_db import remove_professor

        self.professor = None
        remove_professor(self.course_id)

    def view_course_info(self):

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_code": self.course_code,
            "credits": self.credits,
            "description": self.description,
            "department": self.department.department_name,
            "professor": self.professor.name if self.professor else None
        }