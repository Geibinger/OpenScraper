pip3 install easygui praw openpyxl pyinstaller

pyinstaller --onefile -w RedditToExcelScraper.py
mkdir RedditToExcelScraper
cp default_account.json RedditToExcelScraper
cp praw.ini RedditToExcelScraper
cd dist
cp RedditToExcelScraper "../RedditToExcelScraper"