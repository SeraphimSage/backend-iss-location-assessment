#!/usr/bin/env python

__author__ = 'Kenneth Pinkerton'

import requests


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
    items = iss_dict.items()
    for item in items:
        iss_keys.append(item[0]), iss_values.append(item[1])
    print("Current ISS relative location : ", iss_values[0])
    print("Timestamp : ", iss_values[2])


def main():
    astronaut_active_duty()
    iss_locator()


if __name__ == '__main__':
    main()
