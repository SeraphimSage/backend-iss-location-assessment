#!/usr/bin/env python

__author__ = 'Kenneth Pinkerton'

import requests
import time
import turtle

indiana_lon = -86.148003
indiana_lat = 39.791000


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
    return(get_astro)


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
    globe.bgcolor("#111111")
    globe.bgpic("map.gif")
    globe.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(longitude, latitude)
    indiana_loc_pin = turtle.Turtle()
    indiana_loc_pin.penup()
    indiana_loc_pin.color('orange')
    indiana_loc_pin.goto(indiana_lon, indiana_lat)
    indiana_loc_pin.dot(8)
    globe.exitonclick()
    return globe


def intercept(latitude, longitude):
    params = {'lat': latitude, 'lon': longitude}
    indiana_intercept = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=params)
    passover = time.ctime(indiana_intercept.json()['response'][1]['risetime'])
    print("The next time the ISS will passover Indianapolis is on ", passover)
    return passover


def main():
    astronaut_active_duty()
    longitude, latitude = iss_locator()
    intercept(indiana_lat, indiana_lon)
    world_map(longitude, latitude)


if __name__ == '__main__':
    main()
