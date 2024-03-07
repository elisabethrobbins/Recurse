import zip_converter
import holiday
import sunset

# fixme add in a city option so can pick between city or zip. if 0-9 zip else city

user_country = 'US'
zip = '33511'
requested = 'Good Friday'
year = ''
holidays_dictionary = holiday.get_holidays(user_country, year)
date = holidays_dictionary[requested]
coordinates = zip_converter.zip_dictionary()[zip]
sunset_time = sunset.sunset_getter(coordinates, date)

print(f"The sun will set on {requested} ({date}) at {sunset_time.sunset} "
      f"{sunset_time.time_zone} UTC offset {sunset_time.utc_offset}")