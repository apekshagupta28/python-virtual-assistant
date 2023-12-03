import pyttsx3    #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import yagmail
import requests
import json
import random  
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[0])

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak('Good morning')

    elif hour>=12 and hour<18:
        speak('Good afternoon')

    else:
        speak('Good evening')

    speak('sir i am your assisstant. Please tell me how may i help you')

def takeCommand():
    
    # it takes microphone input from the user and return string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)  

    try:
        print("Recognizing...") 
        query=r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"

    return query

speak("Tell me the code word")
query=takeCommand().lower()
if "alexa" in query: 

    wishMe()

    while True:
        query=takeCommand().lower()
        speak(query)

        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia...')
            print(results)
            speak(results)

        elif 'quit' in query:
            speak('Thankyou have a nice day!!')
            break

        elif 'open youtube' in query:
            speak('What do you want to search on YouTube?')
            search_query = takeCommand()
            speak(f'Playing {search_query} on YouTube.')
            pywhatkit.playonyt(search_query)

        elif 'play video' in query:
            speak('What video do you want to play on YouTube?')
            video_query = takeCommand()
            search_url = f'https://www.youtube.com/results?search_query={video_query}'
            webbrowser.open(search_url)    

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open pinterest' in query:
            speak('What do you want to search on pinterest?')
            pinterest_search = takeCommand()
            find_pin=f'https://in.pinterest.com/search/pins/?q={pinterest_search}&rs=typed'
            webbrowser.open(find_pin)

        elif 'open twitter' in query:
            webbrowser.open('https://twitter.com/explore/tabs/trending')

        elif 'play music' in query:
            speak('Which song would you like to play on spotify?')
            music_query = takeCommand()
            search_music = f'https://open.spotify.com/search/{music_query}'
            webbrowser.open(search_music)

        elif 'search' in query:
            search=query.replace('search','')
            search='https://www.google.com/search?q='+search
            webbrowser.open(search)


        elif 'what\'s the time' in query:
            time=datetime.datetime.now().strftime("%I:%M %p")
            
            print(time)
            speak(time)

        elif 'what\'s the date' in query:
            date=datetime.datetime.now().strftime("%d:%B %Y")

            print(date)
            speak(date)

        elif 'what\'s the news' in query:
            url="https://newsapi.org/v2/top-headlines?country=in&apiKey=f4dff133d2674e6da2d777257fe41c8c"

            news=requests.get(url).text
            news=json.loads(news)
            art=news["articles"]

            speak('Today\'s top news')
            for i,article in enumerate(art):
                if i==5:
                    break

                elif i==4:
                    
                    speak('last news is...')
                    print(article["description"])
                    speak(article["description"])
                    

                else :
                    print(article["description"])
                    speak(article["description"])
                    speak('Moving on to the next news...')
            speak('Thank you for listening... have a nice day')

else:
    speak(query+"this is wrong word")