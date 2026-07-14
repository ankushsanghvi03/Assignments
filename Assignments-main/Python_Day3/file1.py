# file = open('student.txt', 'r')
# data = file.read()
# print(data)
# file.close()

file = open('student.txt', 'a+')
file.write("Tony Stark ")
file.write("is the GOAT.")
file.seek(0)  # Move the file pointer to the beginning of the file
content = file.read()
print(content)
file.close()

'''
file = open('student.txt', 'r')
data = file.read()
print(data)
file.close()
'''