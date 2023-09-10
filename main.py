from api_pull import *
from airports import *

import pandas as pd

amadeus = Client(
    client_id="uHWX60WOEvspw0npenxbLa9iW2RNbRyX",
    client_secret="fYGEGG0MAufIGki3"
)
airport_data = pd.read_csv('long_list.csv', names=['AirportID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude', 'Timezone', 'DST', 'TzDatabaseTimezone', 'Type', 'Source'])
userin_orig = input("Origin(city): ")
userin_dest = input("to(city): ")
orig_IATA = citytocode(userin_orig)
dest_IATA = citytocode(userin_dest)
date_depart = input("departure date(yyyy-mm-dd): ")
num_adult = input("Adults(int): ")

for orig in orig_IATA:
    if orig == "\\N":
        continue
    for dest in dest_IATA:
        if dest == "\\N":
            continue
        pull(orig, dest, date_depart, num_adult)
        