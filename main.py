import pyttsx3

import speech_recognition as sr

import wikipedia

import webbrowser

import os

import random

import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    def userName():
        speak('Kindly enter your name')
        name = input('Kindly Enter your name ')

        return name

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak(f'Hello {userName()}, How can I help you today ?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Please say that again')
        return 'None'
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace('Wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open udemy' in query:
            webbrowser.open('www.udemy.com')

        elif 'open gmail' in query:
            webbrowser.open('www.gmail.com')

        elif 'play songs' in query:
            music_dir = 'C:\\Users\\SOUMYA\\Downloads\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 8)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strTime}')

        elif 'open code' in query:
            codePath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.4\\bin\\pycharm64.exe'
            os.startfile(codePath)

        elif 'quit' in query:
            exit()
