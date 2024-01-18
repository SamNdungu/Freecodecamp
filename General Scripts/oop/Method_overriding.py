class  A:
    
    def show(self):
        print("A in show")

class B(A):
    # This show overrides the show in class A
    def show(self):
        print("B in show")


a1 = B()
a1.show()
            
            
        