# To add one item to a set use the add() method.
# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# To add items from another set into the current set, use the update() method.

# Add elements from tropical into thisset:

thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)

print(thisset1)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Add elements of a list to at set:

thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset2.update(mylist)

print(thisset2)

# To remove an item in a set, use the remove(), or the discard() method. If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the remove() method:

thisset3 = {"apple", "banana", "cherry"}

thisset3.remove("banana")

print(thisset3)

# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset4 = {"apple", "banana", "cherry"}

thisset4.discard("banana")

print(thisset4)

# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

# Remove the last item by using the pop() method:
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset5 = {"apple", "banana", "cherry"}

x = thisset5.pop()

print(x)


# The clear() method empties the set:

thisset6 = {"apple", "banana", "cherry"}

thisset6.clear()

print(thisset6)


# The del keyword will delete the set completely:

thisset7 = {"apple", "banana", "cherry"}

del thisset7

print(thisset7)
