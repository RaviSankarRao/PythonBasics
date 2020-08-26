
# { } depicts dictionary inside Python

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions)
print(monthConversions["Sep"])
print(monthConversions.get("Dec"))

# Sending default value if key not found using 'get'
print(monthConversions.get("Bla", "Not a valid key"))