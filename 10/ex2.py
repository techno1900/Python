
A = {1,2,3,4,5}
B = {4,5,6,7,8}

# union Opearator

print(A | B)

# union method
print(A.union(B))


# intersection opearator

print(A & B)
print(A.intersection(B))


#set Deferent 
print(A-B)
print(B-A)

print(A.difference(B))
print(B.difference(A))

#symentric difference 
print(A ^ B)
print(B ^ A)
print(A.symmetric_difference(B))
