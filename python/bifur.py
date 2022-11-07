def bifurc(levelCount, inLow, inHigh):
    levelCount += 1
    print(levelCount)
    return

startNum = 128

firstDiv = startNum / 2
levelCount = 3

lowerNum = firstDiv - (firstDiv / 2)
higherNum = firstDiv + (firstDiv / 2)
levelCount += 1
print(levelCount)
bifurc(levelCount, lowerNum, higherNum)



