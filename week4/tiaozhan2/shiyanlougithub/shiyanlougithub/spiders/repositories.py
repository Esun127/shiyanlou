# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    allowed_domains = ['github.com']

    start_urls = [ 'https://github.com/shiyanlou?tab=repositories' ]

    def parse(self, response):
        for item in response.xpath('//li[contains(@class, "width-full")]'):
            yield  ShiyanlougithubItem( {
                'name': item.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first(r'\s+(\S+)'),

                'update_time': item.xpath('.//div[contains(@class, "f6")]/relative-time/@datetime').extract_first()
                } )


        nextpg= response.xpath('//div[@class="pagination"]/a')
        for page in nextpg:
            if page.xpath('.//text()').extract_first() == 'Next':
                url = page.xpath('.//@href').extract_first()
                yield scrapy.Request(url=url, callback=self.parse)
