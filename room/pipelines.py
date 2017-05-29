# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from redis import Redis

redis = Redis()

class DoubanPipeline(object):
    def process_item(self, item, spider):
        if not item.get('title'):
            return item

        redis.hsetnx('douban-titles', item['link'], item['title'])
        return item

        # if redis.hexists('douban-titles', item['link']):
        #     raise DropItem("Duplicate item found: %s" % item)
        # else:
        #     redis.hmset('douban-titles', {item['link']: item['title']})
        #     return item

class DoubanContentPipeline(object):
    def process_item(self, item, spider):
        if not item.get('content'):
            return item

        redis.hsetnx('douban-contents', item['link'], item['content'])
        return item

        # if redis.hexists('douban-contents', item['link']):
        #     raise DropItem("Duplicate item found: %s" % item)
        # else:
        #     redis.hmset('douban-contents', {item['link']: item['content']})
        #     return item
