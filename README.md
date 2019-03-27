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

## Using Tor
If you want your spiders to make request via Tor, do the following:

1. Install Tor and Privoxy
```
sudo apt install tor
sudo apt install privoxy
```

2. Configure Privoxy to route all the incoming requests to Tor.
   Add this to ```/etc/privoxy/config``` (path on Linux)
```
forward-socks5 / 127.0.0.1:9050 .
```

3. Restart the services
```
sudo service tor restart
sudo service privoxy restart
```

4. Once you set all up, everytime you want to scrape through Tor, uncomment these lines in ```seccrawl/settings.py```
```python
DOWNLOADER_MIDDLEWARES = {
    'seccrawl.middlewares.RandomUserAgentMiddleware': 400,
    'seccrawl.middlewares.ProxyMiddleware': 410,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
}
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
