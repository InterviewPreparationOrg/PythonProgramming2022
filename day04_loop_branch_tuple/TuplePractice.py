numbers = (10, 20, 30, 40, 50, 60, 70, 90, 100)

print(numbers.index(60))

print( numbers.count(10) )

names = ('Ahmet', 'James', 'Ahmet', 'Ahmet', 'Aaron', 'Daniel')

print( names.count('Ahmet') )

print('--------------------------------------')

words = ('Java', 'Python', 'C#', 'Ruby', 'C++')

# words[0] = 'Swift'
# words[5] = 'Cydeo'

print(words)
#print(words[100])

print('--------------------------------------')

elements = ('Java', 'Java', 'Python', 'C#', 'C#', 'C#', 'Cydeo')

for x in elements:
    count = elements.count(x)
    if count == 1:
        print(x)


"""
1. Write a program that can display the unique elements from the tuple
			EX:

				tuple = (10, 10, 20, 30, 30, 40,  40, 40, 50)

				output:
					20
					50
"""

print('--------------------------------------')

group1 = ('Asel', 'Aidai', 'Faruk')
group2 = ('Rene', 'Jimmy', 'Dauren', 'Dinko')
group3 = ('Bella', 'Shay', 'Yulia', 'Aaron', 'Emily')
group4 = ('James', 'Conor', 'John')


groups = (group1, group2, group3, group4)
#index:     0        1       2      3

print(groups)

print(groups[1])
print( groups[1][2] )

print('-------------------------------------------')

for each_group in groups:
    for each_student in each_group:
        print(each_student)






