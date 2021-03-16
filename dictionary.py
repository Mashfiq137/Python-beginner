'''
jan --> January
feb --> February
mar --> March
'''

monthConversion = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June"
}

print(monthConversion["apr"])
print(monthConversion.get("jan")) # returns a 'None' value when not found
print(monthConversion.get("lov","Not a valid key. Try again!"))
