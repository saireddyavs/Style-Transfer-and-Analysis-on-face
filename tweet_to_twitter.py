import numpy as np
import tweepy

#variables for accessing twitter API
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


tweet_text="My first Auto Tweet for #CodeChella"
image_path ="static/uploads/Style_udnie_Mark_Zoo_Mowaa.jpg"

#Generate text tweet with media (image)
status = api.update_with_media(image_path, tweet_text)
# api.update_status(status=tweet_text)



