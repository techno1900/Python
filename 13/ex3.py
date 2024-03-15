class Truck:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drive(self):
        print(f'the driver is drive truck to this codinates {self.x} and {self.y}')


driver1 = Truck(10,20)
driver1.drive()
driver1.z = 35
print(driver1.z)

