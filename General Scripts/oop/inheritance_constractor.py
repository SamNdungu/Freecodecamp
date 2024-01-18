class A: # A is parent(super) class
    
    # It prints this init if B has no init
    def __init__(self):
        print("In A init")
        
    def feature1(self):
        print("Feature 1 is working") 
        
    def feature2(self):
        print("Feature 2 is working") 
        
# Single-level inheritance             
class B(A): #B(A) denotes that B is inheriting from A, B is child(sub) class
    
    def __init__(self):
        # Get the init in A using super()
        super().__init__()
        print("In B init")
        
    def feature3(self):
        print("Feature 3 is working") 
        
    def feature4(self):
        print("Feature 4 is working")  

#Checks init in B, if not found, it prints init in A        
a1 = B()        
        