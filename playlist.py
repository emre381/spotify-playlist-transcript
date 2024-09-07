import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os

# Spotify ENTER API ID  INFORMATION
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="************************",  # Enter spesific spotify list url  
                                               scope="user-library-read"))

# INFORMATION ABOUT THE PLAYLIST 
playlist_id = "spotify:playlist:********************" #Enter the spotify list code end of the playlists url 
results = sp.playlist_tracks(playlist_id)

# SAVE THE SONGS AND ARTISTS
tracks_data = []
for item in results['items']:
    track = item['track']
    track_name = track['name']
    artist_name = track['artists'][0]['name']
    tracks_data.append([track_name, artist_name])

# TRANSPORT THE DATAS DATAFRAME WITH PANDAS 
df = pd.DataFrame(tracks_data, columns=['Track Name', 'Artist Name'])

# SAVE IT TO EXCEL FILE
df.to_excel('spotify_playlist_tracks.xlsx', index=False)

print("Spotify playlist şarkıları 'spotify_playlist_tracks.xlsx' dosyasına kaydedildi.")

# LOCATION OF THE SAVED FILE 
file_path = os.path.abspath('spotify_playlist_tracks.xlsx')
print(f"Dosya şu konuma kaydedildi: {file_path}")
