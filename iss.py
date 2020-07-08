#!/usr/bin/env python

__author__ = 'Kenneth Pinkerton'

import requests


def main():
    get_astro = requests.get(
        'http://api.open-notify.org/astros.json')
    astro_dict = get_astro.json()
    print(astro_dict['name'])


if __name__ == '__main__':
    main()
