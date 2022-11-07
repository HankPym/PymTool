import random

guessRange = 50
guessCount = int(guessRange / 5)
guesses = 0
number = random.randint(1, guessRange)

print("I am thinking of an integer between 1 and " + str(guessRange) + ". Can you guess it within " + str(guessCount) + " tries?")

while guesses < guessCount:
    guesses += 1
    print("Guess #" + str(guesses) + ": ", end="")
    guess = int(input())
    if guess == number:
        break
    if guess < number:
        message = 'Your guess is too low.'
    if guess > number:
        message = 'Your guess is too high.' 
    if guesses == guessRange - 1:
        message = message + " Only one guess left!"
    print(message)

if guess == number:
    print('Congrats! You guessed the number in ' + str(guesses) + ' tries!')
else:
    print("Sorry. The number was " + str(number) + ".\n\n") 