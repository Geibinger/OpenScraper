import tweepy
import openpyxl

# BASIC Twitter API subscription needed

# Create a Twitter API client object
consumer_key = '[YOUR CONSUMER KEY]'
consumer_secret = '[YOUR CONSUMER SECRET]'
access_token = '[YOUR ACCESS TOKEN]'
access_token_secret = '[YOUR ACCESS TOKEN SECRET]'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get a list of tweets from a user's timeline
tweets = api.user_timeline(screen_name='[USER SCREEN NAME]', count=10)

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Iterate through the list of tweets
for i, tweet in enumerate(tweets):
    # Create a worksheet for the current tweet and its replies
    worksheet = workbook.create_sheet(f'Tweet {i+1}')

    # Add column headings to the tweet worksheet
    column_headings = ['Text', 'Author', 'Created', 'Retweets', 'Favorites', 'Reply to']
    worksheet.append(column_headings)

    # Get the desired information about the tweet
    text = tweet.text
    author = tweet.author.screen_name
    created = tweet.created_at.strftime('%d/%m/%Y %H:%M:%S')
    retweets = tweet.retweet_count
    favorites = tweet.favorite_count
    reply_to = tweet.in_reply_to_screen_name

    # Create a list of values for the tweet
    values = [text, author, created, retweets, favorites, reply_to]

    # Add the values to the tweet worksheet as a new row
    worksheet.append(values)

    # Add empty row
    worksheet.append([''])

    # Recursively iterate through the replies to the tweet
    def process_replies(tweet_id, parent_tweet=None):
        replies = api.search(q='to:' + '[USER SCREEN NAME]', since_id=tweet_id, count=100)
        for reply in replies:
            if reply.in_reply_to_status_id == tweet_id:
                # Get the desired information about the reply
                text = reply.text
                author = reply.author.screen_name
                created = reply.created_at.strftime('%d/%m/%Y %H:%M:%S')
                retweets = reply.retweet_count
                favorites = reply.favorite_count

                # Create a list of values for the reply
                values = [text, author, created, retweets, favorites, parent_tweet.author.screen_name if parent_tweet else 'None']

                # Add the values to the tweet worksheet as a new row
                worksheet.append(values)

                # Recursively process the replies to the reply
                process_replies(reply.id, reply)

    process_replies(tweet.id)

# Save the Excel file
workbook.save('[FILE NAME].xlsx')