import pandas as pd

def top_days_by_tweets():
    """
    Returns the top 10 days with the most tweets
    """
    tweets_df = pd.read_json('tweets.json', lines=True)
    tweets_df['date'] = tweets_df['date'].astype(str)
    tweets_df['date'] = tweets_df['date'].str[:10]
    tweets_df = tweets_df.groupby('date').count()
    tweets_df = tweets_df.sort_values(by='id', ascending=False)
    tweets_df = tweets_df.head(10)
    return tweets_df