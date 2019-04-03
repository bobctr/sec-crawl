# sec-crawl
[![CircleCI](https://circleci.com/gh/bobctr/sec-crawl.svg?style=svg)](https://circleci.com/gh/bobctr/sec-crawl)

Scraper that collects cybersecurity news from the web + React REST Client 

![](https://user-images.githubusercontent.com/33261444/55333954-eda49e80-54a0-11e9-91f7-bf7c5ac8aa87.gif)


## Scraped websites (so far)
  - SECURITY | Wired https://www.wired.com/category/security/
  - The Hacker News https://www.thehackernews.com

## References
https://en.wikipedia.org/wiki/Web_scraping

https://scrapy.org/

## What I have learned
Since the purpose of this project is mainly heuristic, I would like to point out a few key concepts I've learned about during my work:

### Web Scraper and server
  - what scraping is, how it works and how powerful can beand server
  - how to use **scrapy** to quickly implement a scraper basic structure
  - producing web requests and parsing the response using **xpath and css selectors** to extract significant data
  - **MongoDB database**, how it differs from relational databases, how to create an instance **to store scraped data** in and how to use the Mongo shell
  - how to use **Tor** (and **privoxy** to support SOCKS protocol) to prevent scraped websites from tracking your activity
  - how to set up a simple read-only **REST API interface** for the database
  - key Python modules used:
     * _scrapy_  -- for the web scraper
     * _pymongo_ -- MongoDB python API
     * _eve_     -- for setting up the REST server

### React client
  - **React libraries and structure** (JSX, components, props and state)
  - how to use **Material-UI** framework to create nice-looking and fluid UX 


----------------------------------------------------------------


## Setup

- [Scraper](seccrawl)
- [REST server](server)
- [React client](sec-crawl-react)
