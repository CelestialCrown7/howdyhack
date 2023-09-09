from amadeus import Client, ResponseError

# User inputs, (cities of origin and destination, etc)
origin_location = "AUS"
dest_locations = ["SYD", "PAR", "MEX"]
departure_date = '2023-09-10'
adults = 1

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
            print(response.data[i])
            print()

    except ResponseError as error:
        print(error)