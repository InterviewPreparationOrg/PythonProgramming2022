
word = 'Python'

l = len(word)

print(l)


def square(number):
    result = number * number
    return result


a = square(5)

print(a)


def cube(number):
    return square(number) * number

b = cube(5)

print(b)


print("-----------------------------------------------------------------------")

def grade(score):
    grade = None
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


result = grade(85)

if result == 'A':
    print('Excellent')
elif result == 'B':
    print('Great')
elif result == 'C':
    print('Good')
elif result == 'D':
    print('Passed')
else:
    print('Failed')


print("-------------------------------------------")

def eligible_to_buy_alcohol(age):
    if age >= 21:
        return True
    else:
        return False


r1 = eligible_to_buy_alcohol(17)

print(r1)

print("-------------------------------------------")

email = 'Cydeo@gmail.com'

r2 = email.endswith('gmail.com')

print(r2)

print("-------------------------------------------")


def addition(n1, n2):
    return n1 + n2


x = 100
y = 10

r3 = addition(400, 500)

print(r3)

print("----------------------------------")


def multiply(a, b):
    return a * b


def area_rectangle(width, length):
    return multiply(width, length)


q = area_rectangle(5, 4)

print(q)










