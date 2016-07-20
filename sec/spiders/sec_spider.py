import scrapy

from sec.items import SecItem

class SecSpider(scrapy.Spider):
    name = 'sec'
    allowed_domains = 'sec.gov'
    start_urls = [
        'https://www.sec.gov/cgi-bin/browse-edgar?CIK=t&owner=exclude&action=getcompany&count=100',
    ]

    def parse(self, response):
        filename = 'tmp.html'

        for sel in response.xpath('//table[@class="tableFile2"]/tr'):
            item = SecItem()
            item['filing'] = sel.xpath('td[1]/text()').extract()
            item['link'] = sel.xpath('td[2]/a/@href').extract()
            item['date'] = sel.xpath('td[4]/text()').extract()
            print(item)
            yield item