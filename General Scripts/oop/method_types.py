class Student:
    
    # Clas variable, school  
    school = "Murang'a"
    
    # Instance method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3    
    
    # Class method
    @classmethod  
    def getSchool(cls):
        return cls.school 
    
    # Static method - No self or cls keywords inside brackets
    @staticmethod
    def info():
        print("This is a student class in types of methods")
        
st1 = Student(34, 67, 32) 
st2 = Student(25, 36, 19)    

# Instance method - accessor method  
print(st1.avg())
print(st2.avg())

# class method
print(Student.getSchool())

# Static method
print(Student.info())