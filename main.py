from scripts.zip_converter import zip_dictionary
from scripts.holiday import get_holidays
from scripts.sunset import sunset_getter
from scripts.custom_dates import custom_date_maker
from scripts.tester import custom_date_tester_name, custom_date_tester_date

# fixme add in a city option so can pick between city or zip. if 0-9 zip else city

# location
user_country = 'US'
zip = '33511'
coordinates = zip_dictionary()[zip]

# user customizable values
name = ''
date = ''
year = ''
notification_buffer = 0     # how many minutes before event
days_selected = []
requested_list = ['Christmas Day', 'Independence Day', 'Good Friday']   # list of requested dates, inc custom dates

holidays_dictionary = get_holidays(user_country, year)      # show all public holidays available from API for country

user_date = custom_date_maker(custom_date_tester_name(), custom_date_tester_date())
requested_list.append(user_date.name)
holidays_dictionary.update({user_date.name: user_date.date})


for each in requested_list:
    requested = each
    date = holidays_dictionary[requested]

    sunset_time = sunset_getter(coordinates, date)
    print(f'The sun will set on {requested} ({date}) at {sunset_time.sunset} {sunset_time.time_zone} '
          f'(UTC offset {sunset_time.utc_offset})')

# print(holidays_dictionary, requested_list)