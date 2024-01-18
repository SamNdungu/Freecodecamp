# What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:

# The return keyword will exit the function and prevent the rest of the code from being executed.
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25)) # None





