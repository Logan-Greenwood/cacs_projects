destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA",
                "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# could be done more ea
def get_destination_index(destination):
    destination_index = -1
    for i in destinations:
        destination_index +=1
        if i == destination:
            return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)

# begin attractions
attractions = [[] for i in destinations]
print(attractions)