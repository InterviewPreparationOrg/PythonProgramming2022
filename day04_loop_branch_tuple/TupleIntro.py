
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# index:    0         1          2              3          4         5          6

print(days[1])
print(days[-2])

print("-------------------------------------")

for each in days:
    print(each)

print("-------------------------------------")

i = len(days) - 1
while i >= 0:
    print(days[i])
    i -= 1

tuple1 = days[2:4+1]

print(tuple1)

work_days = days[:5]

print(work_days)

off_days = days[5:]

print(off_days)


print("-------------------------------------")

group1 = ('Asel', 'Aidai', 'Faruk')
group2 = ('Rene', 'Jimmy', 'Dauren', 'Dinko')
group3 = ('Bella', 'Shay', 'Yulia', 'Aaron', 'Emily')

students = group1 + group2 + group3

print(students)


print('-----------------------------------------')

fruits = ('Orange', 'Cherry', 'Lemon', 'Apple', 'Strawberry')

tuple2 = fruits * 2

print(fruits)
print(tuple2)







