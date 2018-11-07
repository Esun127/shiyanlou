# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker

from SYLGithub.items import RepositoryItem
from SYLGithub.models import engine, Repository

from datetime import datetime

class SylgithubPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, RepositoryItem):
            d = item['update_time']
            item['update_time'] = datetime.strptime(d, '%Y-%m-%dT%H:%M:%SZ')
            item['commits'] = int( item['commits'] )
            item['branches'] = int( item['branches'] )
            item['releases'] = int( item['releases'] )
            self.s.add(Repository(**item))



        return item

    def open_spider(self, spider):
        Session  = sessionmaker(engine)
        self.s = Session()

    def close_spider(self, spider):
        self.s.commit()
        self.s.close()
