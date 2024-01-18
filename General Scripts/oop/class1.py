class Student :
    
    def __init__(self):
        self.name = "Samuel"
        self.age = 36
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False     
        
    def update(self):
        self.age = 30
        

s1 = Student()
s2 = Student()   
           
s1.update()

# Cmparing ages
if s1.compare(s2):
    print("They are the same.")
else:
    print("They are different")    

print(s1.name)
print(s1.name)            
            
            
            