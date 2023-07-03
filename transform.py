import extract
import config
import pandas as pd


df = extract.song_df

# if pd.Series(load_df['track_id'].map(str) + load_df['timestamp'].map(str)).is_unique:
transformed_df = df[['timestamp','artist_name','track_id']].groupby(['timestamp','artist_name'], as_index = False).count()
transformed_df.rename(columns ={'track_id':'count'}, inplace=True)

 # Creating a unique ID based on timestamp and artist name:
transformed_df['id'] = transformed_df[['timestamp', 'artist_name']].sum(axis=1).map(hash)
