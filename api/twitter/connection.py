import os
import tweepy
import pandas as pd
import json


class TwitterApp:
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_key_secret):
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_key_secret = consumer_key_secret
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def post_tweet(self, tweet):
        """Post a text with text"""
        try:
            user = self.api.verify_credentials()
            if user is not None:
                self.api.update_status(tweet)
        except tweepy.TweepError as error:
            print(error.reason)

    def post_tweet_with_media(self, media, tweet):
        """Post a tweet with media and text"""
        try:
            user = self.api.verify_credentials()
            if user is not None:
                # Tweet with image and text
                self.api.update_with_media(media, tweet)
        except tweepy.TweepError as error:
            print(error.reason)

    def get_search_tweets(self, search_term, json_output):
        """Search tweet and export into json output"""
        try:
            user = self.api.verify_credentials()
            if user is not None:
                tweets = []
                tweets_attributes = ['id_str', 'created_at', 'text', 'author',
                                     'user', 'place', 'source', 'source_url',
                                     'in_reply_to_user_id_str', 'in_reply_to_screen_name',
                                     'retweeted_status', 'retweet_count', 'favorite_count']
                for tweet in self.api.search(q=search_term, lang='en', rpp=5):
                    tweets.append(tweet)
                    # print(f"{tweet.user.name}:{tweet.text}")
                tweets_df = pd.DataFrame(
                    vars(tweets[i]) for i in range(len(tweets)))
                tweets_df = tweets_df[tweets_attributes]
                #tweets_df.to_json(json_output, orient='records', lines=True)
                json_data = tweets_df.to_json(orient='records')
                jsonified = json.loads(json_data)
                with open(json_output, 'w', encoding='utf-8') as json_file:
                    json.dump(jsonified, json_file,
                              ensure_ascii=False, indent=2)
        except tweepy.TweepError as error:
            print(error.reason)


# Main
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET_KEY')

image_dir = os.path.join(os.path.dirname(__file__), 'images')
image_path = os.path.join(image_dir, 'viper.jpg')
output_dir = os.path.join(os.path.dirname(__file__), 'output')
output_path = os.path.join(output_dir, 'tweets.json')

twpy = TwitterApp(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                  CONSUMER_KEY, CONSUMER_SECRET)

#twpy.post_tweet('Python is awesome!')
#twpy.post_tweet_with_media(image_path, 'Eyelash vipers are pretty cool!')
twpy.get_search_tweets('volunteers', output_path)
