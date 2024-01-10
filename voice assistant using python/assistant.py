import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ec
from bs4 import BeautifulSoup
import ctypes
import pyjokes
from urllib.request import urlopen
import win32com.client as wincl

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    assname = "Jarvis 1.0"
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you, sir?")
    uname = take_command()
    speak(f"Welcome, Mister {uname}")
    print(f"Welcome, Mr. {uname}")
    speak("How can I help you, Sir")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Replace 'your_email' and 'your_password' with your email credentials
    server.login('your_email', 'your_password')
    server.sendmail('your_email', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wish_me()
    username()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google")
            webbrowser.open("google.com")

        elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key 
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands


