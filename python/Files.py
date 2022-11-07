#!/usr/bin/python

# Open a file
fo = open("outFile.txt", "r+")
str = fo.read(6);
print("Read String is : ", str)

# Check current position
position = fo.tell();
print("Current file position : ", position)

# Reposition pointer at the beginning once again
print("Resetting file position to 0")
position = fo.seek(0, 0);


str = fo.read(6);
print("Again read String is : ", str)
# Close opend file
fo.close()