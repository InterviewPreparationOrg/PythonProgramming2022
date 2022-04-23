def display_value(value):
    print(f'The value is {value}')


display_value(100)

display_value(2000)

print("----------------------------------------------")


def eligible_to_buy_alcohol(age):
    if age >= 21:
        print('You are eligible to buy alcohol')
    else:
        print('You are not eligible to buy alcohol')


eligible_to_buy_alcohol(20)

print("----------------------------------------------")


def find_max_number(num1, num2):
    if num1 > num2:
        print(f'{num1} is greater')
    elif num2 > num1:
        print(f'{num2} is greater')
    else:
        print('both are equal')


find_max_number(100, 100)

print("----------------------------------------------")


def print_each(sequence):
    for x in sequence:
        print(x)


classmates = (
    "Juliette Blake", "Jillian Kane", "Joe Fitzpatrick", "Rodolfo Salinas", "Alexa Cook",
    "Alfredo Stuart", "Audrey Eaton", "Noel Finley", "Salvatore Benjamin", "Kaitlynn Mason")

print_each(classmates)

print("-------------------------------------")

print_each('Cybersecurity')

print("------------------------------------------")


# create a function that can calculate the grade of the student based on the score
def grade(score):
    result = 'Your garde is '
    if 0 <= score <= 100:
        if score >= 90:
            result += 'A'
        elif score >= 80:
            result += 'B'
        elif score >= 70:
            result += 'C'
        elif score >= 60:
            result += 'D'
        else:
            result += 'F'
    else:
        result = 'Invalid Score'

    print(result)


grade(95)

"""
1. create a function that can check if a person is eligible to vote
            Ex:
                eligibleToVote(19, "USA");

            output:
                You are not eligible to vote! 

2. create a function that can calculate the grade of the student based on the score

3. create a function that can if the given integer is positive, negative or zero 
	"""
