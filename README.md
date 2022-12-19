# Reddit to Excel Parser
This python program allows users to connect to the Reddit API and retrieve comments from a Reddit post, saving them to an Excel file. The program uses the praw and openpyxl libraries to interact with the Reddit API and create an Excel file, respectively. The program also utilizes the easygui library to prompt the user for input and display messages.

To use the program, enter the Reddit API credentials (client ID, client secret, user agent, username, and password) when prompted. The program will then ask for the URL of the Reddit post and a file name to save the Excel file as. The program will retrieve the top-level comments and all replies, and save them to the Excel file along with the comment ID, author, submitter status, depth, parent ID, score, and creation date.

A detailed description can be found on [the dedicaded blog post](https://jakobfriedl.tech/extracting-reddit-post-comment-data-praw-openpyxl/).

Note: The program expects a file named default_account.json to exist in the same directory, containing the default Reddit API credentials in JSON format. The program will also update this file with the new credentials entered by the user.