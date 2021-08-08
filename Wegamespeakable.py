


import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
from gtts import gTTS
from tkinter import *
from PIL import Image
import subprocess
import os
import sys
from PIL import Image, ImageTk


print("enter your name")

#root = tkinter.Tk()
#inname ="tenor.gif"
#root.mainloop()
 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def userstart():
    print("enter your name")
    speak("pls enter your name")
          



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
user = input()
def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak("the current Time is")
    speak(Time)
    if hour>=6 and hour<12:
        speak("Good Morning!" + user)
        speak ("iam your assistant JESSICA")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!" + user)
        speak ("iam your assistant JESSICA")

    elif hour>=18 and hour<24:
        speak("Good Evening !" + user)
        speak ("iam your assistant JESSICA")

    else:
        speak("Good Night!" + user)
        speak ("iam your assistant JESSICA")
        
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
   
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    
        
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry," + user)
        speak("can you repeat that again?")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Smartboy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
       
        elif 'open notepad' in query:
            notepadpath = "%windir%\system32\notepad.exe"
            os.startfile(notepad)
            engine = pyttsx3.init() 
            engine.say(command)  
            engine.runAndWait() 
      
        elif "hello" in query:
            speak("hello my dear how are you")
            

        elif "Why have you been created" in query:
            speak("I have been created for helping you")


        elif "thanks i am fine" in query:
            speak("i am very glad to hear that")

        elif "who are you" in query:
            speak("i am your gaming assistant")


        elif "how are you" in query:
            speak("i am fine thanks a lot")

                   
            
        elif "who made you"  in query: 
            speak("I have been created by WeGame team")
           
            
            
        elif "Help" in query: 
            speak("Use pistol when you are out of bullet")
            
         
            
        elif  "what is your name" in query: 
            speak("my name is JESSICA. i am your assistant")
            
            
            
        elif "shut up" in query:
            speak("Hey do not use offensive words.")


        elif "sorry" in query:
            speak ("no problem i love you gamer")


        elif "tell me something" in query:
            speak("you are the best gamer in the world")

        elif "do you have gender?" in query:
            speak("No.")


        elif "do you love me" in query:
            speak("ofcourse i love you because you are great gamer")

 
        elif "go away" in query:
            speak("no please gamer, I can not live without helping to the gamers")
        

        elif  "what do you think about me" in query: 
            speak("you are the best person i have ever met")

          
        elif "calculate" in query: 
              
            # write your wolframalpha app_id here 
            app_id = "TA5L4V-KPPGYA6GE4" 
            client = wolframalpha.Client('TA5L4V-KPPGYA6GE4') 
  
            indx = query.split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 
           
            
        
        
        elif 'bye' in query:
            speak("see you soon my love")
            exit()
            
                
        else :
            webbrowser.open(query)
            
