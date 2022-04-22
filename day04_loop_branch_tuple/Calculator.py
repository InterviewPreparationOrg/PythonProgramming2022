
n1 = float(input('Enter your first number:\n'))
operator = input('Enter the math operator:\n')
n2 = float(input('Enter your second number:\n'))

result = None

pre_condition = operator == '-' or operator == '+' or operator == '*' or operator == '/' or operator == '%'

if pre_condition:

    if operator == '+' :
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n2
    else:
        result = n1 % n2

    print(result)

else:
    print('Invalid Entry')




"""
1. Create a python file named Calculator
			1.1 Ask the user to enter a number
			1.2 Ask user to enter a math operator (+, -, *, /, %)
			1.3 Ask user to enter the second number
			1.4 Display the calculation result on the console
			
		Ex:
			Given Data:
					10
					*
					5

			Output:
					50
"""