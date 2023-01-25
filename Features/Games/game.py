import webbrowser
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 

def play_games(inp_command):
    speak('here you can play games, which ever you want play.')
    url = 'https://poki.com/'
    try:
        webbrowser.open(url)
        return "Successfully opened Poki.com, Play your games!"
    except Exception as e:
        print(e)
        return "Failed to open Poki.com, please try again!"


# if __name__ == '__main__':
#     play_games('inp_command')