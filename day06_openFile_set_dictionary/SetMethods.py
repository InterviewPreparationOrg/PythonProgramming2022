
elements = {"A"}

print(elements)

elements.add('B')

print(elements)

elements.add('C')
elements.add('C')
elements.add('C')

print(elements)

elements.update(('D', 'E', 'F'))

print(elements)


elements.remove('B')

print(elements)

print( len(elements) )

elements.pop()

print(elements)

elements.clear()

print(elements)


print("-------------------------------------")

set1 = {1, 2, 3, 4}

set2 = set1.copy()

print(set2)

print("-------------------------------------")

s1 = {'A', 'B', 'C', 'D', 'E'}
s2 = {'D', 'E', 'C', 'F'}

s3 = s1.difference(s2)
s4 = s1.intersection(s2)

print(s3)
print(s4)

print("--------------------------------------")

for x in s4:
    print(x)



