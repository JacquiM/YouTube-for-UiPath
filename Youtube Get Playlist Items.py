from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import datetime

import pandas as pd
import numpy as np
import requests
import json
import os


# Create a connection to the Youtube service
def auth(developer_key):

  return build("youtube", "v3", developerKey=developer_key)

# Get all items in specified playlist
def get_playlist_items(page_token, connection, playlist_id):

    # Call the playlistItems.list method to retrieve results matching the specified query term.
    request = connection.playlistItems().list(
        part="snippet,contentDetails",
        pageToken=page_token,
        maxResults=50,
        playlistId=playlist_id
    )
    response = request.execute()
    
    return response

# Write the list of songs to xlsx
def record_playlist_items(filepath, developer_key, playlist_id):

  try:

    isEnd = False
    page_token = None
    df = pd.DataFrame()

    connection = auth(developer_key)

    while not isEnd:

        playlist_items = get_playlist_items(page_token, connection, playlist_id)
        
        current_count = playlist_items['pageInfo']['totalResults']
        
        if 'nextPageToken' in playlist_items.keys():
            
            page_token = playlist_items['nextPageToken']
                                
        else:
            
            isEnd = True
            
            page_token = None
            
        for item in playlist_items['items']:

            temp_df = pd.DataFrame.from_dict(item)
            temp_df = temp_df[['snippet']].transpose()

            df = df.append(temp_df)
                
    df.to_excel(filepath)

    return df.to_json(orient='records')

  except Exception as e:

    file = open("{}_log.txt".format(timestamp), "a+")
    file.write("{0}: Error Logged - {1}\n".format(timestamp, e)) 
    file.close()

    print(e)

    return None