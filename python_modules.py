# Lets have a look at some built in functions in Python

# import is the key word used to call modules from Python library

# First iteration
import random

# We have random method in Python library which we use by importing
# print(random.random())  # generates float number between 0 and 1

# Second Iteration
# from random import random
# print(random())


# import math

# number_float = 23.44
# print(math.floor(number_float))  # floor method rounds the figure to lower end
# print(math.ceil(number_float))  # ceil method rounds the figure to upper end

# Task
# get user input of a float number
# check if number is lower than .50 then round to lower end
# if number is greater than .50 then round to upper end

import math


# print(math.pi)  # prints pi


# Function which determines what is after the . in a float number
def round_number():
    while True:
        number = float(input("What number would you like to round?    "))
        decimal = str(number).split('.')[1][0]
        # if the value after decimal is 5 or more it rounds up
        if decimal >= "5":
            math.ceil(number)
            print(math.ceil(number))
        # else it rounds up
        else:
            math.floor(number)
            print(math.floor(number))


round_number()

import os
# To find out system configuration or system related information
# based on the information provided we can handle the user request

import math, datetime, sys  # multiple modules can be imported at once

# working_dir = os.getcwd()
# print(working_dir)

# Lets find out the name of our os (Linux only)
# print(os.uname())

# Lets count the number of CPUs
# print(os.cpu_count()) # gives us CPU count inside os

# Lets find out the current date
# print(datetime.datetime.today())
# datetime module allow us to find current date / time etc

# To find out system path
# print(sys.path)

# How can we create a customised method and utilise the built in functionality at the same time
# When and why should we do that
# def current_system_path():
#     print(f"this is your current directory \n {sys.path}")
# current_system_path()

# pip is used to install packages within python
