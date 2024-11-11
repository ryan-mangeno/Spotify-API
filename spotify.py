from dotenv import load_dotenv
import os
import base64
from requests import post
import requests
import json 


load_dotenv()

client_secret = os.getenv("SPOTIFY_SECRET")
client_id = os.getenv("SPOTIFY_CLIENT_ID")


redirect_uri = "http://localhost:8888/callback"

base_url = 'https://accounts.spotify.com/api/token'

def get_token():

    #encoding the client_id and client_secret required by spotify api ...
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    #specificy grant type
    data = {"grant_type" : "client_credentials"}

    result = post(base_url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    expires = json_result["expires_in"]
    return token, expires

#gets auth headers
def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}


# gen playlist ids
def get_user(header,user_id):

    user_info =  f"https://api.spotify.com/v1/users/{user_id}/playlists"  # Constructing URL with user ID
    response = requests.get(user_info,headers=header)

    if response.status_code == 200:
        json_result = json.loads(response.content)
        playlist_ids = []

        # Iterate through each playlist dictionary
        for playlist in json_result["items"]:
            # Access the 'id' key of the playlist dictionary and append it to the playlist_ids list
            playlist_ids.append(playlist['id'])

        return playlist_ids
    
    else:
        print(f"Error: {response.status_code}")
        return None

def playlist_stuff(header,playlist_id):

    playlist_url =f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.get(playlist_url,headers=header)

    if response.status_code == 200:
        json_result = json.loads(response.content)
        # List to store track names
        track_names = []

        # Iterate through each item (track) in the list
        for item in json_result['items']:
            # Access the 'name' key of the track and append it to the track_names list
            track_names.append(item['track']['name'])
        # Print the list of track names
        return track_names


    else:
        print(f"Error: {response.status_code}")
        return




token, expires = get_token()
header = get_auth_headers(token)

#user_playlist_id is also from env
user_playlist_id = os.getenv("USER_PLAYLIST_ID")
playlist_ids = get_user(header,user_playlist_id)
all_tracks = []

for id in playlist_ids:
    all_tracks.append(playlist_stuff(header,id))


#Open a file named "songs.txt" in write mode
with open("songs.txt", "w") as file:
    for songs_list in all_tracks:
        for song in songs_list:
            file.write(f"{song}\n")

# File is automatically closed after the 'with' block ends
