import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import random

# get dircetory of the file
dir = os.path.dirname(__file__)

# Load the environment variables from the .env file
load_dotenv()

#get quotes
with open(os.path.join(dir,"quotes.txt")) as file:
    quotes = [line.strip() for line in file.readlines()]

my_email=os.getenv('EMAIL')
password=os.getenv('APP_PASSWORD')

week_day = dt.datetime.now().weekday() #Monday = 0, Sunday = 6
quote = random.choice(quotes)

if week_day == 4:
    print(f"Sending quote")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #making encrypted connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="remco.degrave@yahoo.com", msg=f"Subject:Quote of the week\n\n{quote}")
