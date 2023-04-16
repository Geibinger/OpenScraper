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