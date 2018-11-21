# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
from redis import StrictRedis


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        if item['score'] < 8.0:
            raise DropItem("score less than 8.0.")

        self.redis.lpush(self.key, json.dumps(dict(item)))
        
        return item


    def open_spider(self, spider):
        self.redis = StrictRedis()
        self.key = "douban_movie:items"

