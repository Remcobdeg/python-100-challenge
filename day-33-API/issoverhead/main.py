import requests
import time
import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime
from random import randint

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_close(lat: float, long: float) -> bool:

    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
    except requests.exceptions.RequestException as e:
        print(f"request error: {e}")
        print("\n USING DUMMY DATA FOR ISS POSITION")
        # randomly vary lat and long between 0 and 50 deg
        iss_latitude = randint(0,5)*10
        iss_longitude = randint(0,1)*10
    else:
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    iss_is_close = abs(lat - iss_latitude) <= 5 and abs(long - iss_longitude) <= 5

    return iss_is_close

def is_dark(lat: float, long: float) -> bool: 
    
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    except requests.exceptions.RequestException as e:
        print(f"request error: {e}")
        print("\n USING DUMMY DATA FOR SUNRISE AND SUNSET")
        # randomly vary lat and long between -90 and 90 deg
        sunrise = randint(2,8)
        sunset = randint(17,23)
    else:
        print(response.status_code)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    is_dark = time_now.hour >= sunset or time_now.hour <= sunrise

    return is_dark

def send_email():

    # Load the environment variables from the .env file
    dotenv_path = './.env'
    if os.path.exists(dotenv_path):
        load_dotenv('./.env')
    else:
        raise FileNotFoundError('Please provide a valid .env path')

    my_email=os.getenv('EMAIL')
    password=os.getenv('APP_PASSWORD')

    # Construct email message with headers
    subject = "ISS visible"
    to_address = my_email
    from_address = my_email
    content = "The ISS is close to you and it is dark! Look up!"
    message = f"Subject:{subject}\nTo:{to_address}\nFrom:{from_address}\n\n{content}"

    # send letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # making encrypted connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=from_address, to_addrs=to_address,
                            msg=message)

    print('Email sent!')


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

while True:
    
    if is_close(MY_LAT, MY_LONG) and is_dark(MY_LAT, MY_LONG):
        # Then send me an email to tell me to look up.
        send_email()
    else:
        print(f"iss not visible (close = {is_close(MY_LAT, MY_LONG)}, dark = {is_dark(MY_LAT, MY_LONG)})")

    time.sleep(3)



