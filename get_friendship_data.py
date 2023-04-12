import config
import csv
import time
import tweepy


# Authenticate to Twitter API using your private keys and credentials from config.py file
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Creates the API object
api = tweepy.API(auth)

# Twitter username of the user you want to get the following and followers for
username = "anthonymooz"

# Get the user object
user = api.get_user(screen_name=username)

#  Get the list of FOLLOWERS and write username and IDs to CSV
with open(f"{username}_followers.csv", "a", newline="") as file:
    writer = csv.writer(file)


    for page in tweepy.Cursor(api.get_followers, screen_name=username).pages():

        screen_names = [(p.screen_name, p.id) for p in page]
        
        for name, userid in screen_names:
            print([name, userid])
            writer.writerow([name, userid])

        print("waiting 61 secs...")
        time.sleep(61) # Sleep for 61 seconds to avoid hitting rate limit

# Get the list of FOLLOWING and write the username and IDs to CSV
with open(f"{username}_following.csv", "a", newline="") as file:
    writer = csv.writer(file)

    print("Getting the following list")
    for page in tweepy.Cursor(api.get_friends, screen_name=username).pages():
        screen_names = [(p.screen_name, p.id) for p in page]

        for name, userid in screen_names:
            print([name, userid])
            writer.writerow([name, userid])

        print("Waiting 61s...")
        time.sleep(61) # Sleep for 61 seconds to avoid hitting rate limit
