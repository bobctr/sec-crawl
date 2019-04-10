# -*- coding: utf-8 -*-

# Scrapy settings for seccrawl project

import os
from urllib.parse import quote_plus

BOT_NAME = 'seccrawl'

SPIDER_MODULES = ['seccrawl.spiders']
NEWSPIDER_MODULE = 'seccrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


######################################################################################
### if you want your spiders to crawl via -> privoxy -> tor, uncomment these lines ###

# DOWNLOADER_MIDDLEWARES = {
#     'seccrawl.middlewares.RandomUserAgentMiddleware': 400,
#     'seccrawl.middlewares.ProxyMiddleware': 410,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
# }

######################################################################################


# for random user agent when using the middleware
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]

# proxy location
HTTP_PROXY = 'http://127.0.0.1:8118'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'seccrawl.pipelines.MongoDBPipeline' : 100,
    # 'seccrawl.pipelines.JsonWriterPipeline' : 200,
 }

MONGO_URI = 'mongodb://127.0.0.1:27017'
try:
    from .dev_settings import MONGO_URI
except:
    pass
MONGO_DATABASE = 'sec-crawl'

