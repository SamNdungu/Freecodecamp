def div(a, b):
    print(a / b)
    
# This functions changes behavior of the div function by swapping values when a < b  
def smart_div(func):
    
    # A function to swap a and b i.e a, b = b, a  
    def inner(a, b):
        if a < b: 
            a, b = b, a 
        return func(a, b)    
    
    return  inner

# Re-defining the div function
div = smart_div(div)
div(3, 9)