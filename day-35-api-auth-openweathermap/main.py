#todo retrieve 3-hour weather for my location using OpenWeatherMap API

import requests
import os
import dotenv

# set wd to current directory
os.chdir(os.path.dirname(__file__))

# load environment variables
dotenv.load_dotenv('../.env')
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# get city coordinates
parameters = {
    "q": "Newcastle,GB",
    "appid": API_KEY
}

geo_response = requests.get("https://api.openweathermap.org/geo/1.0/direct", params=parameters)

geo_response.raise_for_status()

geo_data = geo_response.json()
lat = geo_data[0]["lat"] # 54.9738474
lon = geo_data[0]["lon"] # -1.6131572

# get weather data
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

response_data = response.json()

# print response code
print(response_data["cod"])