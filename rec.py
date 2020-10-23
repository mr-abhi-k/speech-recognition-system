import pyttsx3   #pip install pyttsx3
import speech_recognition  as sr#pip install Speechrecognition
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')# for window sapi5
voices = engine.getProperty('voices')#list of voices male/female

#print(voices[1.id])
engine.setProperty('voice', voices[1].id)#voice of david

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning!')
    
    elif(hour>=12 and hour<18):
        speak('Good Evening!')
    
    else:
        speak('Good Evening!')
        speak('I am Alka Sir,I serve for DARK SHADOW Please tell me how may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:#microphone for audio input
        print('Listening....')
        r.pause_threshold=1
        r.energy_threshold=300 
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:
            print('Recognizing....')
            query =r.recognize_google(audio, language='en-us')
            print(f'User Said :{query}\n')
        
        except Exception as e:
            print(e)
            print('Say that again please...')
            query=takeCommand().lower()
            return query;
        
        return query;

if __name__== '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'your name' in query:
            speak('I am Jarvis')
        
        elif 'who are you' in query:
            speak('I am Alka living with Dark Shadow')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query =query.replace('Wikipedia', '')
            results =wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {strTime}')
            
        elif 'open code' in query:
            codePath ="C:\\Program Files\\Microsoft VS Code"
            os.startfile(codePath)
        
        elif 'open song' in query:
            music_dir=""
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,3)]))

        elif 'add' in query:
            speak('Enter First no:')
            num1=float(input("Enter first nO:"))
            speak('Enter second no: ')
            num2 =float(input("Enter Secong no:"))
            print(f'Sum={num1+num2}')
            speak(f' The addition of {num1} and {num2} is {num1+num2}')