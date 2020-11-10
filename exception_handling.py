# we will have a look at the practical use cases and implementation of try, except, raise, finally

# we will create a variable to store a file data using open()

# Iteration 1
# try: # lets use try block for one line of code where we know an error will be raised
#     file = open("orders.text")
# except:
#     print("Error")


# Iteration 2
try:
    file = open("orders.text")
except FileNotFoundError as err: #creating alias for FileNotFound error in except block
    print(f"Please create an 'orders.text' file" + str(err))

# if we want to see the actual exception together with customised message
    raise

finally: # finally executes regardless of the above conditions
    print("Finally message")