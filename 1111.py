import pyttsx3 
import speech_recognition
from datetime import date
from datetime import datetime
def brain(you):
    global bot
 
    if " hello "  in you:
        bot="Hello Khang"
    elif "time" in you:
        now = datetime.now()
        bot = now.strftime("%H : %M : %S")
    elif"today" in you:
        today=date.today()
        bot= today.strftime("%B %d, %Y")
    elif "how far" in you:
        if "from Ha Noi to Ho Chi Minh city" in you:
            bot = "1722,8 km"
        elif "from viet nam to america" in you :
            bot = "13789 km" 
        else:
            bot = "how far of what"
    else:
        bot="i don't understand"
while True:

    
    print("robot: i am listening")
    bot_mouth = pyttsx3.init()
    bot_mouth.say("i am listening")
    bot_mouth.runAndWait()
    you =input("You:")

    brain(you)
    if "bye" in you:
        bot= "Goodbye Khang"
        break
    print("robot: " + bot)
    bot_mouth = pyttsx3.init()
    bot_mouth.say(bot)
    bot_mouth.runAndWait()
    