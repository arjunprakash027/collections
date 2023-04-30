class base1():
    def __init__(self):
        self.id = 1
    
    def display(self):
        print("Base1")

class base2():
    def __init__(self):
        self.id = 2
    
    def display(self):
        print("Base2")



dics = {1:base1(),2:base2()}

dics[1].display()