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