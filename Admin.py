from User import User
class Admin(User):

    def __init__(self, user_id, name, date_birth, email, password,admin_id, system):
        super().__init__(user_id, name, date_birth, email, password)
        self.system = system
        self.admin_id=admin_id
        
    def add_student(self, student):
        from DataBase.Student_db import add_student
        self.system.students.append(student)
        add_student(student)
        
    def remove_student(self, student_id):
        from DataBase.Student_db import delete_student
        for student in self.system.students:
            if student_id == student.student_id:
                self.system.students.remove(student)
                delete_student(student_id)
                return True
        return False
    
    def add_professor(self, professor):
        from DataBase.Professor_db import add_professor
        self.system.professors.append(professor)
        add_professor(professor)
        
    def remove_professor(self, professor_id):
        from DataBase.Professor_db import delete_professor
        for professor in self.system.professors:
            if professor_id == professor.professor_id:
                self.system.professors.remove(professor)
                delete_professor(professor_id)
                return True
        return False
    
    def add_course(self, course):
        from DataBase.Course_db import add_course
        self.system.courses.append(course)
        add_course(course)
        
    def remove_course(self, course_id):
        from DataBase.Course_db import delete_course
        for course in self.system.courses:
            if course_id == course.course_id:
                self.system.courses.remove(course)
                delete_course(course_id)
                return True
        return False
    
    def add_department(self, department):
        from DataBase.Department_db import add_department
        self.system.departments.append(department)
        add_department(department)
        
    def remove_department(self, department_id):
        from DataBase.Department_db import delete_department
        for department in self.system.departments:
            if department_id == department.department_id:
                self.system.departments.remove(department)
                delete_department(department_id)
                return True
        return False