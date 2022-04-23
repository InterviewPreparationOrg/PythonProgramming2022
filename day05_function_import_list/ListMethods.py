numbers = [10, 20, 30, 40, 50]

numbers.append(60)
#numbers.append(('A', 'B'))

print(numbers)


numbers.clear()

print(numbers)
print(len(numbers))

print("-------------------------------------")

words = ['Cydeo', 'C#', 'C++', 'Ruby']

print(words)

words.extend( ('Java', 'Python', 'Swift') )

print(words)

print("----------------------------------------------")

nums = [100, 20, 55, 15, 0, -1, 30, 40, 16]

nums.sort() # sorted in ascending order

print(nums)

nums2 = [100, 20, 55, 15, 0, -1, 30, 40, 16]
nums2.sort(reverse= True)  # sorted in descending order


print(nums2)

print("--------------------------------------------------")


names = ['Dauren', 'Dzmitry', 'Aidai', 'Faruk', 'Asel', 'Mirigul']

names.reverse()

print(names)

print("--------------------------------------------------")

n1 = [1, 2, 3, 4, 5, 6, 7]
n2 = n1.copy()

#n1.append(100)
print(n1)
print(n2)

print(n1 is n2)


print("--------------------------------------------------")

students = ['Dauren', 'Dzmitry', 'Aidai', 'Faruk', 'Asel', 'Mirigul']

print(students)

students.remove('Dauren')

print(students)

students.remove('Faruk')

print(students)


print("--------------------------------------------------")

l = [50, 100, 150, 200, 250, 300]

l.pop()

print(l)

l.pop()

print(l)

print('------------------------------------------------')

s = ['A', 'B', 'C', 'D', 'E', 'F']

print(s)

s.pop(1)

print(s)

print('------------------------------------------------')

languages = ['Java', 'C#', 'C++', 'Ruby', 'Swift']

languages.insert(1, 'Python')

print(languages)

print('------------------------------------------------')

print( languages.index('C++'))
# print( languages.index('HTML'))

print('------------------------------------------------')

elements = [1,1,1,2,2,2,3,4,5,6,7,8,9,10, 5, 5, 5, 5]

print(elements.count(5))



















