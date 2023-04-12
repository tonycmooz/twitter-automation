import config
import csv
import time
import tweepy

# Authenticate to Twitter API using your private keys and credentials from config.py file
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Path to list to unfollow
csv_file = 'list_to_unfollow.csv'

with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        username = row[0]
        user_id = int(row[1])

        try:
            api.destroy_friendship(user_id = user_id)
            print(f"Unfollowed {username} ({user_id})")
        except tweepy.errors.TweepyException as e:
            print(f"Failed to unfollow {username} ({user_id}): {e}")

# def unfollow(csv_file_name):
#     with open(file_name, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         return [row[1] for row in reader]