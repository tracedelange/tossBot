#!/usr/bin/env python
# coding: utf-8

# In[2]:



#from os import environ
#from flask import Flask

#app = Flask(__name__)
#app.run(environ.get('PORT'))


# In[3]:


import tweepy
import json
import requests
import time




from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
WEATHER_KEY = environ['WEATHER_KEY']


#Tweepy inantilization

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth)


# In[5]:


#Call for Weather update and process request from json
url = ("https://api.openweathermap.org/data/2.5/weather?q=Eugene,us&appid=" + WEATHER_KEY)
response = requests.get(url)
x = response.json()


# In[ ]:





# In[6]:


#Process the data from Weather request to 'update'
# store the value of "main" 
# key in variable y 
y = x["main"] 
current_temperature = round(((y["temp"]) - 273.15)*(9/5) + 32) 
current_pressure = round(((y["pressure"])/1013.2501),4) 
current_humidiy = y["humidity"] 
z = x["weather"] 
weather_description = z[0]["description"] 

#Process the verdict on if we should play die depending on the weather:
if current_temperature > 60:
    verdict = "It's looking like a great day for die boys"
elif current_temperature < 60 and current_temperature > 30:
    verdict = "It's looking like an alright day for die boys"
elif current_temperature > 30:
    verdict = "It's a fucked day for die boys"


update = (verdict +'\n \n'+"Current weather for Eugene Oregon:"
"\n Temperature = " +
    str(current_temperature) + " Degrees F" 
"\n Pressure (in atmospheres) = " +
    str(current_pressure) +
"\n Humidity (in percentage) = " +
    str(current_humidiy) +
"\n Description = " +
    str(weather_description))


# In[7]:



# In[8]:


# Send processed update as a tweet.

api.update_status(update)

	


# In[ ]:




