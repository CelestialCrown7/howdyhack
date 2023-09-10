from amadeus import Client, ResponseError
import pprint

# User inputs, (cities of origin and destination, etc)
#origin_location = input("Origin (IATA) ? ")
#dest_location = input("Destination (IATA) ? ")
#departure_date = input("Date of Departure (yyyy-mm-dd)? ")
#adults = input("Number of Adults (int)?")

amadeus = Client(
    client_id="uHWX60WOEvspw0npenxbLa9iW2RNbRyX",
    client_secret="fYGEGG0MAufIGki3"
)

# find cheapest flights for each location

def pull(origin_location, dest_location, departure_date, adults):
        
        try:
            #print("Destination (IATA):", dest_location, "\n")
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_location,
                destinationLocationCode=dest_location,
                departureDate=departure_date,
                adults=adults
            )
            if len(response.data) == 0:
                return
            # show 3 flights per place
            print("Searching for the cheapest one-way flights from", origin_location, "to", dest_location, "\n")
            for i in range(2):
                '''
                for key, val in response.data[i].items():
                    print(key, ":", val)
                '''
                print("Option", (i+1), "to", dest_location, "\n")

                try:
                    flight_info = response.data[i]
                except:
                    print(f"no more flights found for {origin_location} to {dest_location}")
                    break
                itineraries = flight_info["itineraries"][0]

                total_duration = itineraries["duration"][2:] # ignores the 2 letters PT before the total time (idk what PT is)
                print("Total duration:", total_duration, "\n")

                print("Flights in route:\n")
                segments = itineraries["segments"] # all the flights (segments) required to reach the destination
                segment = 1
                for flight in segments:
                    print(str(segment) + ".")
                    for item in flight.items():
                        if item[0] == "arrival" or item[0] == "departure":
                            print(item[0], item[1])
                        
                    segment += 1
                    
                    print()

                #print("Pricing breakdown:")
                price_list = flight_info["price"]
                print(f"{flight_info['price']['grandTotal']} {flight_info['price']['currency']}")
                """for k, v in price_list.items():
                    if k == "currency" :
                         print(k, ":", v)
                    if k == "grandTotal" :
                        print(k, ":", v)
                    if k == "arrival": #break after printing relevant info
                         break
                print()"""

                print()

        except ResponseError as error:
            print(error)

#pull("HOU", "DAL", "2023-09-11", "1")
# TODO: put other input parameters like what airlines
# find useful tags in data
# airport/airline code to actual