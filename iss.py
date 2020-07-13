#!/usr/bin/env python

__author__ = 'Kenneth Pinkerton'

import requests
from turtle import *


def astronaut_active_duty():
    astro_values = []
    get_astro = requests.get(
        'http://api.open-notify.org/astros.json')
    astro_dict = get_astro.json()
    items = astro_dict.items()
    for item in items:
        astro_values.append(item[1])

    print("Astronauts currently in space : ", str(astro_values[1]))

    for line in astro_values[2]:
        print("Astronaut active assignment : ", line)


def iss_locator():
    iss_keys = []
    iss_values = []
    get_iss = requests.get("http://api.open-notify.org/iss-now.json")
    iss_dict = get_iss.json()
    timestamp = iss_dict['timestamp']
    location = iss_dict['iss_position']
    longitude = float(location['longitude'])
    latitude = float(location['latitude'])
    print("Current ISS relative location : ", location)
    print("Timestamp : ", time.ctime(timestamp))
    return longitude, latitude


def world_map(longitude, latitude):
    globe = turtle.Screen()
    globe.setup(720, 360)
    globe.setworldcoordinates(-180, -90, 180, 90)
    globe.title("Where on the Earth is the ISS?")
    # bgcolor("#111111")
    globe.bgpic("map.gif")
    globe.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(longitude, latitude)
    return globe


def main():
    astronaut_active_duty()
    longitude, latitude = iss_locator()
    world_map(longitude, latitude)


if __name__ == '__main__':
    main()
