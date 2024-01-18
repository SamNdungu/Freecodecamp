class Computer:
    
    def config(self):
        print("Comuter Specifications are: corei5, 16GB RAM SSD, 1TB SSD")
        
comp1 = Computer()
comp2 = Computer()

Computer.config(comp1)
comp1.config() # Works same as above
 
Computer.config(comp2)        
comp2.config() # Works same as above
         