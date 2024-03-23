class Person:
    def __init__(self):
        
        super().__init__()
        print('object 1')
        self.emp = True
    
    def sing(self):
        print('siging')


class Jack(Person):
    def __init__(self):
        print('object 2')
        super().__init__()
        
        self.job = True

    def walk(self):
        print("walking")


person1 = Jack()
print (person1.job)
print (person1.emp)


