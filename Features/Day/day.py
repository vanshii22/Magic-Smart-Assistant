import pyttsx3
import datetime
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak 

def tellDay():

	day = datetime.datetime.today().weekday() + 1

	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)