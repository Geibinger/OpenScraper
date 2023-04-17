# Open Scraper
This repository contains three projects. All three convert user data of a different source to a more easily manageable Excel file. For more information, visit the `README.md` file of the according folder.

## [Reddit Scraper](RedditScraper/README.md)

The Reddit scraper is capeable of converting a specified number of posts in a subreddit into a sorted Excel file. This file then contains the date about the post (`Title`, `Body`, `Author`, `Created`, `Score`, `Num Comments` and the `Permalink`) as well as data about every comment (`Comment`, `Author`, `Created`, `Score`, `Reply to`).

## [Twitter Scraper](TwitterScraper/README.md)

Similar to the Reddit scraper, the Twitter scraper converts a specified number of tweets of a givin user into a sorted Excel file. The contents include `Text`, `Author`, `Created`, `Retweets`, `Favorites` and `Reply to`. Note that for this to work, a `BASIC` subscription to the Twitter API is needed (~100$/month).

## [YouTube Scraper](YouTubeScraper/README.md)

The YouTube scraper converts all the comments of a given video ID into a sorted Excel file. The data includes following entries: `Comment`, `Author`, `Created`, `Likes`.

For detailed description of the code, refer to the `Explanation` section in the `README.md` files.