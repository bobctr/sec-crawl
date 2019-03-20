import scrapy

class WiredSpider(scrapy.Spider):
    name = "wired"

    def start_requests(self):
        urls = [
            "https://www.wired.com/category/security"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s-%s.html' % (self.name, page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)