import pyttsx3
import webbrowser
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak

def open_youtube():
    speak("Opening Youtube")
    print(f"Magic : Opening Google\n")
    webbrowser.open("youtube.com")