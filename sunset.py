import requests

# https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873&timezone=UTC&date=1990-05-22
# fixme must link to the website if use this api    https://sunrisesunset.io/api/


class SunsetZone:
    def __init__(self, sunset, time_zone, utc_offset):
        self.sunset = sunset
        self.time_zone = time_zone
        self.utc_offset = utc_offset


def sunset_getter(location, holiday):
    latitude = location.latitude
    print(latitude)
    longitude = location.longitude
    print(longitude)
    url = f'https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}&date={holiday.date}'
    response = requests.get(url)
    sunset_data = response.json()
    # print("line 20")
    sunset = sunset_data['results']['sunset']
    time_zone = sunset_data['results']['timezone']
    utc_offset = sunset_data['results']['utc_offset']
    sunset_time = SunsetZone(sunset, time_zone, utc_offset)

    return sunset_time