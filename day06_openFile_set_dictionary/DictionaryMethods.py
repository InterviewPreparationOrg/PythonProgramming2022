employee1 = {
    'name': 'Asel',
    'gender': 'F'
}

print(employee1['name'])
print(employee1.get('name'))

employee1['name'] = 'Bella'
print(employee1)

employee1.update( {'name': 'Emily'} )
print(employee1)

employee1['name'] = 'Conor'
employee1['gender'] = 'M'

print(employee1)

employee1.update( {'job_title': 'Manager'} )

print(employee1)


employee1['salary'] = 150000

print(employee1)

employee1.pop('salary')

print(employee1)

employee1.popitem()

print(employee1)

employee1.popitem()

print(employee1)

employee1.popitem()

print(employee1)

print("---------------------------------------")


student1 = {
    'name': 'Josh',
    'classes': ['Math', 'Art', 'Python']
}

print(student1['classes'])
print(student1['classes'][1] )



