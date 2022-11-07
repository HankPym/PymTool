import random

# Append value to a list
list = ['Hey']
list.append('Ho')
print(list)

# Append a sequence to a list
list.extend(['Let\'s','go'])
print(list)

# Insert into a list
list.insert(2,'-pause-')
print(list)

# Remove from a list
list.remove('-pause-')
print(list)

# Get an item from the list by index
print(list[1])

# Get an item from the list by backwards index
print(list[-2])

# Get items from the list starting with an index
print(list[1:])

# Get items from the list backwards starting with an index
print(list[-2:])
	
print("-------------------------")

# Build sequence of ten random numbers using list
list = []
for x in range (10):
		list.append(random.randrange(10))
print(list)

# Reverse the sequence of the list
list.reverse()
print(list)

# Count how many times something appears in the list
for x in range(10):
	print(x,"appears",list.count(x), "times")

# Sort the list
list.sort()
print(list)