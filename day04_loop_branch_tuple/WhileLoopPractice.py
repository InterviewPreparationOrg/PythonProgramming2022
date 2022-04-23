
# task1: sum of the numbers between 1 ~ 100
sum = 0

i = 1
while i <= 1000: # i: 1, 2, 3, 4, 5 ... 100
    sum += i
    i+=1

print(f'Sum: {sum}')

print("---------------------------------------------")

# task2: write a program that can reverse a string
word = 'Python Programming'
#index: 012345

reverse = '' #nohtyP

i = len(word) - 1
while i >= 0: #i: 5, 4, 3, 2, 1, 0
    reverse += word[i]
    i -= 1

print(reverse)