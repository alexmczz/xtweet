import tweepy 
import sys

client = tweepy.Client(consumer_key = "<consumer key goes here>",
consumer_secret = "<consumer secret goes here>",
access_token = "<Access token goes here>",
access_token_secret = "<Access token secret goes here>")


if len(sys.argv) > 1:
    response = client.create_tweet(text=f'{" ".join(sys.argv[1:])}')
    print('Tweet posted successfully!')
else:
    print(f'Error posting tweet')
    print('Usage: python xweet.py <message>')