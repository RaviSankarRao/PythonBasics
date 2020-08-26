
print(2**3)

from math import *
print(pow(2, 3))


# Creating our own exponent function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(4,3))