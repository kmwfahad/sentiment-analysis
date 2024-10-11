#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install google-api-python-client


# In[3]:


from googleapiclient.discovery import build

# Set up the YouTube Data API
api_key = "AIzaSyBzWChHTCmb1SQESD2Zon1UrDbI_EXPeSM"
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the channel ID
#channel_id = "UCsS-x_cwLNz4PhRwzRRLoXQ"

channel_id = "UCWv7vMbMWH4-V0ZXdmDpPBA"

# Call the API to get the comments
comments = youtube.commentThreads().list(
    part="snippet",
    allThreadsRelatedToChannelId=channel_id,
    maxResults=100
).execute()

# Process the comments
for comment in comments['items']:
    print(comment['snippet']['topLevelComment']['snippet']['textDisplay'])


# In[ ]:





# In[4]:


pip install textblob


# In[7]:


import matplotlib.pyplot as plt
from textblob import TextBlob
from googleapiclient.discovery import build

# Set up the YouTube Data API
api_key = "AIzaSyBzWChHTCmb1SQESD2Zon1UrDbI_EXPeSM"
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the channel ID
channel_id = "UCkLXELm63_pH7L-r-548kig"

# Call the API to get the comments
comments = youtube.commentThreads().list(
    part="snippet",
    allThreadsRelatedToChannelId=channel_id,
    maxResults=100
).execute()

# Perform sentiment analysis
positive_comments = 0
negative_comments = 0

for comment in comments['items']:
    text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        positive_comments += 1
    elif analysis.sentiment.polarity < 0:
        negative_comments += 1

# Display results in a graph
labels = ['Positive Comments', 'Negative Comments']
sizes = [positive_comments, negative_comments]
colors = ['#7d7d7d', '#c3c2c2']
explode = (0.1, 0)  

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Sentiment Analysis of YouTube Comments')
plt.show()


# In[ ]:





# In[ ]:




