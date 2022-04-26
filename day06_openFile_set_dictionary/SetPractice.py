t1 = (1, 2, 3, 4, 1, 2, 3, 4) # Tuple
l1 = [1, 2, 3, 4, 1, 2, 3, 4] # List
s1 ={1, 2, 3, 4, 1, 2, 3, 4, 1 , 2} # Set
s2 = {'A', 'B', 'A', 'C', 'D', 'C'} # Set

print(t1)
print(l1)
print(s1)
print(s2)


print("----------------------------")
print(t1[0])
print(l1[0])
# print(s1[0])

print("--------------------------------")

tuple1 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
result1 = set(tuple1)

print(result1)

set1 = {1,2,3,4,5}
list1 = list(set1)
tuple2 = tuple(set1)

print(list1)
print(list1[0])

print(tuple2)
print(tuple2[0])