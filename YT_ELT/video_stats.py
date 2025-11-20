
# import requests
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path="./.env")
# api_key = os.getenv("api_key")
# channel_name = "MrBeast"

# # The following environment is selected: c:\GIT\.venv\Scripts\python.exe

# def get_playlist_id():
#     try:
#         url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_name}&key={api_key}"
#         response = requests.get(url=url)
#         json_response = response.json()
#         # print(response)
#         # print(json.dumps(json_response,indent=2))
#         channel_items = json_response['items'][0]
#         channel_playlistid = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
#         print(channel_playlistid)
#         return channel_playlistid
#     except requests.exceptions.RequestException as e:
#         raise e

# if __name__ == "__main__":
#     get_playlist_id()


import requests
import json
import os
from dotenv import load_dotenv

load_dotenv("./.env")
api_key = os.getenv("api_key")
channel_name = "@MrBeast"

def get_playlist_id():
    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_name}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    # print(json.dumps(data, indent=2))  # Debug print

    if "items" not in data:
        print("ERROR: items not found in response")
        return

    playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    print("Uploads Playlist ID:", playlist_id)
    return playlist_id

if __name__ == "__main__":
    get_playlist_id()


# print("API KEY LOADED =", api_key)
# print("LENGTH =", len(api_key))
