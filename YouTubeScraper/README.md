# YouTube Comments Scraper using YouTube API
This Python program allows you to scrape comments from a YouTube video using the YouTube API.

## Setup
1) To use this program, you need to have a Google account and enable the YouTube Data API v3 for your project. If you haven't enabled the API already, go to the [Google API Console](https://console.cloud.google.com/apis/library/youtube.googleapis.com) and enable the API.

2) Once you've enabled the API, create a new API key from the "Credentials" section of your Google API Console. This will give you access to the API key needed for authentication.

3) Replace the `[YOUR API KEY]` placeholder with the API key you obtained in the previous step.

4) Replace the `[YOUR VIDEO ID]` placeholder with the video ID of the YouTube video you want to scrape comments from.

5) Install `OpenPyXl` and the `Google API Python client library` by running the following command in your terminal or command prompt:

```sh
pip3 install openpyxl google-api-python-client
```
## Usage
1) Open the `youtube_comments_scraper.py` file in your Python editor of choice.

2) Modify the `VIDEO_ID` variable to specify the video ID of the YouTube video you want to scrape comments from.

3) Run the program.

```sh
python youtube_comments_scraper.py
```
4) The program will save the scraped comments to an Excel file named `[VIDEO_ID].xlsx` in the same directory as the `youtube_comments_scraper.py` file.
## Notes
The YouTube API imposes limits on how frequently you can retrieve comments, so be sure to check the [YouTube API Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost) and adjust your code accordingly.

This program retrieves comments from a single video. If you want to scrape comments from multiple videos, you will need to modify the program to loop over a list of video IDs. Check out the [YouTube API documentation](https://developers.google.com/youtube/v3/docs/comments/list) for more information on retrieving comments from multiple videos.