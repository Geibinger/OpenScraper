# importing easygui module
from tkinter.constants import TRUE
from easygui import *
import json
import praw
import os
import sys

from openpyxl import Workbook
from datetime import datetime

# recursive function to open every fold of the comment tree

def iterateThroughReplys(comment, dpth):

    for reply in comment.replies:

        dpth = dpth + 1

        row = [str(reply.id), str(reply.author), str(reply.is_submitter), str(dpth), str(reply.parent_id), str(reply.score), str(reply.body), str(datetime.fromtimestamp(reply.created_utc))]

        ws.append(row)

        iterateThroughReplys(reply, dpth)

# iterate through every top-level comment and write to file
def appendBodyToWorksheet():
        for comment in submission.comments:

                depth = 1

                row = [str(comment.id), str(comment.author), str(comment.is_submitter), str(depth), str(comment.parent_id), str(comment.score), str(comment.body), str(datetime.fromtimestamp(comment.created_utc))]

                ws.append(row)
                iterateThroughReplys(comment, depth)

def getDataFromJson(fileName):
    # Opening JSON file
    with open(fileName, "r") as accountFile:
        defaultAccount = json.load(accountFile)
    # list of default text from json file
    defaultList = [defaultAccount["client_id"], defaultAccount["client_secret"], defaultAccount["user_agent"], defaultAccount["username"], defaultAccount["password"]]
    accountFile.close()
    return defaultList

def updateJsonFile(fileName, credentials):
    # Update JSON file with new credentials
    updatedData = { "client_id": credentials[0], "client_secret": credentials[1], "user_agent": credentials[2], "username": credentials[3], "password": credentials[4] }

    with open(fileName, "w") as accountFile:
        accountFile.write(json.dumps(updatedData))
        accountFile.close()

if __name__=="__main__":
    # window title
    title = "Reddit to Excel Parser"
    # message to be displayed
    text = "Enter the following details to connect to the Reddit API"
    # list of multiple inputs
    inputList = ["client ID", "client secret", "user agent", "username", "password"]

    # get cretdentials from user input
    try:
        defaultList = getDataFromJson("default_account.json")

        credentials = multenterbox(text, title, inputList, defaultList)

        if(credentials == None):
            sys.exit()

        updateJsonFile("default_account.json", credentials)

    except Exception as e:
        msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
        sys.exit()

    # Reddit API:
    try:
        reddit = praw.Reddit(client_id = credentials[0], client_secret = credentials[1], user_agent = credentials[2], username = credentials[3], password = credentials[4])
    except Exception as e:
        msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
        sys.exit()

    while TRUE:
        url = enterbox("enter post URL", title)
        
        if(url == None):
            sys.exit()

        try:
            submission = reddit.submission(url=url)
            path = enterbox("Safe file as: ", title)
            
            if(path == None):
                sys.exit()

            path += ".xlsx"

        except Exception as e:
            msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
            sys.exit()

        #_______________________________________________________________________________________________________________________
        
        # create workbook

        wb = Workbook()
        ws = wb.active

        try:
            ws.title = submission.id
        except Exception as e:
            msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
            sys.exit()


        row = ["ID", "title", "author", "number of comments", "score", "url", "submission date"]
        ws.append(row)

        try:
            row = [str(submission.id), str(submission.title), str(submission.author), str(submission.num_comments), str(submission.score), str(submission.url), str(datetime.fromtimestamp(submission.created_utc))]
        except Exception as e:
            msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
            sys.exit()

        ws.append(row)
        ws.append([""])
        row = ["comment ID", "author", "is OP", "reply depth", "reply to", "score", "body", "date"]
        ws.append(row)

        # replace "More Comments" to show all comments

        try:
            submission.comments.replace_more(limit=None)
        except Exception as e:
            msgbox("Error occured: " + str(e) + "\nSomething went wrong. Please check:\n-Credentials\n-URL\nand restart the application")
            sys.exit()

        appendBodyToWorksheet()

        if not os.path.exists('generatedFiles'):
            os.makedirs('generatedFiles')
        wb.save("generatedFiles" + os.path.sep + path)
        if(not(ynbox("file generated:\n" + os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "generatedFiles"+ os.path.sep + path + "\n\nConvert another post?"))):
            break