# -*- coding: utf-8 -*-
import scrapy
from scrapy_satplay.items import ScrapySatplayItem


class UplistSpider(scrapy.Spider):
    name = "uplist"
    allowed_domains = [""]
    start_urls = [
    	'file:///home/www/vlist.html',
    ]

    def parse(self, response):
    	print(response.xpath('//body').extract())
        for sel in response.xpath('//table/tbody/tr'):
			item = ScrapySatplayItem()
			item['vname'] = sel.xpath('td[2]/text()').extract()[0]
			item['vid'] = sel.xpath('td[3]/a/@href').re(r'event\?id=(.*)')[0]
			item['vidup'] = sel.xpath('td[4]/span/button[1]/@onclick').re(r"orderUp\(\'(.*)\',\s+\'(.*)\'\)")[1]
			item['viddown'] = sel.xpath('td[4]/span/button[2]/@onclick').re(r"orderDown\(\'(.*)\',\s+\'(.*)\'\)")[1]
			yield item
