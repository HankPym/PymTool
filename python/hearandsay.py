import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    # tlds:
    #   United Kingdom: co.uk
    #   Austrailia: com.au
    #   US: com
    #   India: co.in
    #   Ireland: ie
    tts = gTTS(text=text, lang="en", tld='com')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

speak("listening...")
text = get_audio()
text = text + " you moron."

speak(text)

