import scrapy

from vidstatsx_scrapy.items import VidstatsxScrapyItem

class MySpider(scrapy.spiders.Spider):
	name = "vidtop100"
	allowed_domains = ["vidstatsx.com"]
	start_urls = [ 
	"http://vidstatsx.com/youtube-top-100-most-subscribed-channels"
	]
# response.xpath('//div[@id="report-body"]/table/tbody/tr/td/a[contains(@href, "www.youtube.com")]/@href').extract()
	def parse(self, response):
		for sel in response.xpath('//div[@id="report-body"]/table/tbody/tr/td[1]'):
			item = VidstatsxScrapyItem()
			item['title'] = sel.xpath('a[1]/text()').extract()[0]
			item['link'] = sel.xpath('a[contains(@href, "www.youtube.com")]/@href')[0].re(r'//(.*)')[0]
			yield item

