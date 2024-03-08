class CustomDate:
    def __init__(self, name, date):
        self.name = name
        self.date = date


def custom_date_maker(name, date):
    if date == '':
        print('No date provided')
        return None
    elif name == '':
        name = 'Custom date'
        custom_date = CustomDate(name, date)
        return custom_date
    else:
        custom_date = CustomDate(name, date)
        return custom_date
