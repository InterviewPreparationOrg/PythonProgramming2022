file_path = '/Users/studio2/PycharmProjects/pythonProgramming2022/day06_openFile_set_dictionary/MyNotes1.txt'

file = open(file_path, "r")

full_text = file.read()

print(full_text)

print("-----------------------")

# full_text2 = file.read()
# print(full_text2)

file = open(file_path, "r")

first_line = file.readline()
second_line = file.readline()

print(first_line)
print(second_line)

print("-----------------------")

file = open(file_path, "r")

for each_line in file.readlines():
    print(each_line)

file.close()
