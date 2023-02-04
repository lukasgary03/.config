#!/usr/bin/env python

import json
import requests
from datetime import datetime

WEATHER_ICON = {
    '01d': ' ',
    '01n': ' ',
    '02d': '  ',
    '02n': '  ',
    '03d': '  ',
    '03n': '  ',
    '04d': '  ',
    '04n': '  ',
    '09d': '  ',
    '09n': '  ',
    '10d': '  ',
    '10n': '  ',
    '11d': '  ',
    '11n': '  ',
    '13d': '  ',
    '13n': '  ',
    '50d': '  ',
    '50n': '  '
}

data = {}
apiKey = 98f06073b1b500d6b11fc15bd1cf2578
lat = 38.781151
lon = -90.486931
weather = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?lat={38.781151}&lon={-90.486931}&appid={98f06073b1b500d6b11fc15bd1cf2578}&units=metric').json()

data['text'] = WEATHER_ICON[weather['weather'][0]['icon']] + \
    "  "+str(int(weather['main']['feels_like']))+"°"
print(json.dumps(data))
