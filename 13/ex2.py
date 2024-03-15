# class Robot:

#     def __init__(self, x,y):
#         pass

#     def walk(self):
#         print(f'walking')



# robot1 = Robot(10,20)
# robot1.walk()


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def walk(self):
        print(f'walking {self.x} and {self.y}')


robot = Robot(10,20)
robot.walk()
