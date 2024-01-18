# Using int - immutable
def update(x):
    
    print(id(x))
    
    x = 8
    print(id(x))
    print("X: ", x)
    
a = 10
print(id(a))
update(a)
print("A: ", a)    
    
    
# Using lists - mutable 
def update(lst):
    
    print(id(lst))
    
    x = 8
    print(id(lst))
    print("List: ", lst)

lst = [10, 20, 30]
print(id(lst))
update(list)
print("List: ", lst)     