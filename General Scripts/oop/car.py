class Car:
    
    wheels = 4 # Class variable - Class namespace
    
    def __init__(self):
        
        # Instance variables - Instance/object namespace
        self.millage = 100
        self.company = "BMW"
        
c1 = Car()
c2 = Car()

c1.millage = 8

Car.wheels = 10


print(c1.company, c1.millage, c1.wheels)        
print(c2.company, c2.millage, c2.wheels)        
        
        
        