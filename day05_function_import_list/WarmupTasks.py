numbers = (1, 2, 3, 4, 5, 6, 7)


for x in numbers:
    if x % 2 == 0:
        print(x)

"""
for x in numbers:
    if x % 2 != 0:  # odd number
        continue # skip
    print(x)
"""


print("-----------------------------------------------------------------")

classmates = (
    "Juliette Blake", "Jillian Kane", "Joe Fitzpatrick", "Rodolfo Salinas", "Alexa Cook",
    "Alfredo Stuart", "Audrey Eaton", "Noel Finley", "Salvatore Benjamin", "Kaitlynn Mason")

for s in classmates:
    print(s[0] + "." + s[s.index(' ')+1])





"""
1. Write a program that can display the even numbers from a tuple

		Ex:
			nubers = (1,2,3,4,5,6,7)

			output:
				2
				4
				6

	2. Create a tuple named classmates, and store 10 of your classmates' full names
		Write a program that can display the initials of each student

				names = ('Cydeo School', 'Python Programming', 'Java Programming')

				output:
						C.S
						P.P
						J.P
"""
