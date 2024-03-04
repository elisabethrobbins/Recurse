# limited by free APIs and Recurse guideline to avoid frameworks
# API in use only provides public holidays, not religious and/or cultural holidays

import requests
import datetime     # https://docs.python.org/3/library/datetime.html#format-codes


class Holiday():
    def __init__(self, name, date):
        self.name = name
        self.date = date


def get_holidays(user_country):
    url = f'https://date.nager.at/api/v3/NextPublicHolidays/{user_country}'
    response = requests.get(url).json()

    i = 0
    for each in response:
        date = response[i]['date']
        if date[5] == '0':
            date = date[6:]
        else:
            date = date[5:]

        if response[i]['localName'] == 'Veterans Day':
            print("Halloween: 10-31")
        if response[i]['localName'] == "New Year's Day":
            print("New Year's Eve: 12-31")
        print('{}: {}'.format(response[i]['localName'], date))
        i += 1


    # "name": "Super Bowl Sunday"
    # "name": "Saint Patrick's Day"
    # "name": "Cinco de Mayo"
    # "name": "Memorial Day"
    # "name": "Independence Day"
    # "name": "Bastille Day"
    # "name": "Labor Day"
    # "name": "Halloween"
    # "name": "New Year's Eve"
    # Lunar New Year, Chinese New Year, Spring Festival
    # guy fawks day?
    # diwali
    # mardi gras
    # gasparilla
    # non holiday fireworks from theme parks


def get_a_holiday(user_country, requested):
    year = datetime.date.today().year
    url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{user_country}'
    response = requests.get(url).json()
    i = 0
    found = False

    while not found:
        if response[i]['localName'] == requested:
            holiday = Holiday(requested, response[i]['date'])
            return holiday
        else:
            i += 1