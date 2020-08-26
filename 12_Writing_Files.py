

employee_file = open("Employees", "a")

# write lines in the previous cursor position
# employee_file.write("Dasari - Useless")

employee_file.write("\nDasari - Useless")

employee_file.close()

# mode - w - will override existing file
# if given file is missing it will create a new file
employee_file = open("Employees", "w")
employee_file.write("\nDasari - Useless")
employee_file.close()