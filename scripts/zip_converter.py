def zip_dictionary():
    input_file = open('scripts/US20Codes20201320Data.txt', 'r')
    zipcode_dictionary = {}
    for input_line in input_file:
        divided_info = input_line.split(",")
        lat_long = [divided_info[1], divided_info[2].translate({ord(i): None for i in ' \n'})]
        zipcode_dictionary.update({f"{divided_info[0]}": lat_long})
    input_file.close()
    return zipcode_dictionary