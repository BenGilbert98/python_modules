# import requests
# import json

# live_response = requests.get("http://api.postcodes.io/postcodes/cr82hs")


# argument = input("Please enter your postcode      ")
#
# url_target = live_response + argument

# print(live_response.content)
# print(type(live_response.content))

# Research how to convert this data into dictionary
# HINT - python json library / module/ method cna be used to resolve this

# Iterate through data and print RESULTS

import requests
import json


def find_LongitudeLatitude():
    while True:  # Continually prompts user for input
        postcode = input("What is your postcode?    ")  # Asks user to enter postcode

        if postcode == "Exit":  # if user enters "Exit" program exits
            break
        live_response = requests.get(f"http://api.postcodes.io/postcodes/{postcode}")  # uses postcode in url

        if live_response.status_code == requests.codes.ok:  # if the status code is good:
            print(f"Status code: {live_response.status_code}")
            y = json.loads(live_response.content)  # converts live_response.content to a dictionary
            # iterates through dictionary to find keys of "longitude" and "latitude" and prints the value.
            for i in y["result"]:
                if i == "longitude":
                    print(f"The longitude position at this postcode is", y["result"][i])

                if i == "latitude":
                    print(f"The latitude position at this postcode is", y["result"][i])

        # Alternative Code to check dictionary for specified values
        # outputs = ["postcode", "longitude", "latitude"]
        # for i in display_info:
        #     print(f"{i.capitalize()} : {y['result'][i]}")

        elif live_response.status_code == requests.codes.not_found:  # if the status code is bad:
            print(f"Status code: {live_response.status_code}, Please Enter a valid postcode")


find_LongitudeLatitude()
