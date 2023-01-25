import pyscreenshot
import os
import datetime
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 

def take_screenshot(inp_command):
    speak("Taking Screenshot")

    try:
        image = pyscreenshot.grab()
        image.show()
        a = datetime.datetime.now()
        if not os.path.exists("screenshot"):
            os.mkdir("screenshot")
        image.save(f"screenshot/{a.day, a.month, a.year}_screenshot.png")
        print(f"Screenshot taken: screenshot/{a.day, a.month, a.year}_screenshot.png ")
        return f"Screenshot taken"
    except Exception as e:
        print(e)
        return "Unable to take screenshot"


# if __name__ == "__main__":
#     take_screenshot(1)