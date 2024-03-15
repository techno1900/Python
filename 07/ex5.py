numbers = [10,23,55,77]

numbers2 = [num for num in numbers]
print(numbers2)


numbers2 = [num*2 for num in numbers]
print(numbers2)



modified_numbers = [num if num>30 else num / 2 for num in numbers]

# print(modified_numbers)

modified_numbers = [num for num in numbers if num>30]


grade = 51

result = "pass" if grade>50 else "failed"

print(result)




numbers = [2,34545,6677]


numbers2 = [num*2 for num in numbers]
print(numbers2)

