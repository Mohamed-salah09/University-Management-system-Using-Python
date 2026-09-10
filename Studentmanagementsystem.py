from Student import *
from Professor import *
from Course import *
from Department import *
from Enrollment import *

class StudentManagementSystem:
    def __init__(self):
        self.students:list[Student] = []
        self.professors:list[Professor]= []
        self.courses:list[Course] = []
        self.departments:list[Department]= []
        self.enrollments:list[Enrollment]= []
        
        self.current_user=None