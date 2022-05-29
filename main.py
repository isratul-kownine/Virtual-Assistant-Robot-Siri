 import pyjokes
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import pyjokes
import randfacts
from weather import *
import datetime


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):

    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return("morning")
    elif hour >= 12 and hour < 16:
        return("afternoon")
    else:
        return("evening")


today_date= datetime.datetime.now()

r = sr.Recognizer()

speak("Hello, good " +wishme()+ ", i'm your voice assistant , siri.")
print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And It's currently " + (today_date.strftime("%I")) + "." + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And It's currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
print(" And Today the temperature in Chittagong is " + str(temp())+ " degree celcius " +  str(des()))
speak(" And Today the temperature in Chittagong is " + str(temp())+ " degree celcius " +  str(des()))
speak("How are you Today")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening..")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text :
    speak("I am also having a good day")
    speak("What can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic?")


    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

        assist = infow()

        print("Searching {} in wikipedia".format(infor))
        speak("Searching {} in wikipedia".format(infor))
        assist.get_info(infor)

elif "play" and "video" in text2:
    speak("Which video you want me to play?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure, I will read news for you.")
    speak("Sure, I will read news for you.")
    arr=news()
    for i in range(len(arr)):
         print(arr[i])
         speak(arr[i])

# elif "joke" or "jokes" in text2:
#     speak("Sure, get ready for some fun")
#     y=pyjokes.get_joke()
#     print(y)
#     speak(y)

elif "fact" or "facts" in text2:
    speak("Sure")
    x= randfacts.get_fact()
    print(x)
    speak("Did you know that,"+x)
