import pyttsx3
import speech_recognition as sr
import sys
sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 

def recognze():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")

    except Exception as e:
        print(e)
        print("Could not recognze your voice.....")
        print("Say it again please...")
        return "None"
    return query
# recognze()