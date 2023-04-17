# Reddit Scraper
This Python script scrapes comments from a given subreddit and stores the data in an Excel file using the `praw` and `openpyxl` libraries.

## Prerequisites
You will need to have the following installed:

- Python 3
- `praw` library
- `openpyxl` library
## Setup
1) Create a Reddit account if you don't have one already.

2) Go to https://www.reddit.com/prefs/apps and create a new application.

3) Select "script" as the type of application.

4) Give your app a name and description.

5) Set "http://localhost:8000" as the redirect uri.

6) Note down the "client id" and "client secret" generated for your app.

7) Install the `praw` and `openpyxl` libraries using pip:

```sh
pip3 install praw openpyxl
```
8) Open the `redditscraper.py` file and replace the following placeholders with your Reddit account information:

```python
client_id = '[YOUR CLIENT ID]'
client_secret = '[YOUR CLIENT SECRET]'
user_agent = '[YOUR USER AGENT NAME]'
username = '[YOUR USERNAME]'
password = '[YOUR PASSWORD]'
```
## Usage
1) Open the reddit_scraper.py file and replace the subreddit name in the following line with the name of the subreddit you want to scrape:

```python
subreddit = reddit.subreddit('learnprogramming')
```
2) Change the limit value to the number of posts you want to scrape:

```python
posts = subreddit.hot(limit=2)
```
3) Run the script using the following command:

```sh
python redditscraper.py
```
4) The script will create an Excel file in the same directory as the script with the scraped data.

## Explanation

This Python script performs the following tasks:

1) Imports the necessary modules: praw (Python Reddit API Wrapper) for accessing the Reddit API, openpyxl for creating and manipulating Excel workbooks, and datetime for formatting date and time information.
2) Creates a Reddit API client object by providing the client ID, client secret, user agent name, username, and password. This client object allows the code to interact with the Reddit API.
3) Gets a subreddit object for the subreddit 'learnprogramming'.
4) Gets a list of posts from the subreddit using the 'hot' method and a limit of 2 posts.
5) Creates a new Excel workbook using openpyxl.
6) Defines a function 'process_comments' that recursively iterates through the comments of a post and extracts the desired information about each comment (body, author, creation time, score, and parent comment). For each comment, it creates a list of values and adds them as a new row to the comments worksheet of the current post's worksheet.
7) Iterates through the list of posts and for each post, creates a new worksheet for the post data and another worksheet for the comments of the post. It extracts the desired information about the post (title, body, author, creation time, score, number of comments, and permalink) and adds them as a new row to the post data worksheet. It then adds column headings to the comments worksheet and starts the recursive processing of the comments from the top-level comments of the post using the 'process_comments' function.
8) Saves the Excel file using the post ID as the filename.

For more information, visit [my blog post](https://jakobfriedl.tech/extracting-reddit-post-comment-data-praw-openpyxl/).

## Notes

- The Reddit API client object is created using the client ID, client secret, user agent name, username, and password. These credentials can be obtained by creating a Reddit app at https://www.reddit.com/prefs/apps.
- The 'hot' method is used to get a list of posts from the subreddit. Other methods such as 'new', 'top', 'rising', and 'controversial' can also be used.
- The 'process_comments' function uses recursion to iterate through the comments of a post. It checks if a comment has a parent comment and adds the parent comment's body as an additional value to the list of values for the comment.
- The 'worksheet' variable is used to refer to the current worksheet being worked on. It is created for each post and comments worksheet and is used to append new rows of data to the worksheet using the 'append' method.