import pandas as pd 
import requests
from datetime import datetime
import datetime
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
artist_popularity = []
album_name = []
album_label = []
album_genres = []


for song in data['tracks']['items']:
    track_id.append(song['track']['id'])
    track_name.append(song['track']['name'])
    track_added_at.append(song['added_at'])
    track_popularity.append(song['track']['popularity'])
    artist_name.append(song['track']['popularity'])

    song_dic = {
        'track_id': track_id,
        'track_name':track_name,
        'track_added_at':track_added_at,
        'track_popularity':track_popularity,
        'timestamp':current_day
    }

col = ['track_id', 'track_name', 'track_added_at', 'track_popularity', 'timestamp']

song_df = pd.DataFrame(song_dic, columns = col)
    
print(song_df)

    

