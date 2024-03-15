class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return(f'our cordinates {self.x} and {self.y}')
    def walk(self):
        print(f'our cordinates {self.x} and {self.y}')


walk = Robot(1,2)
print(walk)
