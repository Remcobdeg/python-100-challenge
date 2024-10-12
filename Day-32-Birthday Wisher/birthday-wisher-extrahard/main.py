##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import smtplib
import datetime as dt
import random

from dotenv import load_dotenv
import os
import pandas as pd

# Load the environment variables from the .env file
dotenv_path = '../.env'
if os.path.exists(dotenv_path):
    load_dotenv('../.env')
else:
    raise FileNotFoundError('Please provide a valid .env path')

my_email=os.getenv('EMAIL')
password=os.getenv('APP_PASSWORD')

birthday_data = pd.read_csv("birthdays.csv")
today = dt.datetime.now()

for index, row in birthday_data.iterrows():
    if row['day'] == today.day and row['month'] == today.month:

        #read and personalise letter
        with open('letter_templates/' + random.choice(os.listdir('letter_templates'))) as file:
            letter = file.read().replace('[NAME]', row['name'])

        # Construct email message with headers
        subject = "Happy Birthday!"
        to_address = row['email']
        from_address = my_email
        message = f"Subject:{subject}\nTo:{to_address}\nFrom:{from_address}\n\n{letter}"

        # send letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # making encrypted connection to email server
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=from_address, to_addrs=to_address,
                                msg=message)

        print('Email sent!')






