import requests
import pycountry
import sys

sys.path.append(r'Services\Speech_control')

# ========= Services Module Import =====
from speech_control import speak


def covid_cases(command):
    try:
        command = command.title()
        country = get_country(command)
        cases = get_covid_cases(country)
        total = f"The current active cases in {country} are {cases}"
        speak(total)
        return total
    except Exception as e:
        print("Error: ", e)
        return "Sorry, I couldn't find the country you are looking for. Or server is down."


def get_country(command):  # For getting only the country name for the whole query
    for country in pycountry.countries:
        if country.name in command:
            return country.name


def get_covid_cases(country):  # For getting current covid cases
    totalActiveCases = 0
    response = requests.get('https://api.covid19api.com/live/country/' + country + '/status/confirmed').json()
    for data in response:
        totalActiveCases += data.get('Active')
    return totalActiveCases


# if __name__ == '__main__':
#     print(covid_cases('active Covid India cases?'))  