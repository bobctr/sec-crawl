# sec-crawl
[![CircleCI](https://circleci.com/gh/bobctr/sec-crawl.svg?style=svg)](https://circleci.com/gh/bobctr/sec-crawl)

Scraper that collects cybersecurity news from the web

## Requirements
  - Python3
  - MongoDB
  - Scrapy
  - Pymongo
  - Eve

## Setup
Before running the crawler, make sure the MongoDB service is up and running.
```
mongod
```

Now the crawler can store the scraped data.
You can launch all the available spiders together (scrape all websites) with the following command (add ```-p``` to run the spiders in parallel)
```
python run_crawler.py -p
```
If you want to launch a single spider instead (scrape only one website)
```
scrapy crawl [spider_name]
```

### Data storing
Scraped news are stored in a MongoDB local instance accessible at ```localhost:27017```
The name of the database is ```sec-crawl```.

### REST API
The stored data can be retrieved through a REST API service.
To launch the service:
```
python server/run.py
```

To get all the news, make a GET request to ```http://localhost:5000/news```

## Scraped websites (so far)
  - SECURITY | Wired https://www.wired.com/category/security/
  - The Hacker News https://www.thehackernews.com
