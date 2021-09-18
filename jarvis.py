import pyaudio
import pyttsx3
import speech_recognition as sr

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query

def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure sir! as your wish, byee")
            break
        if "insta" in command:
            Speak("Best python page on instagram is pythonhub")
        if "learn" in command:
            Speak("copyassignment website is best to learn python")
        if "code" in command:
            Speak("You can get this code from copyassignment website")

