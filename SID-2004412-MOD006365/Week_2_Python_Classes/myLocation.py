# SID: 2004412 - MOD006365

# The python file starts with defining a class which is a type of object that defines a set of attributes and methods and have names it "Location".
# After, a funtion called "__init__" is made with the ".self" parameter used to call upon attributes and methods of the class its being used in.

# Another funtion is created with the name "myLocation" with a print statement.
# Loc1 is a location object in Python, representing the location of "Tomas" in "Portugal". It is created by passing two strings - the location name and the country name

# The purpose of this code being to call upon the "myLocaiton" funtions print statement with different variables multiple times.

class Location:

    def __init__ (self, name, country):
        self.name = name
        self.country = country

    def myLocation (self):
        print ("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the class Location
loc1 = Location ("Tomas", "Portugal")
loc2 = Location ("Ying,", "China")
loc3 = Location ("Amare", "Kenya")
# Call a method from the instantiated class
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()

your_loc = Location ("Your_Name", "Your_Country")
your_loc.myLocation()

