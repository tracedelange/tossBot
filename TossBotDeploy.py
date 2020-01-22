

import tweepy
import json
import requests
import time



#Pulling private keys from environment
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


#Call for Weather update and process request from json
url = ("https://api.openweathermap.org/data/2.5/weather?q=Eugene,us&appid=" + WEATHER_KEY)
response = requests.get(url)
x = response.json()


#Process the data from Weather request to 'update'
# store the value of "main" 
# key in variable y 
y = x["main"] 
current_temperature = round(((y["temp"]) - 273.15)*(9/5) + 32) 
current_pressure = round(((y["pressure"])/1013.2501),4) 
current_humidiy = y["humidity"] 
z = x["weather"] 
weather_description = z[0]["description"] 

# New verdict process

#Import Rain and cloud values from Vals, import statements from st
from vals import vals
from st import st

#Define temperature range values
temperature = [None]
temperature[0:10] = (10 - 0) * [1]
temperature[10:20] = (20 - 10) * [2]
temperature[20:30] = (30 - 20) * [3]
temperature[30:40] = (40 - 30) * [4]
temperature[40:50] = (50 - 40) * [5]
temperature[50:60] = (60 - 50) * [6]
temperature[60:70] = (70 - 60) * [7]
temperature[70:80] = (80 - 70) * [8]
temperature[80:90] = (90 - 80) * [9]
temperature[90:100] = (100 - 90) * [10]

#Define counter variable, current weather ID and current temp 
count = 0
wID = z[0]["id"]
ct = current_temperature


#Add weather ID value to count, if it's outside the range of Vals, default to -4
if wID in vals:
    count += vals[wID]

else:
    count += -4
    
#Add the value of the current Temp
count += temperature[ct]

#Set the verdict equal to the value of the count in the st dictionary
verdict = st[count]


update = ("It's about " + str(current_temperature) +
 " degrees in Eugene and looking like " + str(weather_description) + "."
  + "\n" + str(verdict))


# In[7]:



# In[8]:


# Send processed update as a tweet.

api.update_status(update)




# In[ ]:




