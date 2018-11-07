# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlougithub.items import ShiyanlougithubItem
from shiyanlougithub.models import engine, Repository
from datetime import datetime

class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ShiyanlougithubItem):
            d = item['update_time'] 
            item['update_time'] = datetime.strptime(d, '%Y-%m-%dT%H:%M:%SZ')
            self.s.add(Repository(**item))
        return item


    def open_spider(self, spider):
        Session = sessionmaker(engine)
        self.s = Session()




    def close_spider(self, spider):
        self.s.commit()
        self.s.close()
