
# function is defined using 'def' in python
# ':' says python that the function code starts here
# Whatever is within the function indentation is part of function
def say_hi():
    print("Inside function")
    print("Hello user")
    print("function ends")

# calling a function
say_hi()

print("Outside a function")

# function with parameters
def sayhi(name, age):
    print("Hello " + name + ". Your age is " + str(age))

sayhi("Ravi", 20)

# return statement in functions
def add(input1, input2):
    result = float(input1) + float(input2)
    return result

print(add(11.4, 20.3))

