import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import cv2
import random
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id) 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again please....")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("i am jarvis Sir.please tell me how can I help you")


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        if "open api" in query:
            npath="D:\\api"
            os.startfile(npath)

        elif "open arbaaz" in query:
            apath="D:\\arwaz video\\Export"
            os.startfile(apath)
 
        elif "open github desktop" in query:
            bpath="C:\\Users\\SCH\AppData\\Roaming\\GitHub Desktop"
            os.startfile(bpath)

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\SCH\\Music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir ,rd))
            # for song in songs:
            #     if songs.endswith('.mp3'):
                    # os.startfile(os.path.join(music_dir ,rd))
        

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send message" in query:
            kit.sendwhatmsg("+919719601762","this is testing protocol",2,24)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "email to mohdabbas " in query:
            try:
                speak("what should i say ?")
                content=takeCommand().lower()
                to="avi999880@gmail.com"
                sendEmail(to_content)
                speak("email has been sent to avi")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to sent this mail mohdabbas ")
        
        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day.")
            sys.exit()
        speak("sir , do you have any other work")
  