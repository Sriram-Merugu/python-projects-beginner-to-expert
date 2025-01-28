import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("The current time is ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    speak("Current date is ")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir! ")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good AfterNoon sir")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good Night Sir")
    speak("Jarvis at your shoes. Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Please repeat sir")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("YOUR MAIL", "YOUR PASSWORD")
    server.sendmail('YOUR MAIL', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("PATH TO SAVE THE IMAGE" + ".png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)


        elif 'send email' in query:
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = 'SEND MAIL'
                sendemail(to, content)
                speak("Email has been sent! ")
            except Exception as e:
                print(e)
                speak("Unable to send the email sir")



        elif 'offline' in query:
            speak("Jarvis signing off bye sir")
            quit()
        elif 'chrome' in query:
            try:
                speak("What should I search ? ")
                chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe" # YOUR CHROME PATH
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + '.com')
                speak("search successfull")
            except Exception as e:
                print(e)
                speak("Could not execute the query sir")
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play songs' in query:
            songs_dir = "music file location"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remeber ?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open("data.txt", 'r')
            speak("You said me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Taking Screen Shot sir")
        elif 'cpu' in query:

            speak("Fetching CPU details")
            cpu()
