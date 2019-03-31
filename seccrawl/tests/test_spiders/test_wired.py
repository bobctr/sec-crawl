import pytest
import os
import scrapy
from scrapy.http import Request, TextResponse
from seccrawl.spiders.wired_spider import WiredSpider
from seccrawl.utility import fake_response

def test_parse():
    response = fake_response('tests/test_spiders/mocks/mock_wired_home')

    ws = WiredSpider()
    articles = list(ws.parse(response))
    for link in articles:
        assert str.startswith(link.url, "https://www.wired.com/story/") 
    assert len(set(articles)) == len(articles)
    assert len(articles) in range(1,15)

def test_parse_article():
    response = fake_response('tests/test_spiders/mocks/mock_wired_article')
    ws = WiredSpider()
    item = ws.parse_article(response)
    assert item['author'] == 'Emily Dreyfuss'
    assert item['date'] == '2019-03-30'
    assert item['image'] == 'https://media.wired.com/photos/5c9ea193ee20947f575edc60/master/w_1684,c_limit/maleware-1094817202.jpg'
    assert item['title'] == 'Security News This Week: Google Play Store Has a Malware Problem'
    assert item['website'] == 'Security | WIRED'
    assert str.startswith(item['text'],
        'This week started off with one of tech’s biggest events of the '
          'year: an Apple product release. One of the most inter'
    )

