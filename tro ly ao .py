import pyttsx3 
import speech_recognition

bot_ear = speech_recognition.Recognizer()
bot_mouth = pyttsx3.init()
bot = ""

with speech_recognition.Microphone() as mic:
    audio = bot_ear.listen(mic)

print("robot: ...")

try:
    you = bot_ear.recognize_google(audio)
except:
    you = "..." 

print("You:" + you)

if you=="Hello":
    bot="Hello Khang"
elif you=="What time is it":
    bot=""

print("robot: " + bot)
bot_mouth.say(bot)
bot_mouth.runAndWait()