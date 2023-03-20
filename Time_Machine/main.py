import requests
import spotipy
import os
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_ENDPOINT="https://api.spotify.com/v1"
BILLBOARD_URL="https://www.billboard.com/charts/hot-100"
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
REDIRECT_URI="https://www.example.com"



date=input("which year you want to travel to ?Type the date in this format YYYY-MM-DD : ")
response=requests.get(url=BILLBOARD_URL+"/"+date)
response.raise_for_status()

soup=BeautifulSoup(response.text,'html.parser')
song_names=soup.select(selector="li h3")
    
song_lists=[song.getText().replace("\t","").replace("\n","") for song in song_names]
print(song_lists)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="Time_Machine/token.txt"
    )
)

year= date.split("-")[0]
song_URI_list=[]



for song in song_lists:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_URI_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


        
playlist = sp.user_playlist_create(user=CLIENT_ID, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_URI_list)