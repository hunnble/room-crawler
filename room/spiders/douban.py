# -*- coding: utf-8 -*-
import scrapy

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ['www.douban.com']
    start_urls = (
        'http://www.douban.com/group/145219/discussion?start=0',
        'http://www.douban.com/group/145219/discussion?start=50',
        'http://www.douban.com/group/145219/discussion?start=100',
        'http://www.douban.com/group/145219/discussion?start=150',
        'http://www.douban.com/group/145219/discussion?start=200',
        'http://www.douban.com/group/145219/discussion?start=250'
    )

    def parse(self, response):
        title_list = response.css('.olt .title')
        items = [
            {
                'title': item[0].extract(),
                'link': item[1].extract()
            } for item in zip(title_list.css('::attr(title)'), title_list.css('::attr(href)'))]

        return items
