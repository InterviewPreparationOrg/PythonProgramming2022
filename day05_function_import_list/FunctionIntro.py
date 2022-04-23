def greeting():
    print("Hello Everyone!")
    print("How are you all today?")


greeting()
greeting()
greeting()

print("-------------------------------")


# 1. create a function that can print odd numbers between 1~100 in a same line separated by space
def print_odd_1to100():
    result = ''
    i = 1
    while i <= 100:
        result += str(i) + " "
        i += 2

    print(result)


# 2. create a function that can print even numbers between 1~100 in a same line separated by space
def print_even_1to100():
    result = ''
    i = 2
    while i <= 100:
        result += str(i) + " "
        i += 2

    print(result)



print_odd_1to100()
print_even_1to100()


"""

2. create a function that can print even numbers between 1~100 in a same line separated by space

3. create a function that can print a Rectangle
                
                * * * * * 
                * * * * *
                * * * * *
                * * * * *
                * * * * *
                * * * * *
                
"""
