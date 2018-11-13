# -*- coding: utf-8 -*-

import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        """
        TODO: 将 item 结果以 JSON 形式保存到 Redis 数据库的 list 结构中
        """
        s = item['text']
        item['text'] =  re.sub(r'\s{2,}', '', s)
        dictstr = dict(item)
        jsonstr = json.dumps(dictstr)
        self.redis.lpush('flask_doc:items', jsonstr)
        return item

    def open_spider(self, spider):
        # 连接数据库
        self.key = "flask_doc:items"
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        if self.redis.exists(self.key):
            self.redis.delete(self.key)
