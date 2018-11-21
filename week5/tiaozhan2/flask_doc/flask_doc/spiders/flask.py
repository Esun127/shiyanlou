# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

import re



class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ["http://flask.pocoo.org/docs/1.0/"]
    
    page_link = LinkExtractor(allow=(r"docs/1.0/"))
    page_link = LinkExtractor(allow="http://flask.pocoo.org/docs/1.0/*")
    rules = (
        #Rule("TODO: 配置 Link Extractor，及爬取链接的规则，并合理定义其他相关参数"),
        Rule(page_link, callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        item = PageItem()
        """
        TODO:补充 url 和 text 的解析规则
        """
        item['url'] = response.url
        item['text'] = '\n'.join(response.css('::text').extract())
        '''
        for i in response.css('div.body'):
            t = i.xpath('.//*/text()').extract_first().strip()
            if t:
                item['text'] += (t + '\n')
        '''
        yield item
