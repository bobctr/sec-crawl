import os
import random


class RandomUserAgentMiddleware:

    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent_list = crawler.settings.get('USER_AGENT_LIST'),
        )

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware:

    def __init__(self, http_proxy):
        self.http_proxy = http_proxy

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            http_proxy = crawler.settings.get('HTTP_PROXY')
        )

    def process_request(self, request, spider):
        request.meta['proxy'] = self.http_proxy
        spider.log('Proxy : %s' % request.meta['proxy'])