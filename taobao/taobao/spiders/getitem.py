# -*- coding: utf-8 -*-
import scrapy


class GetitemSpider(scrapy.Spider):
    name = 'getitem'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
