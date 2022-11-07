"""
sayit - a python module to speak a text input.
    Works with Windows or Mac
    Les Fister, Fystems
    2022-10-09
"""

from gtts import gTTS
from playsound import playsound
import platform
import os

def sayit(msg):
    speech = gTTS(text = msg)  # convert the messaage to sound
    if platform.system() == "Darwin":                            # this is a Mac
        speech.save('/Users/lfister/Downloads/SayItTemp.mp3')    # save the sound file
        playsound('/Users/lfister/Downloads/SayItTemp.mp3')      # play the sound file
        os.remove('/Users/lfister/Downloads/SayItTemp.mp3')      # delete the sound file

    # function to speak a text message
    else:                                       # this is Windows
        speech.save('C:/temp/SayItTemp.mp3')    # save the sound file
        playsound('C:/temp/SayItTemp.mp3')      # play the sound file
        os.remove('C:/temp/SayItTemp.mp3')      # delete the sound file
