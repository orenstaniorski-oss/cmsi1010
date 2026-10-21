import random
from haversine import haversine
from geography import countries 

def random_hint(country):
    match random.choice(["capital", "region", "landmark", "distance"]):
        case "capital":
            hint = "whose capital is " + country["capital"]
        case "region":
            hint = "in " + country["region"]
        case "landmark":
            hint = "where you can find " + random.choice(country["landmarks"])
        case "distance":
            los_angeles = (34.0522, -118.2437)
            from_LA = haversine(los_angeles, country["coordinates"], unit="km")
            from_LA = round(from_LA)
            hint = "approximately " + str(from_LA) + " km from Los Angeles"
    return "Carmen is in a country " + hint

def random_country_name():
    return random.choice(list(countries.keys()))

while True:
    print("Guess where Carmen is, or say 'hint' or 'exit'.")
    guess = input("Where are you going to look? ").strip().lower()
    if guess == current_country_name:
        print("She was here, but you missed her by one hour!")
    elif guess == "hint":
        print("Sorry, no hints yet.")
    elif guess == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Oh no, she’s not here!")

