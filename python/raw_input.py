import re

myString = input("Enter your name: ")

hold = re.search(r'(.*)Les(.*)',myString)

if hold:
	print("\nYes")
else:
	print("\nNo")