# Copy all data from mydata.txt into abc.txt
f = open("mydata.txt", 'r')

f1 = open("data.txt", 'w')

for data in f:
    f1.write(data)