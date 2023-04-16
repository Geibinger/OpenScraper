pip3 install easygui praw openpyxl pyinstaller

pyinstaller --onefile -w RedditToExcelScraper.py
mkdir RedditToExcelScraper
copy default_account.json RedditToExcelScraper
copy praw.ini RedditToExcelScraper
cd dist
copy RedditToExcelScraper.exe "../RedditToExcelScraper"

pause