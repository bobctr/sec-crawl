# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
import scrapy
import json

class MongoDBPipeline(object):
    collection_name = 'news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        for data in item:
            if data is None:
                raise DropItem ("Missing {0}!".format(data))
        self.db[self.collection_name].update_one(
            {'_id' : item['_id']},
            {'$set' : dict(item)},
            upsert = True
        )

        log.msg(
            "News added to MongoDB database!",
            level=log.DEBUG, spider=spider
        )
        return item