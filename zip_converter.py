class ZipLocation:
    def __init__(self, divided_info):
        self.zip = divided_info[0]
        self.latitude = divided_info[1]
        self.longitude = divided_info[2].translate({ord(i): None for i in ' \n'})


def zip_goes_brr(zip):
    input_file = open('US20Codes20201320Data.txt', 'r')

    for input_line in input_file:
        if input_line.startswith(zip[0]):
            if input_line.startswith(zip[1], 1):
                if input_line.startswith(zip[2], 2):
                    if input_line.startswith(zip[3], 3):
                        if input_line.startswith(zip[4], 4):
                            divided_info = input_line.split(",")
                            location = ZipLocation(divided_info)
                            input_file.close()
                            return location