#importing modules
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random
import math

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning Sir,")
        print("Good Morning !")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon Sir,")
        print("Good Afternoon !")

    else:
        Speak("Good Evening Sir,")
        print("Good Evening !")

    # Speak("Hi Sir, I am Jarvis. How can I help you ?")


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("goooglekeda@gmail.com", "dabir7890")
    server.sendmail("goooglekeda@gmail.com", to, content)
    server.close()


#taking microphone input and give string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2.5)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognising...")
        # Speak("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query


if __name__== "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        #logic for executing tasks
        if "wikipedia" in query:
            Speak("Searching in WikiPedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to wikipedia")
            print(results)
            Speak(results)

        elif "open youtube" in query:
            Speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            Speak("Opening google...")
            webbrowser.open("www.google.com")

        elif "open stalkoverflow" in query:
            Speak("Opening stalkoverflow...")
            webbrowser.open("www.stalkoverflow.com")

        elif "open facebook" in query:
            Speak("Opening Facebook...")
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            Speak("Opening Instagram...")
            webbrowser.open("www.instagram.com")

        elif "find" in query:
            query = query.replace("find", "")
            results1 = wikipedia.summary(query, sentences=5)
            print(results1)
            Speak(results1)

        elif "play song" in query:
            Speak("Playing Songs...")
            music_dir = "C:\\Users\\abira\\Music\\2021"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randrange(1, 66).__floor__()]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strtime}")

        elif "open pycharm" in query:
            Speak("Okay, Sir !")
            #set songs file path here
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)

        elif "email to dk" in query:
            try:
                Speak("What should I say ?")
                content = takecommand()
                to = "goooglekeda5@gmail.com"
                sendemail(to, content)
                Speak("Email Sent !")

            except:
                Speak("Sorry Sir! I am facing some issues to send ")
