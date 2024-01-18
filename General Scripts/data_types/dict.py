data = {1: "Sam", 2: "Jane", 3: "Robert"}

print(data)
print(data[1])
print(data[3])

# Using get() method
print(data.get(2))
print(data.get(4, "Not Found!"))

# Printing a dictionary from a list
keys = ["Alvin", "Peter", "James"]
values = ["Python", "Java", "JavaScript"]

coders =  dict(zip(keys, values))
print(coders)

# Adding values to a dictionary
coders["Patrick"] = "C#"
print(coders)


# Dictionary inside a dictionary
Lang = {'JavaScript': 'Atom', 'C#': 'Vs Code', 'Python': ['Pycharm', 'Sublime Text'], 'Java': {'Java SE': 'NetBeans', 'Java EE': 'Eclipse'}}

print(Lang['Python'])
print(Lang['Python'][1])
print(Lang['JavaScript'])
print(Lang['Java'])   
print(Lang['Java']['Java SE'])  
print(Lang['Java']['Java EE'])  
