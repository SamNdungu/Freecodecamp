class A: # A is parent(super) class
    
    def feature1(self):
        print("Feature 1 is working") 
        
    def feature2(self):
        print("Feature 2 is working") 
        
# Single-level inheritance             
class B(A): #B(A) denotes that B is inheriting from A, B is child(sub) class
    
    def feature3(self):
        print("Feature 3 is working") 
        
    def feature4(self):
        print("Feature 4 is working")    
    
# Multi-level inheritance
class C(B): # Class C inherites form class B, which(class B) is inheriting from class A.
    
    def feature5(self):
        print("Feature 5 is working") 
        
class D: # Class D is independent.
    
    def feature6(self):
        print("Feature 6 is working") 
        
    def feature7(self):
        print("Feature 7 is working")   
        
class E(B,D): #B(A) denotes that B is inheriting from A, B is child(sub) class
    
    def feature8(self):
        print("Feature 8 is working")                    
            
a1 = A()
b1 = B()
c1 = C()
e1 = E()

a1.feature1()
a1.feature2() 
       
b1.feature1() # You can access feature 1 from class A, inside class B.
b1.feature2() # You can access feature 2 from class A, inside class B.
b1.feature3()
b1.feature4() 

c1.feature1()  # You can access feature 1 from class A, through class B inside class C.
c1.feature2() # You can access feature 2 from class A, through class B inside class C.           
c1.feature3() # You can access feature 3 from class B.          
c1.feature4() # You can access feature 3 from class B.             
c1.feature5()            
            
e1.feature1()    
e1.feature2()                 
e1.feature3()                 
e1.feature4() # Class E accesses all features from all classes  except class C                        
e1.feature6()                 
e1.feature7()                 
e1.feature8()                 
             