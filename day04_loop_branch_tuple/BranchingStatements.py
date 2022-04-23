word = 'ABCDEFGHIJKL'

for x in word:
    if x == 'D':
        break  # exits the loop

    print(x)

print("---------------------------------------------")

i = 1

while True:
    print(i)
    if i == 5:
        break  # exits the loop
    i += 1

print("---------------------------------------------")

for z in 'ABCDEF':
    if z == 'C' or  z == 'E':
        continue # skips the current iteration
    print(z)

print("---------------------------------------------")

i = 0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i)