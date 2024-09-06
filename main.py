import requests

from people import People
from planet import Planet
import matplotlib.pyplot as plt

import pandas as pd

base_url = "https://swapi.dev/api/"

people_endpoint = "people/"

planets_endpoint = "planets/"

planets_list = []
people_list = []

def main():
    #get_planets()
    get_people()

def get_people():
    response = requests.get(base_url + people_endpoint)
    if response.status_code == 200:
        people = response.json()
        for p in people['results']:
            name = p['name']
            gender = p['gender']
            height = p['height']
            birth_year = p['birth_year']

            peopleData = People(name, gender, height, birth_year)
            people_list.append(peopleData)

        data_people = create_dataframe(people_list)
        print(data_people)
        data_people['Height'].astype(float)
        data_people.plot.scatter(x="Name", y="Height", s=200)
        plt.show()
    else:
        print(f"Erro: {response.status_code}")

def get_planets():
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
    people_list_name = []
    people_list_height = []
    for dt in data:
        people_list_name.append(dt.name)
        people_list_height.append(dt.height)

    people_dict = {
        "Name": people_list_name,
        "Height": people_list_height
    }

    people_dataframe = pd.DataFrame(people_dict)
    return people_dataframe

main()