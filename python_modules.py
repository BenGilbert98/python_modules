# Lets have a look at some built in functions in Python

# import is the key word used to call modules from Python library

# First iteration
import random

# We have random method in Python library which we use by importing
# print(random.random())  # generates float number between 0 and 1

# import math

# number_float = 23.44
# print(math.floor(number_float))  # floor method rounds the figure to lower end
# print(math.ceil(number_float))  # ceil method rounds the figure to upper end

# Task
# get user input of a float number
# check if number is lower than .50 then round to lower end
# if number is greater than .50 then round to upper end

import math

print(math.pi)


def round_number(num):
    decimal = str(num).split('.')[1]
    if decimal >= "5":
        math.ceil(num)
        return print(math.ceil(num))
    else:
        math.floor(num)
        return print(math.floor(num))


while True:
    number = float(input("What number would you like to round?    "))
    round_number(number)
