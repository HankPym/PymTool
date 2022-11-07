# pylint: disable=invalid-name
''' Runs a monte carlo simulation'''

import random

gameNumber = 100000
gameCount = 0
winCount = 0
changeSelect = 0

# Run games and switch each time
while gameCount < gameNumber:
    theDoor = random.randint(1,3)
    mySelect = random.randint(1,3)
    gameCount = gameCount + 1
    correctFlag = 0
    if mySelect == theDoor:
        correctFlag = 1
    if changeSelect == 0:
        if correctFlag == 0:
            winCount = winCount + 1
    else:
        if correctFlag == 1:
            winCount = winCount + 1

print("Switching: Games: ", gameCount, "   Wins: ", winCount, "   Losses: ",\
    gameCount - winCount, "   Win %: ", str((float(winCount)/gameCount)*100),"%")

# Run games and stick each time
gameCount = 0
winCount = 0
changeSelect = 1
while gameCount < gameNumber:
    theDoor = random.randint(1,3)
    mySelect = random.randint(1,3)
    gameCount = gameCount + 1
    correctFlag = 0
    if mySelect == theDoor:
        correctFlag = 1
    if changeSelect == 0:
        if correctFlag == 0:
            winCount = winCount + 1
    else:
        if correctFlag == 1:
            winCount = winCount + 1

print("Sticking : Games: ", gameCount, "   Wins: ", winCount, "   Losses: ",\
    gameCount - winCount, "   Win %: ", str((float(winCount)/gameCount)*100),"%")
