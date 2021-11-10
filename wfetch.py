#!/usr/bin/env python3
"""

wfetch - show weather in your terminal (version 0.1)
Created by Igor Makarowicz.

"""

# Loads dependencies.
import os
import sys
import requests

# Loads settings.
import config as cfg


# Fetches raw data from OpenWeatherMap API and converts it to JSON list.
def fetchData() -> str:
    j = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cfg.city}&APPID={cfg.api}&units={cfg.unit}&lang={cfg.lang}")

    source = j.json()

    # Checks, if return code is 200 and if isn't, displays error message.
    if source['cod'] == 200:
        pass
    elif source['cod'] == "404":
        print("Invalid city name given.")
        sys.exit()
    elif source['cod'] == 401:
        print("Invalid API key given.")
        sys.exit()
    else:
        print("Unknown error occured.")
        sys.exit()
    
    return source


source = fetchData()


# Returns ascii image. 
# ascii weather art used from wego project: https://github.com/schachmat/wego
#pylint: disable=anomalous-backslash-in-string
def viewAscii() -> None :
    iconName = source['weather'][0]['main']
    if iconName == "Clear":
        print("      \   /    ", 
              "       .-.     ", 
              "    ‒ (   ) ‒  ", 
              "       `-᾿     ", 
              "      /   \    ", 
              "               ", sep = '\n')
    elif iconName == "Clouds":
        print("       .--.     ", 
              "    .-(    ).   ", 
              "   (___.__)__)  ", 
              "                ", sep = '\n')
    elif iconName == "Rain":
        print("       .--.     ", 
              "    .-(    ).   ", 
              "   (___.__)__)  ", 
              "   ʻ‚ʻ‚ʻ‚ʻ‚ʻ‚   ", 
              "                ", sep = '\n')
    elif iconName == "Snow":
        print("       .--.     ", 
              "    .-(    ).   ", 
              "   (___.__)__)  ", 
              "    * * * * *   ", 
              "                ", sep = '\n')
    else:
        print("       .--.     ", 
              "    .-(    ).   ", 
              "   (___.__)__)  ", 
              "                ", sep = '\n')

# Checks which measurement unit to use
def unitCheck() -> str:
    if cfg.unit == "standard":
        tempUnit = "K"
        speedUnit = "m/s"
    elif cfg.unit == "metric":
        tempUnit = "°C"
        speedUnit = "m/s"
    elif cfg.unit == "imperial":
        tempUnit = "°F"
        speedUnit = "mph"
    return tempUnit, speedUnit


tempUnit, speedUnit = unitCheck()


# Prints ascii image and weather info.
def printInfo() -> None:
    mainGroup = source['main']
    temp = mainGroup['temp']
    humidity = mainGroup['humidity']

    windGroup = source['wind']
    speed = windGroup['speed']

    descGroup = source['weather'][0]
    desc = descGroup['description']

    viewAscii()
    print(f"""
Weather in {cfg.city}
Description: {desc}
Temperature: {str(temp)}{tempUnit}
Humidity: {str(humidity)}%
Wind: {str(speed)} {speedUnit}
""")

os.system("clear")
printInfo()
input("")
