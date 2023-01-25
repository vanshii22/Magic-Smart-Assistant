import pyttsx3
import datetime
import sys
sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("My name is Magic, A voice Assistant and")
    speak("I am your voice assistant. Please tell me how may I help you ")
# greet()