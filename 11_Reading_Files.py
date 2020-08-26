

# using OPEN cmd to open files
# first param - File name with relative path
# second param - mode
# r - read, w - write, a - append, r+ - read and write

employee_file = open("Employees", "r")

# check if file is readable
print(employee_file.readable())

# read - read the entire file
# print(employee_file.read())

# readline - read line by line
# print(employee_file.readline())
# print(employee_file.readline())

# readlines - convert each line to array
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

# always close thf ile at the end of your execution
employee_file.close()