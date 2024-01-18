# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function
def great():
    print("Hello, how are you doing?")
    print("Isn't the weather nice today?")
great()  

# Function that allows an input
def greet_with_name(name):
    print(f"Hello {name}, how are you doing?")
    print(f"Isn't your name {name}?")

greet_with_name("Samuel")    

# Functions with more than one input
def greet_with(f_name, location):
    print(f"Hello {f_name}")
    print(f"What is it like to be in {location}")

# Position arguments
greet_with("Jack Bauer", "Nairobi")

# Keyword arguments
greet_with(location="Nairobi", f_name="Jack Bauer")



