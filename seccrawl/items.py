# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SeccrawlItem(scrapy.Item):
    _id = scrapy.Field()  # url
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    website = scrapy.Field()
    image = scrapy.Field()
    date = scrapy.Field()