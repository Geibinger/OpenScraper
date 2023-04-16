import openpyxl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# API key
API_KEY = '[YOUR API KEY]'

# Video ID
VIDEO_ID = '[YOUR VIDEO ID]'

# Create a YouTube API client object
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Get the comments for the video
comments = []
next_page_token = ''

while True:
    try:
        # Call the API to retrieve comments
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=VIDEO_ID,
            textFormat='plainText',
            pageToken=next_page_token,
            maxResults=100
        ).execute()

        # Extract comment data from the response
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            created = datetime.strptime(item['snippet']['topLevelComment']['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y %H:%M:%S')
            likes = item['snippet']['topLevelComment']['snippet']['likeCount']

            # Add the comment data to the comments list
            comments.append([comment, author, created, likes])

        # Check if there are more comments to retrieve
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break

    except HttpError as error:
        print(f'An HTTP error {error.resp.status} occurred: {error.content}')
        break

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Create a worksheet for the comments
worksheet = workbook.active
worksheet.title = 'Comments'

# Add column headings to the worksheet
column_headings = ['Comment', 'Author', 'Created', 'Likes']
worksheet.append(column_headings)

# Add the comments to the worksheet
for comment in comments:
    worksheet.append(comment)

# Save the Excel file
workbook.save(f'{VIDEO_ID}.xlsx')
