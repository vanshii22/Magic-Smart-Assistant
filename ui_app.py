from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1367, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(31, 81, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_Navigation = QFrame(self.frame)
        self.frame_Navigation.setObjectName(u"frame_Navigation")
        self.frame_Navigation.setMinimumSize(QSize(0, 40))
        self.frame_Navigation.setMaximumSize(QSize(16777215, 40))
        self.frame_Navigation.setStyleSheet(u"background-color: rgb(12, 12, 12);\n"
"")
        self.frame_Navigation.setFrameShape(QFrame.StyledPanel)
        self.frame_Navigation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_Navigation)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Icon = QFrame(self.frame_Navigation)
        self.frame_Icon.setObjectName(u"frame_Icon")
        self.frame_Icon.setMinimumSize(QSize(0, 40))
        self.frame_Icon.setMaximumSize(QSize(0, 40))
        self.frame_Icon.setFrameShape(QFrame.StyledPanel)
        self.frame_Icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_Icon)

        self.frame_app_name = QFrame(self.frame_Navigation)
        self.frame_app_name.setObjectName(u"frame_app_name")
        self.frame_app_name.setFrameShape(QFrame.StyledPanel)
        self.frame_app_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_app_name)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.App_name = QLabel(self.frame_app_name)
        self.App_name.setObjectName(u"App_name")
        font = QFont()
        font.setPointSize(10)
        self.App_name.setFont(font)

        self.verticalLayout_13.addWidget(self.App_name, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_app_name, 0, Qt.AlignLeft)

        self.frame_controls_2 = QFrame(self.frame_Navigation)
        self.frame_controls_2.setObjectName(u"frame_controls_2")
        self.frame_controls_2.setFrameShape(QFrame.StyledPanel)
        self.frame_controls_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_controls_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
#         self.Btn_MINIMISE = QPushButton(self.frame_controls_2)
#         self.Btn_MINIMISE.setObjectName(u"Btn_MINIMISE")
#         self.Btn_MINIMISE.setMinimumSize(QSize(50, 30))
#         self.Btn_MINIMISE.setCursor(QCursor(Qt.PointingHandCursor))
#         self.Btn_MINIMISE.setStyleSheet(u"QPushButton {\n"
# "	color: rgb(255, 255, 255);\n"
# "	background-color: rgb(45, 45, 45);\n"
# "	border: 0px solid;\n"
# "}\n"
# "QPushButton:hover{\n"
# "	background-color: rgb(90,90,90);\n"
# "}")
#         icon = QIcon()
#         icon.addFile(u"icons/minimize-white.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.Btn_MINIMISE.setIcon(icon)
#         self.Btn_MINIMISE.setFlat(True)

#         self.horizontalLayout_4.addWidget(self.Btn_MINIMISE)

#         self.Btn_MAXIMISE = QPushButton(self.frame_controls_2)
#         self.Btn_MAXIMISE.setObjectName(u"Btn_MAXIMISE")
#         self.Btn_MAXIMISE.setMinimumSize(QSize(50, 30))
#         self.Btn_MAXIMISE.setCursor(QCursor(Qt.PointingHandCursor))
#         self.Btn_MAXIMISE.setStyleSheet(u"QPushButton {\n"
# "	color: rgb(255, 255, 255);\n"
# "	background-color: rgb(45, 45, 45);\n"
# "	border: 0px solid;\n"
# "}\n"
# "QPushButton:hover{\n"
# "	\n"
# "	background-color: rgb(90, 90, 90);\n"
# "}")
#         icon1 = QIcon()
#         icon1.addFile(u"icons/expand-white.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.Btn_MAXIMISE.setIcon(icon1)
#         self.Btn_MAXIMISE.setFlat(True)

        # self.horizontalLayout_4.addWidget(self.Btn_MAXIMISE)

        self.Btn_CLOSE = QPushButton(self.frame_controls_2)
        self.Btn_CLOSE.setObjectName(u"Btn_CLOSE")
        self.Btn_CLOSE.setMinimumSize(QSize(50, 30))
        self.Btn_CLOSE.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_CLOSE.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/close-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_CLOSE.setIcon(icon2)
        self.Btn_CLOSE.setIconSize(QSize(12, 12))
        self.Btn_CLOSE.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Btn_CLOSE)


        self.horizontalLayout.addWidget(self.frame_controls_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_Navigation)

        self.frame_center = QFrame(self.frame)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(0, 0))
        self.frame_center.setMaximumSize(QSize(16777215, 16777215))
        self.frame_center.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_center)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_Welcome = QFrame(self.frame_center)
        self.frame_Welcome.setObjectName(u"frame_Welcome")
        self.frame_Welcome.setMinimumSize(QSize(0, 120))
        self.frame_Welcome.setMaximumSize(QSize(16777215, 120))
        self.frame_Welcome.setStyleSheet(u"")
        self.frame_Welcome.setFrameShape(QFrame.StyledPanel)
        self.frame_Welcome.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Welcome)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_Welcome)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Calibri Light")
        font1.setPointSize(50)
        font1.setKerning(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.gif_9 = QLabel(self.frame_4)
        self.gif_9.setObjectName(u"gif_9")
        self.gif_9.setMinimumSize(QSize(120, 0))
        self.gif_9.setMaximumSize(QSize(120, 16777215))
        self.gif_9.setPixmap(QPixmap(u"gif/9.gif"))
        self.gif_9.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.gif_9)

        self.horizontalSpacer_2 = QSpacerItem(249, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.gif_9.raise_()
        self.label.raise_()

        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_Welcome)

        self.frame_About = QFrame(self.frame_center)
        self.frame_About.setObjectName(u"frame_About")
        self.frame_About.setMinimumSize(QSize(0, 0))
        self.frame_About.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setKerning(True)
        self.frame_About.setFont(font2)
        self.frame_About.setFrameShape(QFrame.StyledPanel)
        self.frame_About.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_About)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 50, 400, 250))
        self.label_3.setStyleSheet(u"border-top:1px solid;\n"
"border-left:1px solid;\n"
"border-right:0px solid;\n"
"border-bottom:0px solid;\n"
"border-color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Btn_ABOUT = QPushButton(self.frame_About)
        self.Btn_ABOUT.setObjectName(u"Btn_ABOUT")
        self.Btn_ABOUT.setGeometry(QRect(80, 30, 101, 41))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.Btn_ABOUT.setFont(font3)
        self.Btn_ABOUT.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_ABOUT.setStyleSheet(u"QPushButton {\n"
"	color: rgb(85, 170, 255);\n"
"	background-color: rgb(12, 12, 12);\n"
"	border: 1px solid;\n"
"	border-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_4 = QLabel(self.frame_About)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 100, 291, 151))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.gif_3 = QLabel(self.frame_About)
        self.gif_3.setObjectName(u"gif_3")
        self.gif_3.setGeometry(QRect(920, 50, 365, 250))
        self.gif_3.setPixmap(QPixmap(u"gif/3.gif"))
        self.gif_3.setScaledContents(True)
        self.Btn_HELP = QPushButton(self.frame_About)
        self.Btn_HELP.setObjectName(u"Btn_HELP")
        self.Btn_HELP.setGeometry(QRect(1270, 0, 65, 35))
        self.Btn_HELP.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_HELP.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 85, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_About)

        self.frame_buttons = QFrame(self.frame_center)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMinimumSize(QSize(0, 150))
        self.frame_buttons.setMaximumSize(QSize(16777215, 150))
        self.frame_buttons.setStyleSheet(u"background-color: rgb(12, 12, 12);")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_5 = QSpacerItem(453, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.frame_register = QFrame(self.frame_buttons)
        self.frame_register.setObjectName(u"frame_register")
        self.frame_register.setMinimumSize(QSize(225, 150))
        self.frame_register.setMaximumSize(QSize(225, 150))
        self.frame_register.setFrameShape(QFrame.StyledPanel)
        self.frame_register.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_register)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 10, 131, 31))
        font4 = QFont()
        font4.setPointSize(15)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Btn_START = QPushButton(self.frame_register)
        self.Btn_START.setObjectName(u"Btn_START")
        self.Btn_START.setGeometry(QRect(20, 60, 150, 50))
        font5 = QFont()
        font5.setPointSize(13)
        self.Btn_START.setFont(font5)
        self.Btn_START.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_START.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 170, 0);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_5.addWidget(self.frame_register, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_login = QFrame(self.frame_buttons)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMinimumSize(QSize(225, 150))
        self.frame_login.setMaximumSize(QSize(225, 150))
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_login)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 10, 211, 31))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Btn_STOP = QPushButton(self.frame_login)
        self.Btn_STOP.setObjectName(u"Btn_STOP")
        self.Btn_STOP.setGeometry(QRect(50, 60, 150, 50))
        self.Btn_STOP.setFont(font5)
        self.Btn_STOP.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_STOP.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 49, 49);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 49, 49);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 49, 49);\n"
"}")

        self.horizontalLayout_5.addWidget(self.frame_login, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_6 = QSpacerItem(452, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_buttons)


        self.verticalLayout_4.addWidget(self.frame_center)

        self.frame_bottom = QFrame(self.frame)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(0, 50))
        self.frame_bottom.setMaximumSize(QSize(16777215, 50))
        self.frame_bottom.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(594, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.copyright = QLabel(self.frame_bottom)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setFont(font)
        self.copyright.setStyleSheet(u"color: rgb(207, 207, 207);")

        self.horizontalLayout_3.addWidget(self.copyright)

        self.horizontalSpacer_4 = QSpacerItem(594, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.App_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; color:#00ff00;\">FAMS - Facial Recognition Attendance Management System-</span><span style=\" color:#f1f1f1;\"> Landing page</span></p></body></html>", None))
        # self.Btn_MINIMISE.setText("")
        # self.Btn_MAXIMISE.setText("")
        self.Btn_CLOSE.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">Welcome to the World of MAGIC</span></p></body></html>", None))
        self.gif_9.setText("")
        self.label_3.setText("")
        self.Btn_ABOUT.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#55aaff;\">I am Magic, Your Virtual Assistant.</span></p><p><span style=\" font-size:8pt; color:#55aaff;\">I am developed by Vanshika Sharma </span></p><p><span style=\" font-size:8pt; color:#55aaff;\"> and Nashra Ali.</span></p><p><span style=\" font-size:8pt; color:#55aaff;\">I will be assisting you in few tasks like, </span></p><p><span style=\" font-size:8pt; color:#55aaff;\">-&gt; doing google search</span></p><p><span style=\" font-size:8pt; color:#55aaff;\">-&gt; opening any software and a lot more..</span></p><p><span style=\" font-size:11pt; color:#55aaff; vertical-align:sub;\"><br/></span></p></body></html>", None))
        self.gif_3.setText("")
        self.Btn_HELP.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        # self.label_5.setText(QCoreApplication.translate("MainWindow", u"New User ?", None))
        self.Btn_START.setText(QCoreApplication.translate("MainWindow", u"START", None))
        # self.label_6.setText(QCoreApplication.translate("MainWindow", u"Already Registered ?", None))
        self.Btn_STOP.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.copyright.setText(QCoreApplication.translate("MainWindow", u"Copyright message here", None))
    # retranslateUi

