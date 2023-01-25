# ======= Main Module Import ======
import pyttsx3
from time import ctime
import playsound
import speech_recognition as sr
import os
import sys
import random

# ========= Services Module Import =====
from Services.Speech_control.speech_control import speak
from Services.Greeting.greeting import greet
from Services.Recognition.recognition import recognze

# ========= Features Module Import =====
from Features.Screenshot.screenshot import take_screenshot
from Features.Jokes.jokes import tell_me_joke
from Features.Date_time.date_time import date, time
from Features.Video_download.video_download import download_yt_video
from Features.News.news import news, show_me_some_tech_news, show_me_some_tech_videos
from Features.Games.game import play_games
from Features.Picture.picture import click_pic
from Features.Covid.covid import covid_cases
# from Features.Internet_speed.internet_speed import speed_test
from Features.Day.day import tellDay
from Features.Google.open_google import open_google
from Features.Youtube.open_youtube import open_youtube
from Features.Wikipedia.Wikipedia_search import wikipedia_search

# Support for regular expressions (RE). Hover mouse cursor over re to learn more about it
import re
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import platform
from PySide2.QtWidgets import * 
from PyQt5.QtCore import * 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

# ============UI Import=========
from ui_app import Ui_MainWindow
UI = Ui_MainWindow()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello Magic", "Magic", "wake up Magic", "you there Magic", "time to work Magic", "hey Magic",
             "ok Magic", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

# This is the main thread
class LandingThread(QThread):
    def __init__(self):
        super(LandingThread, self).__init__()

    def run(self):
        self.introFunction()

    def introFunction(self):
        # pass
        speak("Welcome to this Application")
        speak("I am your personal voice assistent") 
        speak("I am here to assist you to use this app easily")
        # time.sleep(0.5)
        speak("if you want to work with me,then clicked on Start button") 
        speak("or click on Stop button to terminate Me")
        # time.sleep(0.5)
        speak("to know more about me click on about button") 
        # time.sleep(1)
        speak("to hear again click on the help button")
    
    def aboutFunction(self):
        # pass
        speak("I am Magic, Your Assistent to use this Application.")
        speak("I am developed by, Vanshika Sharma and Nashra Ali") 
        # time.sleep(0.5)
        speak("I will be assisting you in few tasks like,")
        speak("doing google search")
        # time.sleep(0.2)
        speak("opening any software")
        # time.sleep(0.2)
        speak("and a lot more.")
        # time.sleep(0.5)

# This is the main thread
class AboutThread(QThread):
    def __init__(self):
        super(AboutThread, self).__init__()

    def run(self):
        self.aboutFunction()

    def aboutFunction(self):
        speak("I am Magic, Your Assistent to use this Application.")
        speak("I am developed by, Vanshika Sharma and Nashra Ali") 
        # time.sleep(0.5)
        speak("I will be assisting you in few tasks like,")
        speak("doing google search")
        # time.sleep(0.2)
        speak("opening any software")
        # time.sleep(0.2)
        speak("and a lot more.")
        # time.sleep(0.5)


LandingStartExecution = LandingThread()
AboutStartExecution = AboutThread()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.taskExecution()

    def taskExecution(self):
        from Services.Greeting.greeting import greet
        from Services.Recognition.recognition import recognze
        greet()
        while True:
            # if 1:
            query = recognze().lower()

            if query in GREETINGS:
                greet = random.choice(GREETINGS_RES)
                speak(f"{greet}")

            elif 'from wikipedia' in query:
                wikipedia_search(query)

            elif 'youtube' in query:
                open_youtube()

            elif 'google' in query:
                open_google()

            elif 'screenshot' in query:
                take_screenshot(1)

            elif 'joke' in query:
                tell_me_joke()

            elif 'date' in query:
                date()

            elif 'time' in query:
                time()

            elif 'download video' in query:
                download_yt_video(1)

            elif 'tell me a news' in query:
                speak(news())

            elif 'tech news' in query:
                show_me_some_tech_news()

            elif 'tech video' in query:
                show_me_some_tech_videos()

            elif 'game' in query:
                play_games(1)

            elif 'picture' in query or 'photo' in query:
                click_pic(1)

            elif 'covid' in query:
                covid_cases(query)

            elif 'internet speed' in query or 'internet speed check' in query:
                speed_test(1)

            elif 'day' in query:
                tellDay()
            
            elif 'quit' in query or 'bye' in query or 'terminate' in query:
                speak("OKay bye Sir, I am terminating myself in three seconds")
                speak("three")
                speak("two")
                speak("one")
                speak("GOODBye")
                quit()



startExecution = MainThread()

# This is the main class
class Landing(QMainWindow):
    def __init__(self):
        super().__init__()
        UI.setupUi(self)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main window to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        # Apply shadow to cental widget
        UI.centralwidget.setGraphicsEffect(self.shadow)
    
        # --------------------- Set window Icon
        self.setWindowIcon(QtGui.QIcon("icons/bot-logo.png"))
        self.setWindowTitle("MAGIC - Your Personal Assistant")

        # start button functionality
        UI.Btn_START.clicked.connect(self.startTask)

        LandingStartExecution.start()

        #----------------- Close window
        UI.Btn_CLOSE.clicked.connect(lambda: self.close())

        # Setting GIFs
        UI.movie = QtGui.QMovie("gif\\9.gif")
        UI.gif_9.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\robo1.gif")
        UI.gif_3.setMovie(UI.movie)
        UI.movie.start()

        UI.copyright.setText(u"Copyright "+"\u00A9"+" 2023 Magic - Your Smart Assistant | Developed by Vanshika Sharma and Nashra Ali")

        UI.Btn_ABOUT.clicked.connect(self.speakIntro)
        UI.Btn_HELP.clicked.connect(self.startLandingIntro)

        UI.Btn_STOP.clicked.connect(lambda: self.close()) 

    #This function is for running GUIs or GIFs
    def startLandingIntro(self):
        LandingStartExecution.start()

    def speakIntro(self):
        AboutStartExecution.start()
 

    def startTask(self):
        speak('I am ready sir')
        startExecution.taskExecution()
        


app = QApplication(sys.argv)
landing_page = Landing()
landing_page.show()
exit(app.exec_())



