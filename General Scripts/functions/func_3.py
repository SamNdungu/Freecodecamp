def student(name, **data): # ** means Keyword variable lengthargument
    
    print(name)
    # print(data) 
    
    for i, j in data.items():
        print(i, j)

student("Samuel", age=36, city="Nairobi", Mobile=90712829281)    