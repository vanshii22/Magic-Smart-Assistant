import datetime
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 

def date(*args, **kwargs):
    """
    Just return date as string
    :return: date if success, False if fail
    """
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    speak(date)
    return date


def time(*args, **kwargs):

    try:
        time = datetime.datetime.now().strftime("%H:%M")
    except Exception as e:
        print(e)
        time = False
    speak(time)
    return time

