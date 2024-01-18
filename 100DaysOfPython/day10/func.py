# function with outputs
def  format_name(f_name, l_name):
    
    if f_name == "" or l_name == "":
        return "No valid inputs."
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"
 
print(format_name(input("What's your first name? "), input("What's your last name? ")))