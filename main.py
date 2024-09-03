import requests

from planet import Planet

import pandas as pd

base_url = "https://swapi.dev/api/"


films_endpoint = "films/"

planets_endpoint = "planets/"

people_endpoint = "people/"

species_endpoint = "species/"

vehicles_endpoint = "vehicles/"

species_endpoint = "species/"

def main():
    planets_list = []

    response = requests.get(base_url + planets_endpoint)

    if response.status_code == 200:
        planets = response.json()
        for planet in planets['results']:
            name = planet['name']
            climate = planet['climate']
            gravity = planet['gravity']
            population = planet['population']
            terrain = planet['terrain']

            planetData = Planet(name, climate, terrain, population, gravity)
            planets_list.append(planetData)

            print(f"Planet: {name}\nClimate: {climate}\n"
                  f"Gravity: {gravity}\nPopulation: {population}\n"
                  f"Terreno: {terrain}\n")
            print('====================================================================')
    create_dataframe(planets_list)



#showing dataframe for population on planets
def create_dataframe(data):
    planets_dict = {}
    for dt in data:
        planets_dict.setdefault(dt.name, dt)

    planets_dataframe = pd.DataFrame(data=data)
    print(planets_dataframe)

main()