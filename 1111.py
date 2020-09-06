import pyttsx3 
import speech_recognition
from datetime import date
from datetime import datetime

def say(bot):
    bot_mouth = pyttsx3.init()
    bot_mouth.say(bot)
    bot_mouth.runAndWait()

def listen():
    global bot, you
    print("robot: i'm listening")
    bot=("i'm listening")
    say(bot)
    bot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        audio = bot_ear.listen(mic)
    try:
        you = bot_ear.recognize_google(audio)
        print("    ...   ")
        print("You:" + you)
    except:
        you = "..."

def brain(you):
    if "hello" in you:
        bot="Hello Khang"
    elif "time" in you:
        now = datetime.now()
        bot = now.strftime("%H : %M : %S")
    elif"today" in you:
        today=date.today()
        bot= today.strftime("%B %d, %Y")
    elif "how far" in you:
        if "from HaNoi to Ho Chi Minh city" in you:
            bot = "1722,8 km"
        elif "from Vietnam to America" in you:
            bot = "13789 km" 
        else:
            bot = "how far of what"
    elif "bye" in you:
        bot = "Goodbye Khang"
        print("robot: " + bot)
        say(bot)
        exit(0)        
    else:
        bot="i don't understand"
    print("robot: " + bot)
    say(bot)        
while True:
    listen()
    brain(you)
    
     