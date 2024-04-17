import scrapy


class BaidubaikeSpider(scrapy.Spider):
    name = "baidubaike"
    allowed_domains = ["baike.baidu.com"]
    start_urls = ["https://baike.baidu.com"]

    def parse(self, response):
        pass
