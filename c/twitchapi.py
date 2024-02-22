#twitch api

from dotenv import load_dotenv
import os
from requests import post 
import requests
import json 


#using dotenv to load client secrets so its not explicitly stated in the code
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

url = 'https://id.twitch.tv/oauth2/token'

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

data = requests.post(url,params=params)

if data.status_code == 200:
    result = data.json()
    access_token = result['access_token']
    expire = result['expires_in']

    stream_url = "https://api.twitch.tv/helix/streams"

    #make param for streamer
    user = input("Enter streamer")
    streamer_param = {
    "user_login": user
    }

    #header for access_token
    #'client-id' in headers not "client_id"
    streamer_headers = {
    "Client-id" : client_id,
    "Authorization": "Bearer " + access_token,
    }

    stream_data = requests.get(stream_url,params=streamer_param, headers=streamer_headers)

    if stream_data.status_code == 200:

        stream_result_bruh = stream_data.json()


        #if streamer offline this will not work
        try:
            stream_result = stream_result_bruh['data'][0]
            print(stream_result)
            print(f"{user} is playing {stream_result['game_name']}")
            print(f"There is currently {stream_result['viewer_count']} viewers")
            print(f"{user} started at {stream_result['started_at']})")

            #found out broadcaster_id is the 'id' in streamer data
            broadcaster_id = stream_result['id']
            user_id = stream_result['user_id']

        
        except IndexError as e:
            print("Error: could not parse streamer data due to - ", e)

    else:
        print(f"Could not connect - stream part {stream_data.status_code}")


    emote = "https://api.twitch.tv/helix/bits/cheermotes"
    
    emote_params = {
        'broadcaster_id':broadcaster_id,
    }

    emote_response = requests.get(emote,params=emote_params,headers=streamer_headers)

    if emote_response.status_code == 200:
        emote_data = emote_response.json()
        data_parse = emote_data['data'][0]['tiers'][0]['images']['dark']['animated']
        
        for element in data_parse.values():
            print(element)
    
    else:
        print("Error getting ad schedule ", emote_response.status_code)
    
    
    
else:
    print(f"Could not get access_token {data.status_code}")