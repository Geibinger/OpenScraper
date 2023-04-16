import praw
import openpyxl
import datetime

# Create a Reddit API client object
reddit = praw.Reddit(client_id='[YOUR CLIENT ID]',
                     client_secret='[YOUR CLIENT SECRET]',
                     user_agent = '[YOUR USER AGENT NAME]',
                     username = '[YOUR USERNAME]',
                     password = '[YOUR PASSWORD]')

# Get a subreddit object
subreddit = reddit.subreddit('learnprogramming')

# Get a list of posts from the subreddit
posts = subreddit.hot(limit=2)

# Create a new Excel workbook
workbook = openpyxl.Workbook()


# Recursively iterate through the comments of the post
def process_comments(comments, parent_comment=None):
    for comment in comments:
        # Get the desired information about the comment
        body = comment.body
        author = comment.author.name if comment.author is not None else 'Deleted'  # Check if the author attribute is None before accessing the name attribute
        created = datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%d/%m/%Y %H:%M:%S') # convert created_utc to human-readable format
        score = comment.score       

        # Create a list of values for the comment
        values = [body, author, created, score]

        # If the comment has a parent comment, add the parent comment's body as an additional value
        if parent_comment is not None:
            values.append(parent_comment.body)
        else:
            values.append("None")

        # Add the values to the comments worksheet as a new row
        worksheet.append(values)
        # Recursively process the child comments
        process_comments(comment.replies, comment)



# Iterate through the list of posts
for i, post in enumerate(posts):
    # Create a worksheet for the current post and its comments
    title = post.title
    body = post.selftext
    author = post.author.name if post.author is not None else 'Deleted'  # Check if the author attribute is None before accessing the name attribute
    created = datetime.datetime.utcfromtimestamp(post.created_utc).strftime('%d/%m/%Y %H:%M:%S') # convert created_utc to human-readable format
    score = post.score
    num_comments = post.num_comments
    permalink = post.permalink

    # Create a worksheet for the post data
    worksheet = workbook.create_sheet(f'Post {post.id}')

    # Add column headings to the post worksheet
    column_headings = ['Title', 'Body', 'Author', 'Created', 'Score', 'Num Comments', 'Permalink']
    worksheet.append(column_headings)

    # Add the post data to the post worksheet as a new row
    values = [title, body, author, created, score, num_comments, permalink]
    worksheet.append(values)
    
    # Add empty row
    worksheet.append([''])

    # Add column headings to the comments worksheet
    column_headings = ['Comment', 'Author', 'Created', 'Score', 'Reply to']
    worksheet.append(column_headings)
    # Start the recursive processing of the comments from the top-level comments of the post
    process_comments(post.comments, None)

# Save the Excel file
workbook.save(f'{post.id}.xlsx') 