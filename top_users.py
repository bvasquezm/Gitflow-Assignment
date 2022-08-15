import pandas as pd

def top_users_by_tweets():
    """
    Returns the top 10 users with the most tweets
    """
    tweets_df = pd.read_json('tweets.json', lines=True)
    tweets_df['user'] = tweets_df['user'].astype(str)
    tweets_df = tweets_df.groupby('user').count()
    tweets_df = tweets_df.sort_values(by='id', ascending=False)
    tweets_df = tweets_df.head(10)
    return tweets_df