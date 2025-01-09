# Import required modules.
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Get the requested date to input into the request to Billboard. Split out the year for later.
date = input("What date would you like to time-travel to? (YYYY-MM-DD) ")
year = int(date.split("-")[0])

# Scrape data from the Top 100 Songs list for the given date.
# Save that response to a variable and soup it.
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date}/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
response = requests.get(url=billboard_endpoint, headers=headers)
top100 = response.text
soup = BeautifulSoup(top100, "html.parser")

# Pick out all song titles and artists from the list.
titles = soup.select(selector="li ul li h3")
artists = soup.select(selector="li ul li span")

# Put all the song titles into a list of dictionaries.
songs = []
for i in range(len(titles)):
    title = titles[i].getText().strip()
    artist = titles[i].find_next_sibling().getText().strip()
    songs.append({
        "title" : title,
        "artist" : artist,
    })

# Get Spotify credentials and set up a session.
SP_ID = "REDACTED"
SP_SECRET = "REDACTED"
sp_oauth = SpotifyOAuth(client_id=SP_ID, client_secret=SP_SECRET, redirect_uri="http://example.com", scope="playlist-modify-private")
sp_token = sp_oauth.get_access_token(as_dict=False)
client = spotipy.Spotify(oauth_manager=sp_oauth)
user = client.current_user()["id"]

# Take the requested date, search Spotify for songs matching the top-100 title and given year.
# Get the URIs of those songs and save them to a list to use later.
song_uris = []
for song in songs:
    try:
        search_term = f"track:{song["title"]} year:{year-1}-{year}"
        result = client.search(q=search_term, limit="1", type="track")
        artist = result["tracks"]["items"][0]["album"]["artists"][0]["name"]
        track = result["tracks"]["items"][0]["name"]
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    # If the search does not return any tracks, notify the user and skip.
    except IndexError:
        print("Song could not be found. Skipping!")
        pass

# Create a private playlist on Spotify, import the Top 100 Billboard songs from the given date.
playlist = client.user_playlist_create(user=user, name=f"{date} Time Machine", public=False)["id"]
client.user_playlist_add_tracks(user=user, playlist_id=playlist, tracks=song_uris)