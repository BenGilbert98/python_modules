# use json module to do json encoding and decoding

import json

car_data = {"name": "tesla", "engine": "electric"}  # creating dictionary and storing it into a variable
print(type(car_data))

# json.dumps - serialises json to a formatted string
# json.dump() - creates a steam object and except a file object to write to
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# this is how we can encode from a dictionary and write to a file
with open("new_json_file.json", "w") as jsonfile:  # with open("<file_name>", "w") "w" gives write permissions
    json.dump(car_data, jsonfile)

try:
    with open("new_json_file.json", "r") as jsonfile:
        car = json.load(jsonfile)  # load() copies the data and stores to a variable "r" gives read permissions
        print(car)
        print(type(car))
        print(car["name"])
        print(car["engine"])
except FileNotFoundError:
    print("Oh no the file is not found ... please try again. ")
finally:
    print("""The finally clause executes before the try statement completes and will run regardless of whether the 
          try statement produces an exception or not""")

# getting the value by keys
# Json is used heavily in the industry so reading(encoding), writing(decoding), parsing data and converting data
# are the most commonly utilised options

# exception handling


# add the exception handling required blocks to check if the file is created if not return back the original exception
# together with customised user friendly message
