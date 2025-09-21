# NBA Stat Scraping
A set of web crawler scripts that scrape player information, and statistics. Can be used to fill CSV/Txt files or populate a database, depending on use cases or implementation.
(This repo is a template implementation)

## How It's Made:

**Tech used:** Selenium, Python, Flask, Docker

This uses a webscraper using selenium to pull from basketball reference. Registered clients have emails sent regularly through SMTP running on a Flask server through a cron job daily with their particular requested stats, organized to be digestible with my own particular insights on what I believe the trends will be moving forward.(Email Jadavila9 for more info)

## Optimizations:

Once this reaches a certain number of concurrent requests, FastApi would be a better option than Flask however not needing to update until all games are over allowing for as much time as needed to update daily stats makes this adequate. Can also look to using languages that support concurrency much better such as Go or Rust, or even Node with some clever Typescript could work in this situation. In the process of making this I ran into many issues with Beautiful Soup which led to me using Selenium as a solution to allow me to move quickly and iterate on, if I had to start over I would probably spend more time on the Beautiful Soup solution for a fairly measurable performance optimization.

## Lessons Learned:

I'm not sure if it's a result of the explosion of bots, however the html that some web apps produce is fairly difficult to reason about, which greatly improved my understanding of html and its document model truly being a tree. Learning to use docker to schedule and automate a part of the workflow felt like a rewarding skill to have picked up as well. 
