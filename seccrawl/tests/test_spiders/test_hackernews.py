import pytest
import os
from scrapy.http import Request, TextResponse
from seccrawl.spiders.hackernews_spider import HNSpider
from seccrawl.utility import fake_response

def test_parse():
    response = fake_response('tests/test_spiders/mocks/mock_thn_home')
    ws = HNSpider()
    articles = list(ws.parse(response))
    assert len(set(articles)) == len(articles)
    assert len(articles) in range(1,8)

def test_parse_article():
    response = fake_response('tests/test_spiders/mocks/mock_thn_article')
    ws = HNSpider()
    item = ws.parse_article(response)
    assert item['author'] == 'Wang Wei'
    assert item['date'] == '2019-03-30'
    assert item['image'] == (
        'https://1.bp.blogspot.com/-wOHuEklO9e4/XJ8y7jUjU6I/AAAAAAAAzok/AxnBha-'
        'TdE4LsZlbe0R40z1ouDUfIMAwQCLcBGAs/s728-e100/bithumb-cryptocurrency-exchange-hacked.jpg'
    )
    assert item['title'] == 'Hackers Steal $19 Million From Bithumb Cryptocurrency Exchange'
    assert item['website'] == 'The Hacker News'
    assert len(item['text']) == 36 # lines

