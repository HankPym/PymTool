import random

# Set seed
random.seed()

# Generate random number between 0 to 1
print(random.random())

# Generate from 0 to 500
print(random.randrange(500))

# Generate from 500 to 1000
print(random.randrange(500,1000))

# Manually create a sequence
mySeq = [1,2,3,4,5,6,7]
print(mySeq)

# Shuffle the sequence
random.shuffle(mySeq)
print(mySeq)

# Now reorder the sequence
print(sorted(mySeq))

print('-------------')

# Build a sequence of ten random numbers between 0 and 29
myRandSeq = random.sample(range(30),10)
print(myRandSeq)

# Sort the sequence
myRandSeq.sort()

print(myRandSeq)

# Shuffle the sequence
random.shuffle(myRandSeq)
print(myRandSeq)
