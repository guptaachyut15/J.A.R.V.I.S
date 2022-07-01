import random


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning master!\n How may I help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon master!\n How may I help you?")
    else:
        speak("Good Evening master!\n How may I help you?")
def takecommand():
    '''Takes speech command from the user and converts it into text'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return 'None'
    return query


if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak("According to wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open mail" in query:
            webbrowser.open("gmail.com")
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif "movie" in query:
            movie_path="D:\\Series and Movies\\movies"
            mov=os.listdir(movie_path)
            os.startfile(os.path.join(movie_path,mov[random.randint(0,11)]))



