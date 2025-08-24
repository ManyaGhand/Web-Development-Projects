import os
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp= spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id= f"{client_id}",
        client_secret=f"{client_secret}",
        show_dialog=True,
        username="Manya",
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

charts = requests.get(url = f"https://www.billboard.com/charts/hot-100/{date}" , headers= header)
soup = BeautifulSoup(charts.text, "html.parser")
billboard_songs = [song.getText().strip() for song in soup.select("li ul li h3")]

song_uris = []
year = date.split("-")[0]
for song in billboard_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit= 1)
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlists = sp.user_playlist_create(
    user = user_id,
    name= f"Billboard Hot 100- {date}",
    public = False,
    description = f"Top 100 songs from Billboard  on {date}"
)

for i in range(0, len(song_uris), 100):
    sp.playlist_add_items(playlist_id= playlists["id"], items= song_uris[i:i+100])

print(f" Playlist created: {playlists['external_urls']['spotify']}")