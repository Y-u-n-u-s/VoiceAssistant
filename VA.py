import pyttsx3 #python text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5') #Used to get api for voices in windows
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id) #Voice of zira
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour) # gives us the current time
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal voice assistant. Please tell how may i help you")
def takeCommand():
    # It takes microphone input from the user and returns string object
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said {query}\n")
    except Exception as e:
        # print(e)
        print("Couldnt recognize")
        return "None"
    return query
# using smtplib
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','pwd')
    server.sendmail('yunus20122000@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'ok' in query:
            music_dir = 'D:\\video'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open visual code' in query:
            code_path = "C:\\Users\\91812\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'email to' in query:
            try:
                to = 'yunus201100@gmail.com'
                sendEmail(to,'anything')
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Cant send email")