class Student:
    
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
        # From the nested classs, Laptop
        self.lap = self.Laptop( )
        
    def show(self):
        print(self.name, self.regno)
        self.lap.show()
        
    # Nested class
    class Laptop:
        
        def __init__(self):
            self.brand = "Taifa"
            self.cpu = "Corei3"
            self.ram = "4GB"
        
        def show(self):
            print(self.brand, self.cpu, self.ram)
        
st1 = Student("Samuel", 2067)
st2 = Student("Ndungu", 220)        

print(st1.lap.ram)

# Creating an object of inner class inside the outer class
lap1 = Student.Laptop()

st1.show()
