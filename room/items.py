# -*- coding: utf-8 -*-

from scrapy import Item, Field

class DoubanItem(Item):
    title = Field()
    link = Field()

class DoubanContentItem(Item):
    content = Field()
    link = Field()
