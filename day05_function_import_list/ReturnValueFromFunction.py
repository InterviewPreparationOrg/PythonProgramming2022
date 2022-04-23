
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













