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
def fetchData():
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
def viewAscii():
    iconName = source['weather'][0]['main']
    if iconName == "Clear":
        icon = ["      \   /    ", 
                "       .-.     ", 
                "    ‒ (   ) ‒  ", 
                "       `-᾿     ", 
                "      /   \    ", 
                "               "]
    elif iconName == "Clouds":
        icon = ["       .--.     ", 
                "    .-(    ).   ", 
                "   (___.__)__)  ", 
                "                "]
    elif iconName == "Rain":
        icon = ["       .--.     ", 
                "    .-(    ).   ", 
                "   (___.__)__)  ", 
                "   ʻ‚ʻ‚ʻ‚ʻ‚ʻ‚   ", 
                "                "]
    elif iconName == "Snow":
        icon = ["       .--.     ", 
                "    .-(    ).   ", 
                "   (___.__)__)  ", 
                "    * * * * *   ", 
                "                "]
    else:
        icon = ["       .--.     ", 
                "    .-(    ).   ", 
                "   (___.__)__)  ", 
                "                "]

    return icon


# Prints ascii image and weather info.
def printInfo():
    mainGroup = source['main']
    temp = mainGroup['temp']
    humidity = mainGroup['humidity']

    windGroup = source['wind']
    speed = windGroup['speed']

    descGroup = source['weather'][0]
    desc = descGroup['description']

    icon = viewAscii()

    for i in icon:
        print(i)
    print(f"Weather in {cfg.city}")
    print(f"Description: {desc}")
    print(f"Temperature: {str(temp)}°C")
    print(f"Humidity: {str(humidity)}%")
    print(f"Wind: {str(speed)} m/s")


os.system("clear")
printInfo()