import scrapy
from ..items import SeccrawlItem
from ..utility import format_date


class HNSpider(scrapy.Spider):
    name = "thehackernews"
    start_urls = [
        "https://thehackernews.com/"
    ]
    website_date_format = "%B %d, %Y"

    def parse(self, response):
        '''Parses the homepage looking for news

        [Contract]
        @url https://thehackernews.com/
        @returns items 0
        @returns requests 1 8
        '''
        for href in response.xpath('//a[@class="story-link"]/@href').extract():
            request = scrapy.Request(
                href,
                callback=self.parse_article
            )
            yield request

    def parse_article(self, response):
        '''Parses the article to fill the item

        [Contract]
        @url https://thehackernews.com/2019/03/bithumb-cryptocurrency-hacked.html
        @returns items 1 1
        @returns requests 0 0
        @scrapes _id website title author image text date
        '''
        item = SeccrawlItem()
        item['_id'] = response.url
        item['website'] = "The Hacker News"
        item['title'] = response.xpath('//main//h1//text()').get()
        item['author'] = response.css('a[rel="author"]::text').get()
        item['image'] = response.xpath(
            '//div[contains(@class, "articlebody")]//img/@src'
        ).get()
        item['text'] = response.xpath(
            '//div[contains(@class, "articlebody")]//div[@dir="ltr"]/text()'
        ).extract()

        messy_date = response.xpath(
            '//div[@class="postmeta"]/span/text()').get()
        item['date'] = format_date(
            messy_date,
            self.website_date_format
        )

        return item
