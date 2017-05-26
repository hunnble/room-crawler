# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from redis import Redis

redis = Redis()

class DoubanPipeline(object):
    def process_item(self, item, spider):
        if not item['title']:
            return item

        if redis.get(item['link']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            redis.set('title:' + item['link'], item['title'])
            return item

class DoubanContentPipeline(object):
    def process_item(self, item, spider):
        if not item['content']:
            return item

        if redis.get(item['link']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            redis.set('content:' + item['link'], item['content'])
            return item
