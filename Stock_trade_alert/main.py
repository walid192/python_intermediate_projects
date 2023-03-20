from turtle import title
import requests
import os
from twilio.rest import Client
from newsapi import NewsApiClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY=os.getenv("STOCK_API_KEY")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")

#------------------------------- STEP 1: Use https://www.alphavantage.co/documentation/#daily ------------------------------------#
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Get yesterday's closing stock price
my_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response=requests.get(url=STOCK_ENDPOINT,params=my_params)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[float(value["4. close"]) for (key,value) in data.items()]
yesterdays_price=data_list[0]
print("yesterday's closing stock price : ",yesterdays_price)


# Get the day before yesterday's closing stock price
before_yesterdays_price=data_list[1]
print("before yesterday's closing price : ",before_yesterdays_price)


# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=(yesterdays_price-before_yesterdays_price)
if difference<0:
    up_down="🔻"
else:
    up_down="🔺"


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_percenatge=round(abs(difference)*100/yesterdays_price,2)
print(f"the percentage of difference : {difference_percenatge} %")

    
#------------------------------------ STEP 2: https://newsapi.org/ -----------------------------------------------#

#get the first 3 news pieces for the COMPANY_NAME. 
if difference_percenatge>5:
    
    newsapi=NewsApiClient(api_key=NEWS_API_KEY)
    news=newsapi.get_everything(q="TESLA",language="en")
    articles=news["articles"][:3]
    news_list=[f"TSLA :{up_down} %{int(difference_percenatge)} \nHeadline : {article['title']} \nBrief : {article['description']}" for article in articles  ]
#------------------------------------ STEP 3: Use twilio.com/docs/sms/quickstart/python ---------------------------------------#
# Send each article as a separate message via Twilio. 
    account_sid = os.getenv("ACCOUNT_ID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    for article in news_list:
        
        message = client.messages \
                        .create(
                            body=article,
                            from_=os.getenv("SENDER_NUMBER"),
                            to=os.getenv("RECEIVER_NUMBER")
                        )
        print(message.sid)






