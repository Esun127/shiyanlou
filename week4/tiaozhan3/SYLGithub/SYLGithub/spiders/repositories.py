# -*- coding: utf-8 -*-
import scrapy

from SYLGithub.items import RepositoryItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
#    allowed_domains = ['github.com']
    start_urls = [ 'https://github.com/shiyanlou?tab=repositories' ]

    def parse(self, response):
        for i in response.xpath('//li[contains(@class, "width-full")]'):
            item = RepositoryItem()

            item['name'] = i.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first(r'\s+(\S+)'),
            item['update_time'] = i.xpath('.//div[contains(@class, "f6")]/relative-time/@datetime').extract_first()
            
#??????
            i_url = i.xpath('.//div[contains(@class, "mb-1")]/h3/a/@href').extract_first()
            i_url = response.urljoin(i_url)
            request = scrapy.Request(i_url, callback=self.parse_detail)
            request.meta['item'] = item
            yield request



#??????
        nextpg= response.xpath('//div[@class="pagination"]/a')
        for page in nextpg:
            if page.xpath('.//text()').extract_first() == 'Next':
                url = page.xpath('.//@href').extract_first()
                yield scrapy.Request(url=url, callback=self.parse)


    def parse_detail(self, resp):
        item = resp.meta['item']
        data = resp.css('span.num.text-emphasized::text').re(r'.*(\d+).*')
        if not data:
            data = ['0','0','0','0']

        item['commits'] = data[0]
        item['branches'] = data[1]
        item['releases'] = data[2]
        

        yield item
            
