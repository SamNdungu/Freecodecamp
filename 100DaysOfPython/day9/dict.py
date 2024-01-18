programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items in the programming_dictionary
y = programming_dictionary["Bug"]


# Adding items in the programming_dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#print(programming_dictionary)

# Empty dictionary
empty_dict = {}

# Wipe out existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary["Bug"] = "A mog in the computer"
print(programming_dictionary)

# Looping through the dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting dictionaries in dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log)


# Nesting a dictionary in a list 
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

print(travel_log)
