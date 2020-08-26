
random = ["Ravi", 2, True]
friends = ["Ravi", "Sankar", "Rao", "Dasari", "John", "Doe"]
lucky_numbers = [4, 8, 10, 16, 23, 42]

print(friends)
print(friends[2])
print(friends[3].upper())

friends = ["Ravi", "Sankar", "Rao", "Dasari", "John", "Doe", "John"]
lucky_numbers = [42, 8, 15, 10, 23, 4]

# adding two lists
friends.extend(lucky_numbers)
print(friends)

# adding item to list
friends.append("New value")
print(friends)

# insert item to list
friends.insert(1, "New inserted value")
print(friends)

# remove item
friends.remove("New inserted value")
print(friends)

# pop an item - Pops the last item
friends.pop()
print(friends)

# find item index
print(friends.index("Dasari"))

# count of repeated items
print(friends.count("John"))

# sorting a list
lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

# clear list
friends.clear()
print(friends)