# SID: 2004412 - MOD006365

# The prupose of this task is to...
# - 1. Parses the JSON object R1 into a Python dictionary
# - 2. Prints the parsed Python dictionary onto the console
# - 3. Modify the parsed Python dictionary so that it no longer contains the key "motd" and its associated value
# - 4. Print the parsed python dictionary to the console in a table format with rows and columns
# - 5. Within your python program, create a new python dictionary called R2 with the following key/value pays
# - 6. Print the new python dictionary to the console in a table format with rows and columns similar to this ((*SEE CANVAS SITE WEEK 4*))
# - 7. Parse this new R2 dictionary so that it is converted into a JSON object
# - 8. Print the contents of the JSON object to the console 

# JSON library to enable parsing is imported at the start of the code.

import json

# Below are python dictionaries which store information about R1, and R2.

R1 = '''{
    "hostname": "R1",
    "enable": "cisco",
    "motd": "Unauthorised access is prohibited",
    "encryption": "True",
    "ip_address": "192.168.100.10",
    "username": "cisco",
    "password": "cisco123!"
}'''

R2 = '''{
    "hostname": "R2",
    "enable": "cisco",
    "motd": "No unauthorised access",
    "encryption": "False",
    "ip_address": "192.168.100.100",
    "username": "cisco",
    "password": "class"
}'''

data = json.loads (R1)
data1 = json.loads (R2)

# Above code is loading a JSON object into a python dictionary

print (type(data))
print (data)
print ("\n")

# Above code is displaying dictionary in JSON format

del data ["motd"]

# Above code is removing "motd" and its value from the dictionary

for key, value in data.items():
    print (key, ":", value)

# Above code is iterating through the R1 dictionary and displaying the content in a more readable/table format.

print ("\n")
print ("^^R1 motd has been deleted^^")
print ("\n")

for key, value in data1.items():
    print (key, ":", value)

# Above code is iterating through the R2 dictionary and displaying the content in a more readable/table format.

print ("\n")

json.dumps (data1)
print (data1)

# Finally the R2 dictionary is printed in the JSON format

