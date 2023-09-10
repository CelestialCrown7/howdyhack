"""This program takes one city name as input (not case sensitive) and outputs a 
    list of airports in IATA form in that city. We need to feed these airports one at a time
    to the API pull """

import pandas as pd
airport_data = pd.read_csv('long_list.csv', names=['AirportID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude', 'Timezone', 'DST', 'TzDatabaseTimezone', 'Type', 'Source'])
#print(airport_data.head(5)) (debugging)
# print(airport_data[airport_data['City'] == "Houston"])
# print(airport_data.City.value_counts())
def citytocode(citname): 
    match_cities = airport_data[airport_data['City'].str.contains(citname, case=False, na=False)]
    
    if not match_cities.empty:
        iata_codes = match_cities['IATA'].tolist()
        return iata_codes
    else:
        return None
    
user_in = input("cityname: ") #placeholder

print(citytocode(user_in)) #placeholder
