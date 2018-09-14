
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

DOMAIN = 'pusheen.com'
URL = 'http://pusheen.com/'
class TestSpider(BaseSpider):
    name = DOMAIN
    allowed_domains = [ DOMAIN ]
    start_urls = [
        URL
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for url in hxs.select('//a/@href').extract():
            if DOMAIN not in url:
                continue
            if not ( url.startswith('http://') or url.startswith('https://') ):
                url= URL + url
            print( url )
            yield Request(url, callback=self.parse)
