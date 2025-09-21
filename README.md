# NBA Stat Scraping
A set of web crawler scripts that scrape player information, and statistics. Can be used to fill CSV/Txt files or populate a database, depending on use cases or implementation.
(This repo is a template implementation)

## How It's Made:

**Tech used:** Selenium, Python, Flask, Docker

This uses browser drivers in selenium to scrape from basketball reference, then using handrolled decorators can write or read to/from the data store. Registered clients have emails sent regularly through SMTP running on a Flask server through a cron job daily with their particular requested stats, organized to be digestible with my own particular insights on what I believe the trends will be moving forward.(Email Jadavila9 for more info)

## Optimizations:

Once this reaches a certain number of concurrent requests, I will find a solution using a suitable language such as Go or Rust to handle the routing of data and emails to allow for a more performant application. In the process of making this I ran into many issues with Beautiful Soup which led to me using Selenium as a solution to allow me to move quickly and iterate on, if I had to start over I would probably spend more time on the Beautiful Soup solution for a fairly measurable performance optimization.

## Lessons Learned:

I'm not sure if it's a result of the explosion of bots, however the html that some web apps produce is fairly difficult to reason about, which greatly improved my understanding of html and its document model truly being a tree. Learning to use docker to schedule and automate a part of the workflow felt like a rewarding skill to have picked up as well. 
