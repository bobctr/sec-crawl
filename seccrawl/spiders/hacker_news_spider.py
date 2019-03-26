import scrapy
from ..items import SeccrawlItem
from ..utility import format_date

class HNSpider(scrapy.Spider):
    name = "thehackernews"
    start_urls = [
        "https://thehackernews.com/"
    ]
    website_date_format = "%B %d, %Y"

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse)

    def parse(self, response):
        for href in response.xpath('//a[@class="story-link"]/@href').extract():
            request = scrapy.Request(
                href,
                callback = self.parse_article
            )
            yield request

    def parse_article(self, response):
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
            '//div[@class="postmeta"]/span/text()'
        ).get()
        item['date'] = format_date(
            messy_date,
            self.website_date_format
        ) 
  
        return item
