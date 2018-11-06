import tweepy
import datetime
from time import sleep

# Import our Twitter credentials from credentials.py
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## test to make sure your credentials are set up properly
## should print out the user name associated with your account credentials
#user = api.me()
#print (user.name)

##Test Tweet
# Sending a tweet directly from the python console
#tweet = "this is a test tweet from my bot for #SITEAkron"
#print(tweet)
#api.update_status(tweet)

#For loop to iterate over tweets with #SITEAkron, limit to 10
for tweet in tweepy.Cursor(api.search,
                           q='#SITEAkron',
                           since='2018-11-06',
                           until='2018-11-06',
                           lang='en').items(10):
#Print out usernames of the last 10 people to use #SITEAkron
    try:
        print('I see: @' + tweet.user.screen_name + ' is also making this project today. Nice!')

        #Retweet the tweet
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')

        #Have to space everything out so as to no overload Twitter
        sleep(5)

    #Break gracefully
    except tweepy.TweepError as e:
        print(e.reason)

    #Stop for loop
    except StopIteration:
        break


##Follow everyone who follows you as of today's date.
now = datetime.datetime.now()
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following me as of " + str(now) + ".")

# Open text file stoker.txt (or your chosen file) for reading
stoker = open('stoker.txt', 'r')
# Read lines one by one from my_file and assign to file_lines variable
file_lines = stoker.readlines()
# Close file
stoker.close()

# Create a for loop to iterate over file_lines
# Tweet a line every 10 seconds
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(10)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

tweet()
