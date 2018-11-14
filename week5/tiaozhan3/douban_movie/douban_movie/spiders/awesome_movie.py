# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban_movie.items import DoubanMovieItem

class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
        Rule(LinkExtractor(allow=r'\?from=subject-page$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['url'] = response.url
        i['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first()
        i['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first().strip()
        i['score'] = float(response.xpath('//strong/text()').extract_first())
        return DoubanMovieItem(i)




    def parse_start_url(self, response):
        yield self.parse_item(response)
