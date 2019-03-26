import scrapy
from ..items import SeccrawlItem
from ..utility import format_date

class WiredSpider(scrapy.Spider):
    name = "wired"
    start_urls = [
        "https://www.wired.com/category/security"
    ]
    website_date_format = "%m.%d.%y"

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse)

    def parse(self, response):
        for href in response.css("div.card-component a:not([href^='/author'])::attr(href)").extract():
            request = scrapy.Request(
                'https://www.wired.com' + href,
                callback = self.parse_article
            )
            yield request

    def parse_article(self, response):
        item = SeccrawlItem()
        item['_id'] = response.url
        item['website'] = 'Security | WIRED'
        item['title'] = response.css('h1.title::text').get()
        item['author'] = response.css('a[rel="author"]::text').get()
        item['image'] = response.xpath(
            '//div[@class="article-lede-component__image-wrapper"]//img/@src'
        ).get()
        item['text'] = response.xpath('normalize-space(//article)').get()                
                
        messy_date = response.xpath('//time/text()').get()
        item['date'] = format_date(
            messy_date,
            self.website_date_format
        )

        return item
        