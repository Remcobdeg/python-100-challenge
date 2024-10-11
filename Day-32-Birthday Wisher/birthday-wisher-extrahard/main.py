##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas as pd

birthday_data = pd.read_csv("birthdays.csv")

# for _, row in birthday_data.iterrows():
#     print(dt.datetime(day=birthday_data['day'].item(),month=birthday_data['month'].item(),year=birthday_data['year'].item()))

birthday_data['date'] = dt.datetime(day=birthday_data['day'].item(),month=birthday_data['month'].item(),year=birthday_data['year'].item())
print(birthday_data['date'])




# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




