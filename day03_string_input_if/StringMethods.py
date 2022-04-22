
name = 'CYDEO SCHOOL'

name = name.lower()  # 'asel'

print(name)

print("------------------------------------")

s1 = 'python programming language'
s2 = s1.upper()

print(s2)

print("-------------------------------------")

s3 = 'cyDEO'
s3 = s3.capitalize()  # Cydeo

print(s3)

print("-------------------------------------")

school_name = 'cyDEO schoOL'

# school_name= school_name.capitalize()
school_name = school_name.title() # Cydeo School

print(school_name)

tv_show = 'the walking dead'

tv_show = tv_show.title()

print(tv_show)

print("-------------------------------------")

str1 = '       Python         '
str1 = str1.strip()

print(len(str1))
print(str1)

print("-------------------------------------")

word = 'Python Programming'

i1 = word.index('g')
print(i1)

i2 = word.rindex('g')
print(i2)

print("-------------------------------------")

sentence = 'I love python programming'

result = sentence[sentence.index('p'):]

print(result)

print('---------------------------------------')

sentence2 = 'python is the easiest programming language, I love python'

print(sentence2.index('p'))
print(sentence2.index('pr'))
print(sentence2.rindex('p'))

print('---------------------------------------')

sentence = 'I love Java programming language'
sentence = sentence.replace('Java', 'Python' )

print(sentence)

print('---------------------------------------')

s = 'Hello Hello Hello'
print(s.count('Hello'))

s = 'pyTHON python PYTHON python'
print(s.lower().count('python'))

print('---------------------------------------')

url = 'www.amazon.com'

r1 = url.startswith('www.')
print(r1)

r2 = url.endswith('.com')
print(r2)

print('---------------------------------------')

email = 'cydeo@yahoo.com'

isGmail = email.endswith('gmail.com')
isYahoo = email.endswith('yahoo.com')

print(isGmail)
print(isYahoo)


