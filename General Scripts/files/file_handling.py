f = open("mydata.txt", 'r')

print(f.readline()) # only the first line
print(f.read())

# Writing to a file
f1 = open("abc.txt", 'w')
f1.write("Something...")

