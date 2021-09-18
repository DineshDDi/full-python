"""
import os
import speech_recognition as sr

while True:
    y = sr.Recognizer()
    with sr.Microphone() as source:
        print("speek something ....")
        audio = y.listen(source)
        try:
            text = y.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            else:
                if text == "Open Google Chrome":
                    os.startfile('')
                elif text == "Open Pycharm":
                    os.startfile('')
        except:
            print("")
"""


