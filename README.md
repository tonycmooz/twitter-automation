# Twitter Automation

## Prerequisites


* Twitter Developer Account([sign up here](https://developer.twitter.com/en))
* A Project and an App created [in the dashboard](https://developer.twitter.com/en/portal/dashboard)
* Python 3

## Scripts

* get_friendship_data.py

This script finds out any user's follower and following and generates two CSV files with the username and user_id.

* find_common_people.py

Once you a user's follower and following CSV files, you can run this script to find the user's friends (people who follow back).

* not_following_back.py

You can even find out who is not following back an account this script.

* unfollow_twitter_users.py

If you wish to automatically unfollow accounts that do not follow you back. Run this script (with your API credentials in your config.py file)

## Requirements

* Install Tweepy

```bash
pip3 install tweepy
```

* Setup your config.py File with your developer credentials

```python
API_KEY = 'YOUR-API-KEY-GOES-HERE'
API_SECRET = 'YOUR-API-SECRET-GOES-HERE'
ACCESS_TOKEN = 'YOUR-ACCESS-TOKEN-GOES-HERE'
ACCESS_TOKEN_SECRET = 'YOUR-ACCESS-TOKEN-SECRET-GOES-HERE'
```
