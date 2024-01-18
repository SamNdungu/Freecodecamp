class Computer:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Computer configurations is: ", self.cpu, self.ram)


comp1 = Computer("Corei5", "16GB RAM")
comp2 = Computer("Corei7", "32GB RAM")

comp1.config()
comp2.config()





