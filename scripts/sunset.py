import requests
# fixme must link to the website if use this api    https://sunrisesunset.io/api/


class SunsetZone:
    def __init__(self, sunset, time_zone, utc_offset):
        self.sunset = sunset
        self.time_zone = time_zone
        self.utc_offset = utc_offset


def sunset_getter(coordinates, date):
    url = f'https://api.sunrisesunset.io/json?lat={coordinates[0]}&lng={coordinates[1]}&date={date}'
    response = requests.get(url)
    sunset_data = response.json()
    sunset = sunset_data['results']['sunset']
    time_zone = sunset_data['results']['timezone']
    utc_offset = sunset_data['results']['utc_offset']   # is this amount correct?
    sunset_time = SunsetZone(sunset, time_zone, utc_offset)
    return sunset_time