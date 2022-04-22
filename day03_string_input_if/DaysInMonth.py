number = 1

has28Days = number == 2
has30Days = number == 4 or number == 6 or number == 9 or number == 11

if 1 <= number <= 12:  # precondition: number must be between 1 ~ 12

    if has28Days:
        print('28 days')
    elif has30Days:
        print('30 days')
    else:
        print('31 days')

else:
    print('Invalid Number')

"""
3. Write a program that can print the number of days in a month

	            Ex:
	                number = 1;

	            output:
	                31 Days

	            Hints:
	                Months that has 31 days: 1, 3, 5, 7, 8, 10, 12
	                Months that has 30 days: 4, 6, 9, 11
	                Month that has 28 days: 2

"""