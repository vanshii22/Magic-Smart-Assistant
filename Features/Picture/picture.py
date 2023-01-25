import datetime
import cv2
import os
import time
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak


def click_pic(inp_command):
    try:
        speak('I am helping you, to taking a pictureof you.')
        t = datetime.datetime.now()
        camera = cv2.VideoCapture(0)
        for i in range(20):
            return_value, image = camera.read()
        if not os.path.exists("photos"):
            os.mkdir("photos")
        cv2.imwrite(f"photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png", image)
        del camera
        print(f"Photo taken: photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png")
        return "Photo taken"
    except Exception as e:
        return "Error: " + str(e) + "\n Unable to take photo"


# if __name__ == "__main__":
#     click_pic(1)