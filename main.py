import requests

from planet import Planet

import pandas as pd

base_url = "https://swapi.dev/api/"

planets_endpoint = "planets/"

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

        data_planets = create_dataframe(planets_list)
        print(data_planets)

    else:
        print(f"Erro: {response.status_code}")

#showing dataframe for population on planets
def create_dataframe(data):
    planets_list = []
    for dt in data:
        planet_dict = {
            "Name": dt.name,
            "Population": dt.population,
            "Climate": dt.climate,
        }
        planets_list.append(planet_dict)

    planets_dataframe = pd.DataFrame(planets_list)
    return planets_dataframe

main()