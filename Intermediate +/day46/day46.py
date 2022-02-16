import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
"""
a = input("Which year do you want to? travel to? YYYY\n")
b = input("Which month do you want to? travel to? MM\n")
past = a + "-" + b + "-"
c = input("Which day do you want to? travel to? DD\n")
past += c
"""
past = "1989-02-18"
URL = f"https://www.billboard.com/charts/hot-100/{past}/"

response = requests.get(URL)
reply = response.text  # <---- Toda a página

soup = BeautifulSoup(reply, "html.parser")
raw_songs = soup.find_all(name='h3', class_='a-no-trucate', id="title-of-a-story")

artist_name = soup.select(".c-label.a-font-primary-s")

song_titles = [songs.getText().replace('\n', '') for songs in raw_songs]
artiste = [artist.getText().replace('\n', '') for artist in artist_name]
print(artiste)
print(song_titles)


#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="106939fe5a2548638937bdc424be2611",
        client_secret="23d8b1948e59495a8d283e4efcbf0996",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


