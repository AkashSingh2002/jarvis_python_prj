from ast import excepthandler
import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    time = int(datetime.datetime.now().hour)
    if time>=1 and time<12:
        speak("good morning")
    elif time >=12 and time <17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello how may i help you sir")

def command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio,language = 'en-in')
        print("user said: ",query)

    except :
        print("pls say that again:")
        return 'none'
    return query
    
wishme()
command()