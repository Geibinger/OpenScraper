pip install easygui
pip install praw
pip install openpyxl
pip install datetime

pyinstaller --onefile -w RedditToExcelScraper.py
mkdir RedditToExcelScraper
copy default_account.json RedditToExcelScraper
copy praw.ini RedditToExcelScraper
cd dist
copy RedditToExcelScraper.exe "../RedditToExcelScraper"

pause