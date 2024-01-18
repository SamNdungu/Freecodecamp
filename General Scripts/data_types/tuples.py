# Packing a tuple:

fruits = ("apple", "banana", "cherry")

# In Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#  The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
# Assign the rest of the values as a list called "red":

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green1, yellow1, *red1) = fruits1

print(green1)
print(yellow1)
print(red1)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Add a list of values the "tropic" variable:

fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green2, *tropic2, red2) = fruits2

print(green2)
print(tropic2)
print(red2)

# Loop Through a Tuple

# for loop: Iterate through the items and print the values.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Loop Through the Index Numbers

# Print all items by referring to their index number:

thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
  print(thistuple1[i])


# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
# Remember to increase the index by 1 after each iteration.
thistuple2 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple2):
  print(thistuple2[i])
  i = i + 1


#Join Two Tuples - To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  


# Multiply Tuples - If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits3 = ("apple", "banana", "cherry")
mytuple = fruits3 * 2

print(mytuple)


# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found