import pandas as pd

def top_retweets():
    """
    Returns the top 10 most retweeted tweets
    """
    tweets_df = pd.read_json('tweets.json', lines=True)
    tweets_df['retweetCount'] = tweets_df['retweetCount'].astype(int)
    tweets_df = tweets_df.sort_values(by='retweetCount', ascending=False)
    tweets_df = tweets_df.head(10)
    return tweets_df