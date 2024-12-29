import requests
import os
import dotenv
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "tesla"

# Import API keys from .env file
dotenv.load_dotenv(".env")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

stock_data = requests.get("https://www.alphavantage.co/query", params=params)
stock_data.raise_for_status()

stock_day_data = stock_data.json()["Time Series (Daily)"]

# get dates of the stock data
dates = list(stock_day_data.keys())
yesterday = dates[0]
day_before_yesterday = dates[1]

# Get the opening price of the stock for yesterday and the day before yesterday
open_yesterday = float(stock_day_data[yesterday]["1. open"])
close_day_before_yesterday = float(stock_day_data[day_before_yesterday]["4. close"])

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then collect news articles
percentage_change = round((open_yesterday - close_day_before_yesterday) / close_day_before_yesterday * 100, ndigits=1)

if abs(percentage_change) > .5:

    params = {
        "q": COMPANY_NAME,
        "from": day_before_yesterday,
        "sortBy": "popularity",
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    news_articles = requests.get("https://newsapi.org/v2/everything", params=params)
    news_articles.raise_for_status()
    news_articles = news_articles.json()["articles"]

    UP = '🔺'
    DOWN = '🔻'

    messages = [
        f"{STOCK}: {UP if percentage_change > 0 else DOWN}{abs(percentage_change)}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in news_articles
    ]

    # concatenate all messages
    messages = "\n\n".join(messages)

    # PREPARE EMAIL

    my_email=os.getenv('EMAIL')
    password=os.getenv('APP_PASSWORD')

    # Construct email message with headers
    subject = f"{STOCK}: {UP if percentage_change > 0 else DOWN}{abs(percentage_change)}%"
    to_address = my_email
    from_address = my_email
    message = f"Subject:{subject}\nTo:{to_address}\nFrom:{from_address}\n\n{messages}"

    # send letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # making encrypted connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=from_address, 
            to_addrs=to_address,
            msg=message.encode('utf-8')  # encode the message in utf-8
        )

    print('Email sent!')


