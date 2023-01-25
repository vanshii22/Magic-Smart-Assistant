import pyttsx3
import webbrowser
import wikipedia
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak

def wikipedia_search(command):
    speak("Searching the wikipedia ")
    command = command.replace("wikipedia", "")
    result = wikipedia.summary(command, sentences=4)
    speak("According to wikipedia")
    speak(result)

# wikipedia_search("Salman Khan on Wikipedia")