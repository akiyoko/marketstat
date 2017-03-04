# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketstatItem(scrapy.Item):
    name = scrapy.Field()
    expected_value = scrapy.Field()
    preliminary_value = scrapy.Field()
    confirmed_value = scrapy.Field()
