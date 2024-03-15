class Robot:
    def __init__(self, x,y):
        self.x =x
        self.y = y
    

    @classmethod
    def specific_walk(cls):
        return cls(30,20)

    def walk(self):
        print(f'specific cordinates {self.x} and {self.y}')


text_walk = Robot.specific_walk()
text_walk.walk()
