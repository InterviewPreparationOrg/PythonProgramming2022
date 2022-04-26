car1 ={
    'make': 'Toyota',
    'model': 'Camry',
    'year': 2018,
    'color': 'Black',
    'price': 25000
}

for x in car1.keys():
    print(x)

print("------------------------------")


for y in car1.values():
    print(y)

print("------------------------------")

print( car1.items())
print( list(car1.items())  )

print("------------------------------")

for pair in list(car1.items()):
# print(pair)
    print(pair[1])




