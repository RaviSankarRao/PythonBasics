
# Tuples are defined by ()
coordinates = (3, 6)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

# Tuples are immutable. We cannot change the values of tuples
# below line will throw - TypeError: 'tuple' object does not support item assignment

# coordinates[1] = 10

# Tuples are used when you dont want data to be changed

# list of tuples
points = [(3, 2), (4, 5), (7,2)]
print(points)
print(points[1])
print(points[1][0])