age = 15
isUSCitizen = True

isEligible = age >= 21 and isUSCitizen

print(isEligible)

print("----------------------------------")

student = False
alumni = False

isEligible = student or alumni
print(isEligible)

print("----------------------------------")

age = 21
fakeID = True

isEligible = age > 21 or fakeID
print(isEligible)

print("----------------------------------")

print( False == True or True != False) # True

print( 10 > 20 and 100 < 1000)  # False

print("----------------------------------")
age = 21
citizen = "USA"

print( age >= 21 and citizen == "USA")

print("---------------------------------------")

r = not True

print(r)

t = not False

print(t)

print("-------------------------------------------")

print(  not (True == False) )













