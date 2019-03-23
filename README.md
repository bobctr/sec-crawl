# sec-crawl
[![CircleCI](https://circleci.com/gh/bobctr/sec-crawl.svg?style=svg)](https://circleci.com/gh/bobctr/sec-crawl)

Scraper that collects cybersecurity news from the web

## Requirements
  - Scrapy
  - Pymongo
  - Eve

```
pip install -r requirements.txt
```

### Data storing
Scraped news are stored in a MongoDB local instance accessible at ```localhost:27017```

### REST API
The stored data can be retrieved through a REST API service.
To launch the service:
```
python server/run.py
```

To make a request of all the news do make a GET request to ```http://127.0.0.1:5000/news```

### Scraped websites (so far)
  - SECURITY | Wired https://www.wired.com/category/security/
