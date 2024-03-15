# class Robot:
#     def __init__(self, x,y):
#         self.x = x
#         self.y =y



# test1 = Robot(1,2)
# test2 = Robot(1,2)

# print(test1==test2)

# print(id(text1))
# print(id(text2))


# class Robot:
#     def __init__(self, x,y):
#         self.x = x
#         self.y =y
    
#     def __eq__(self, value):
#         return self.x == value.x and self.y == value.y


# test1 = Robot(1,2)
# test2 = Robot(1,2)
# print(test1 == test2)



class Robot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        return self.y == value.y and self.x == value.x
    
    def __gt__(self, value):
        return self.x > value.x and self.y> value.x
    

text1 = Robot(3,4)
text2 = Robot(3,4)

# print(text1>text2)
print(text1 == text2)









