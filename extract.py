import pandas as pd 
import requests
from datetime import datetime
import datetime
import json
import config

TOKEN = config.TOKEN
top_50_playlist = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF?si=ac434aa3d9a24104'
HEADERS = {
    "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

top_50 = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF?si=ac434aa3d9a24104'

# Spotify playlist documentation: https://developer.spotify.com/documentation/web-api/reference/get-playlist

current_day = datetime.datetime.now()

response = requests.get(url = top_50_playlist, headers = HEADERS)

data = response.json()
track_id = []
track_name = []
track_added_at = []
track_popularity = []
artist_name = []
artist_id = []
album_name = []
album_label = []
# album_genres = []

for song in data['tracks']['items']:
    track_id.append(song['track']['id'])
    track_name.append(song['track']['name'])
    track_added_at.append(song['added_at'])
    track_popularity.append(song['track']['popularity'])
    artist_id.append(song['track']['artists'][0]['id'])
    artist_name.append(song['track']['artists'][0]['name'])
    album_name.append(song['track']['album']['name'])
    # album_label.append(song['track']['album']['label'])
    # album_genres.append(song['track']['album']['genres'])
    
    
song_dic = {
    'track_id': track_id,
    'track_name':track_name,
    'track_added_at':track_added_at,
    'track_popularity':track_popularity,
    'artist_id': artist_id,
    'artist_name': artist_name,
    'album_name': album_name,
    # 'album_label': album_label,
    # 'album_genres': album_genres,
    'timestamp':current_day
}

col = ['track_id', 
       'track_name', 
       'track_added_at', 
       'track_popularity', 
       'artist_name',
       'album_name',
    #    'album_label',
    #    'album_genres',
       'timestamp']

song_df = pd.DataFrame(song_dic, columns = col)
    
# print(song_df.head())

    

