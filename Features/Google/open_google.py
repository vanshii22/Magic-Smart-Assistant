import pyttsx3
import webbrowser
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak

def open_google():
    speak("Opening Google")
    print(f"Magic : Opening Google\n")
    webbrowser.open("google.com")