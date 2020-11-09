<div align="center">
    <h1>wfetch</h1>
    A small (~100 lines of code) terminal weather fetch tool written in Python.
</div>

## Dependencies
* ```python``` - must be 3.5 or greater
* ```requests``` - for fetching raw data from weather APIs

You can install dependencies using this command: ```pip install -r requirements.txt```

## Installation
To install wfetch, make symbolic link to ```wfetch.py``` file in ```/usr/bin/``` directory:
```
sudo ln -s /path/to/wfetch/wfetch.py /usr/bin/wfetch
```

## Setup
1. Create an [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) account
2. Go to [API keys](https://home.openweathermap.org/api_keys) section in your account settings
3. Update in ```config.py``` ```api``` and ```city``` parameters 
4. Also, optionally update other parameters to set proper for you description language and measurement units
