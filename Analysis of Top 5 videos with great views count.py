#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openpyxl


# In[2]:


pip install google-api-python-client


# In[ ]:





# In[ ]:





# In[13]:


import pandas as pd
from textblob import TextBlob
from googleapiclient.discovery import build

# Set up the YouTube Data API
api_key = "AIzaSyBzWChHTCmb1SQESD2Zon1UrDbI_EXPeSM"
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the channel ID
channel_id = "UCsS-x_cwLNz4PhRwzRRLoXQ"

# Initialize lists to store data
video_data = []

# Call the API to get the playlist items
next_page_token = None
while True:
    playlist_items = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        pageToken=next_page_token,
        type='video'
    ).execute()

    # Iterate over the playlist items
    for playlist_item in playlist_items['items']:
        video_id = playlist_item['id']['videoId']
        video_details = youtube.videos().list(
            part='statistics, snippet',
            id=video_id
        ).execute()

        title = video_details['items'][0]['snippet']['title']
        views = int(video_details['items'][0]['statistics']['viewCount'])

        comments = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100
        ).execute()
        comment_count = len(comments['items'])

        positive_score = 0
        negative_score = 0
        for comment in comments['items']:
            text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
            analysis = TextBlob(text)
            positive_score += analysis.sentiment.polarity if analysis.sentiment.polarity > 0 else 0
            negative_score += -analysis.sentiment.polarity if analysis.sentiment.polarity < 0 else 0

        video_data.append({
            'video_title': title,
            'views': views,
            'comment_count': comment_count,
            'positive_score': positive_score,
            'negative_score': negative_score
        })

    next_page_token = playlist_items.get('nextPageToken')

    if not next_page_token:
        break

# Create a DataFrame
df = pd.DataFrame(video_data)

# Display the DataFrame
print(df)


# In[15]:


df = df.sort_values(by='views', ascending=False)

df


# In[ ]:





# In[ ]:




