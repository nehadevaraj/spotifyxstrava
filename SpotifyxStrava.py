print ("Hello welcome to the Spotify x Strava feature")

import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
import circlify
import matplotlib.pyplot as plt

######### lets geddit little miss  #############
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


CLIENT_ID = '5a736490b12c4ed28d74f6f6bbdadf2b'
CLIENT_SECRET = 'b280e2f0654141da9aea87377dfbb1ab'
REDIRECT_URI = 'https://localhost:8888/callback'
USERNAME = '5kqif587k252j991ekfnj9tfh'
SCOPE = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    username=USERNAME,
    show_dialog=True
))

results = sp.current_user_top_tracks(limit=50, time_range='medium_term')

tracks = []

for item in results['items']:
    track_info = {
        'Track Name': item['name'],
        'Artist': item['artists'][0]['name'],
        'Album': item['album']['name'],
        'Release Date': item['album']['release_date'],
        'Popularity': item['popularity'],
        'Duration (ms)': item['duration_ms'],
        'Track URL': item['external_urls']['spotify']
    }
    tracks.append(track_info)

df = pd.DataFrame(tracks)
df.to_csv('spotifyxstrava/Top_items.csv', index=False)

print("Top_items.csv has been created.")