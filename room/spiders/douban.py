# -*- coding: utf-8 -*-

import scrapy
from room.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ['www.douban.com']
    start_urls = [
        'http://www.douban.com/group/145219/discussion?start=0'
    ]

    def parse(self, response):
        title_list = response.css('.olt .title')

        items = [
            DoubanItem({
                'title': item[0].extract(),
                'link': item[1].extract()
            }) for item in zip(title_list.css('::attr(title)'), title_list.css('::attr(href)'))]

        for item in items:
            yield item

        total_num = int(response.css('.thispage::attr(data-total-page)').extract()[0])
        url_pair = response.url.split('start=')
        current_num = int(url_pair[-1]) + 50

        if current_num < min(total_num, 300):
            yield scrapy.Request(url_pair[0] + 'start=' + str(current_num), self.parse)
