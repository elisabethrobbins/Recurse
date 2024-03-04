import zip_converter
import holiday
import sunset

user_country = 'US'
zip = '33511'
requested = 'Independence Day'

location = zip_converter.zip_goes_brr(zip)
holiday = holiday.get_a_holiday(user_country, requested)
print(holiday.date)
sunset_time = sunset.sunset_getter(location, holiday)
print(sunset_time.sunset, sunset_time.time_zone, "UTC offset ", sunset_time.utc_offset)

# fixme add in a city option so can pick between city or zip. if 0-9 zip else city