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
load_dotenv('../.env')

my_email=os.getenv('EMAIL')
password=os.getenv('APP_PASSWORD')

birthday_data = pd.read_csv("birthdays.csv")
today = dt.datetime.now()

for index, row in birthday_data.iterrows():
    if row['day'] == today.day and row['month'] == today.month:

        #read and personalise letter
        with open('letter_templates/' + random.choice(os.listdir('letter_templates'))) as file:
            letter = file.read().replace('[NAME]', row['name'])

        print(letter)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




