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
    "Dec": "December",
     12: "December",
}

# Forma de acessar um iten da biblioteca
print(monthConversions["Nov"])

# Outra forma de acessar
print(monthConversions.get("Sep"))

# Outra forma de acessar
print(monthConversions.get(12))