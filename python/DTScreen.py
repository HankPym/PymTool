# Take screenshot at a specified time
# For MacOS

import time
import datetime
import os

myScreenshotTime = "13:32:00"
myFlag = "0"

os.system('clear')

print("Alarm time: " + myScreenshotTime)
while (myFlag == "0"):
	theTime = datetime.datetime.now().strftime("%H:%M:%S")
	showTime = myScreenshotTime + " - " + theTime
	print(showTime)
	time.sleep(0.03)
	if (theTime == myScreenshotTime):
		os.system('screencapture screen.png')
		myFlag = "1"
	time.sleep(0.95)

