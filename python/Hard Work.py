phrase = "ASSKISSING"
charlist = ""
numlist = ""
charsum = 0

for char in phrase:

    if charlist != "":
        charlist = charlist + "-"
    charlist = charlist + char.upper()

    if numlist != "":
        numlist = numlist + " + "
    numlist = numlist + str(ord(char.upper()))
    
    charsum = charsum + (ord(char.upper()) - 64)

print(phrase.upper())
print(charlist, ":",numlist," = ",charsum,"%")
