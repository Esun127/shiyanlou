#!/usr/bin/env python3
import scrapy

class LouPlusCourseSpider(scrapy.Spider):

    name = 'louplus_spider'
    
    start_urls = [ 'https://github.com/shiyanlou?tab=repositories' ]

    def parse(self, response):
        for item in response.xpath('//li[contains(@class, "width-full")]'):
            data = {
                'name': item.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first(r'\s+(\S+)'),
                'update_time': item.xpath('.//div[contains(@class, "f6")]/relative-time/@datetime').extract_first()
            }

            yield data
        
        nextpg= response.xpath('//div[@class="pagination"]/a')
        for page in nextpg:
            if page.xpath('.//text()').extract_first() == 'Next':
                url = page.xpath('.//@href').extract_first()
                print(url)
                yield scrapy.Request(url=url, callback=self.parse)
