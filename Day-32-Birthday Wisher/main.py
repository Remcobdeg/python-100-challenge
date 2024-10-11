import smtplib
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

my_email = "remco.b.de.grave@gmail.com"
password=os.getenv('APP_PASSWORD')

connection = smtplib.SMTP("smtp.gmail.com") #smtp.mail.yahoo.com
connection.starttls() #making encrypted connection to email server
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="remco.degrave@yahoo.com", msg="Subject:hello\n\n"
                                                                                "This is the body of my email")
connection.close()