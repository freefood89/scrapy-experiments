import scrapy

from sec.items import SecItem
import re

class SecSpider(scrapy.Spider):
    name = 'sec'
    allowed_domains = ['sec.gov']
    start_urls = [
        'https://www.sec.gov/cgi-bin/browse-edgar?CIK=t&owner=exclude&action=getcompany&count=100',
    ]

    def parse(self, response):
        for sel in response.xpath('//table[@class="tableFile2"]/tr'):
            item = SecItem()
            item['filing'] = sel.xpath('td[1]/text()').extract()
            item['link'] = sel.xpath('td[2]/a/@href').extract()
            item['date'] = sel.xpath('td[4]/text()').extract()
            print(item)
            yield item

        next_page = response.xpath("//input[@type='button']/@onclick")
        # print(next_page)
        if next_page:
            path = re.findall("'((?:.|\n)*?)'", next_page.pop().extract()).pop()
            url = 'https://www.sec.gov' + path
            yield scrapy.Request(url, self.parse)
