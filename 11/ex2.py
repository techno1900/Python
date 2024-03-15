
# proudtcs = [
#     ('product-1',20),
#     ('product-2',30),
#     ('product-3',25),
#     ('product-4',33),
#     ('product-5',10),
#     ]



# proudtcs.sort(key=lambda product:product[1])
# print(proudtcs)

my_list = [1,2,3,4,6,7,8,9]

lambdalist = filter(lambda x: (x % 2 == 0), my_list)
# for i in lambdalist:
#     print(i)


new_list = map(lambda x: x*2, my_list)
new_list = list(new_list)
print(new_list)
