if True:
    print('Hello World')

print("---------------------------------")
"""
while True:
    print('Hello World')
"""

i = 1

while i < 11: # i: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    print('Hello World')
    i += 1

print("---------------------------------")

age = int(input('Enter your age:\n'))
us_citizen = input('Are you a US citizen?\n').lower()

while not (us_citizen == 'yes' or us_citizen == 'no'):
    us_citizen = input('Please re-enter! Are you a US citizen?\n').lower()

if age >= 21 and us_citizen == 'yes':
    print('You are eligible to vote')
else:
    print('You are not eligible')


