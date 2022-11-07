import re

myString = '12 drummers drumming, 11 pipers piping, 10 lords \'a-lording'
myString2 = '9 ladies dancing, 8 swans \'a-swimming'

# Find all digits
myRegex = re.compile('\d+')
print("\nFind all digits")
print(myRegex.findall(myString))

# Find places where 'a-lord' appears, print(text, start and end
# locations and range
myRegex = re.compile('a-lord')
mySearch = myRegex.search(myString)
print("\na-lord group:")
print(mySearch.group())
print("\na-lord start:")
print(mySearch.start())
print("\na-lord end:")
print(mySearch.end())
print("\na-lord span:")
print(mySearch.span())

# Extract the searched value from the string
a = mySearch.start()
b = mySearch.end()
print("\na-lord index by span")
print(myString[a:b])

# Apply regex and determine if something was found
myCheck = myRegex.search(myString)
print("\nSearch myString:")
if myCheck: 
	print('Match found for ', myCheck.group() + ".\n")
else:
	print("No match\n")

myCheck = myRegex.search(myString2)
print("\nSearch myString2 for a-lord:")
if myCheck: 
	print('Match found for ', myCheck.group() + ".\n")
else:
	print('No match found.\n')