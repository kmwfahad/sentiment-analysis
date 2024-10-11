#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openpyxl


# In[2]:


from googleapiclient.discovery import build
import openpyxl

# Set up the YouTube Data API
api_key = "AIzaSyBzWChHTCmb1SQESD2Zon1UrDbI_EXPeSM"
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the channel ID
channel_id = "UCsS-x_cwLNz4PhRwzRRLoXQ"

# Call the API to get the comments
comments_response = youtube.commentThreads().list(
    part="snippet",
    allThreadsRelatedToChannelId=channel_id,
    maxResults=100
).execute()

# Extract the comments
comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_response['items']]

# Write comments to an Excel file
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Comments'

for i, comment in enumerate(comments, start=2):
    sheet.cell(row=i, column=1).value = comment

# Save the Excel file
wb.save("youtube_comments.xlsx")


# In[ ]:




