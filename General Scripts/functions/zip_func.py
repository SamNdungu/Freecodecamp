names = ("Samuel", "Eva", "Joy")
computers = ("Taifa", "Mac Book", "HP")

x = list(zip(names, computers))
y = dict(zip(names, computers))
z = set(zip(names, computers))
print(x)
print(y)
print(z)

zipped = zip(names, computers)
for (a, b) in zipped:
    print(a, b)