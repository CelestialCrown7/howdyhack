from amadeus import Client, ResponseError

# User inputs, (cities of origin and destination, etc)
origin_location = "AUS"
dest_locations = ["SYD"] #["SYD", "PAR", "MEX"]
departure_date = '2023-09-10'
adults = 1


print("Searching for the cheapest round-trip flights from", origin_location, "to", dest_locations, "\n")

amadeus = Client(
    client_id="uHWX60WOEvspw0npenxbLa9iW2RNbRyX",
    client_secret="fYGEGG0MAufIGki3"
)

# find cheapest flights for each location
for location in dest_locations:
    try:
        print("Destination (IATA):", location, "\n")
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin_location,
            destinationLocationCode=location,
            departureDate=departure_date,
            adults=adults
        )

        # show 3 flights per place
        for i in range(3):
            '''
            for key, val in response.data[i].items():
                print(key, ":", val)
            '''
            print("Option", (i+1), "to", location, "\n")

            flight_info = response.data[i]
            itineraries = flight_info["itineraries"][0]

            total_duration = itineraries["duration"][2:] # ignores the 2 letters PT before the total time (idk what PT is)
            print("Total duration:", total_duration, "\n")

            print("Flights in route:\n")
            segments = itineraries["segments"] # all the flights (segments) required to reach the destination
            segment = 1
            for flight in segments:
                print(str(segment) + ".")
                for k, v in flight.items():
                    print(k, ":", v)
                segment += 1
                print()

            print("Pricing breakdown:")
            price_list = flight_info["price"]
            for k, v in price_list.items():
                print(k, ":", v)
            print()

            print()

    except ResponseError as error:
        print(error)


# TODO: put other input parameters like what airlines
# find useful tags in data
# airport/airline code to actual
