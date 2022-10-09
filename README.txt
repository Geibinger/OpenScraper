RedditToExcelScraper
Copyright Friedl Jakob 2021
----------------------------------------------------------------------------------

How to install:
-Python and PIP need to be installed beforehand
-doubbleclick on install.bat to start the installation
-the installed program can be found in the RedditToExcelScraper folder
-to run the program, praw.ini and default_account.json need to be in the same folder
-update the default_account.json file with the information about your reddit application
	(can be created underhttps://www.reddit.com/prefs/apps)

----------------------------------------------------------------------------------

How to setup Reddit-app:
-goto https://www.reddit.com/prefs/apps, login and click on "create another app..."
	on the bottom side of the page
-choose a describtive name for the app (this is important, otherwise the app cant be used,
	do not call it any variation of "RedditScraper")
-choose "script"
-at "description" make sure to write abit about your usage (again, if there is not enough information,
	the app cant be used)
-"about url" can be left blank
-for "redirect uri" fill in "http://localhost:8080"
-finish by clicking on "create app"

After creating the app, the client_id can be found beneath the application name
in the top left corner. The other fields should be self explanatory.

The information of the Reddit app is needed to connect to the Reddit API in the RedditToExcelScraper program.