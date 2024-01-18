class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    # Method overloading _ You cannot do directly i.e you can't have 2 methods with the same name. Hence, we use the trick as follows:
    def sum(self, a=None, b=None, c=None):
        
        s = 0
        
        if a != None and b != None and c != None:
            s = a + b + c   
        elif a != None and b != None:
            s = a + b
        else:
            s = a    
            
        return s     
    
s1 = Student(50, 69)

print(s1.sum(5, 9, 7))
print(s1.sum(5, 9))
print(s1.sum(5))
