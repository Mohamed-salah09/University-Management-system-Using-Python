class Department:
    def __init__(self,department_id,department_name,description,system):
        self.department_id=department_id
        self.department_name=department_name
        self.description=description
        self.system=system
    
    def view_courses(self):
        courses=[]
        for course in self.system.courses:
            if(course.department==self):
                courses.append(course)
        return courses
    
        
    def view_department_info(self):
          return {
            "id": self.department_id,
            "name": self.department_name,
            "description": self.description
        }
    
        