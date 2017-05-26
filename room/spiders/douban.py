# -*- coding: utf-8 -*-

import scrapy
from scrapy.conf import settings
from room.items import DoubanItem, DoubanContentItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ['www.douban.com']
    start_urls = [
        'http://www.douban.com/group/145219/discussion?start=0'
    ]

    def parse(self, response):
        title_list = response.css('.olt .title')

        for item in zip(title_list.css('::attr(title)'), title_list.css('::attr(href)')):
            yield DoubanItem({'title': item[0].extract(), 'link': item[1].extract()})
            yield scrapy.Request(item[1].extract(), self.parse_content)

        total_num = int(response.css('.thispage::attr(data-total-page)').extract()[0])
        url_pair = response.url.split('start=')
        current_num = int(url_pair[-1]) + settings['PER_PAGE']

        if current_num < min(total_num, settings['MAX_NUM']):
            yield scrapy.Request(url_pair[0] + 'start=' + str(current_num), self.parse)

    def parse_content(self, response):
        content_list = response.css('.topic-content .topic-content p')
        yield DoubanContentItem({'content': ''.join(content_list.extract()), 'link': response.url})

