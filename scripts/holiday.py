# limited by free APIs and Recurse guideline to avoid frameworks
# API in use only provides public holidays, not religious and/or cultural holidays
import requests


def get_holidays(user_country, year):
    if year == '':
        url = f'https://date.nager.at/api/v3/NextPublicHolidays/{user_country}'
    else:
        url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{user_country}'
    response = requests.get(url).json()
    i = 0
    dictionary = {}
    for line in response:
        key = response[i]['localName']
        value = response[i]['date']
        dictionary.update({key: value})
        i += 1
    return dictionary


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