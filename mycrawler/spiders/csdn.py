# -*- coding: utf-8 -*-
import scrapy
from mycrawler.items import MycrawlerItem


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = (
        'http://www.csdn.net/',
    )

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = MycrawlerItem()
            item['name'] = sel.xpath('a/@href').extract()
            yield item


