import requests
import os
import dotenv
from twilio.rest import Client

# set wd to current directory
os.chdir(os.path.dirname(__file__))

# load environment variables
dotenv.load_dotenv('../.env')
API_KEY = os.getenv('OPENWEATHER_API_KEY')
TWILIO_SID = os.getenv('TWILLO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILLO_TOKEN')
MY_NUMBER = os.getenv('MY_NUMBER')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

# get city coordinates (to find a place where it rains: https://www.ventusky.com/)
parameters = {
    # "q": "Newcastle,GB",
    "q": "Detroit,US",
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
    "appid": API_KEY,
    "cnt": 4 # count of forecasts. 4 * 3 = 12 hours
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

response_data = response.json()

for data in response_data["list"]: 
    for weather_data in data["weather"]:
        if weather_data["id"] < 700:
            bring_umbrella = True
            break
        else:
            bring_umbrella = False

if bring_umbrella:
    
    # prepare twilio client
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body = "Bring an umbrella! Wet weather is coming.",
        from_= TWILIO_NUMBER,
        to = MY_NUMBER,
    )

    # message = client.messages.create(
    # from_='whatsapp:+14155238886',
    # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
    # content_variables='{"1":"12/1","2":"3pm"}',
    # to='whatsapp:+447401912373'
    # )    

    print(f"Message status: {message.status}")

else:
    print("No message sent. No need to bring an umbrella.")