import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = [" https:"]
    start_urls = ["http:// https:/"]

    def parse(self, response):
        pass
