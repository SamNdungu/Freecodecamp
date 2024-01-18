from abc import ABC, abstractmethod 

# Abstract class
class Computer(ABC):
    @abstractmethod
    # Abstract method
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("It's running!")
        
class Whitboard:
    def write(self):
        print("It's writing...")
                

class Programmer:
    def work(self,com):
        print("Solving Bugs...")
        com.process()
       
#com = Computer()
com1 = Laptop()
#com.process()    
prog1 = Programmer()
prog1.work(com1)

