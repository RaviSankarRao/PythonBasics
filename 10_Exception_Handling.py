
input_text = input("Enter a number: ")

try:
    number = int(input_text)
    print(number)
except:
    print("Invalid input")


# Catching specific exceptions

input_text = input("Enter a number: ")
try:
    value = 10/0
    number = int(input_text)
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid input")

