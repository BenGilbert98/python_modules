# importing requests to make an api call to www

import requests
import emoji

# Checking website status

live_response = requests.get("https://www.bbc.co.uk/")


# print(live_response.headers)
# print(live_response.content)

# it provides an integer as a response code
# First Iteration

# it provides an integer as a response code
# if live_response.status_code == 200:
#     print('Mission Successful!', emoji.emojize(":thumbs_up:"), str(live_response.status_code))
#
# else:
#     print("oops something went wrong... ")

# Second Iteration
# def check_response_code():
#     if live_response.status_code == 200:
#         print('Mission Successful!', emoji.emojize(":thumbs_up:"), str(live_response.status_code))
#     elif live_response.status_code == 404:
#         print(" the site in unavailable util further notice. Please come back later")
#     else:
#         print("oops something went wrong... ")

# Third Iteration
# what does the requests module bring to the table
def check_response_code():
    if live_response.status_code:  # Will evaluate as true if the code is between 200-400, otherwise false
        print('Mission Successful!', emoji.emojize(":thumbs_up:"), str(live_response.status_code))
    elif live_response.status_code == 404:
        print(" the site in unavailable util further notice. Please come back later")
    else:
        print("oops something went wrong... ")
# requests comes with built in status code lookup object so you can easily reference.
