
is_male = False

# IF....ELSE
if is_male:
    print("The IF condition was true")
    print("You are a male")
else:
    print("you have reached ELSE")
    print("You are not a male")

is_tall = True

#----------------------------------------------------------------

# OR statement
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male not tall")

#----------------------------------------------------------------

# AND statement
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

#----------------------------------------------------------------

# else if -> ELIF
# NOT
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

#----------------------------------------------------------------

# using COMPARISION
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(10,200,30))

#----------------------------------------------------------------

# WHILE loop

i = 1
while i <= 10:
    print(i)
    i = i + 1

#----------------------------------------------------------------

# FOR lopp

for letter in "Sample text":
    print(letter)

names = ["Ravi", "Sanakar", "Rao"]
for name in names:
    print(name)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(names)):
    print(names[index])

