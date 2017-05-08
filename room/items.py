# -*- coding: utf-8 -*-

import scrapy

class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
