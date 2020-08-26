
# new line in a string
print("Ravi\nSankar")

# working with string functions
message = "This is my MESsage"
print(message)
print(message.upper())
print(message.lower())

lower_case_message = message.lower()
print(lower_case_message.islower())

# chaining of functions
print(message.upper().isupper())

# length of a string function
print(len(message))

# grab a character from a string
print(message[12])

# index function
print(message.index("E"))
print(message.index("e"))
print(message.index("my"))
# print(message.index("z"))   # This will throw exception and further execution will stop

print(message.replace("my", "sample"))


