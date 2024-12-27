import requests
import os
import dotenv

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

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then ...
percentage_change = (open_yesterday - close_day_before_yesterday) / close_day_before_yesterday * 100

if abs(percentage_change) > .5:
    print("Get News")
    
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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

print(news_articles)


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

