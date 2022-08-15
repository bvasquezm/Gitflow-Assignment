import pandas as pd

def top_hashtags():
    """
    Returns the top 10 hashtags most used
    """
    tweets_df = pd.read_json('tweets.json', lines=True)
    tweets_df['hashtags'] = tweets_df['hashtags'].astype(str)
    tweets_df['hashtags'] = tweets_df['hashtags'].str[2:-1]
    tweets_df['hashtags'] = tweets_df['hashtags'].str.split(',')
    tweets_df['hashtags'] = tweets_df['hashtags'].apply(lambda x: [i.strip('"') for i in x])
    tweets_df['hashtags'] = tweets_df['hashtags'].apply(lambda x: [i for i in x if i != '#'])
    tweets_df = tweets_df.groupby('id').count()
    tweets_df = tweets_df.sort_values(by='id', ascending=False)
    tweets_df = tweets_df.head(10)
    
    return tweets_df