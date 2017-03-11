# -*- coding: utf-8 -*-

from datetime import datetime
import scrapy
from pytz import timezone

from ..items import MarketstatItem


class BojSpider(scrapy.Spider):
    name = "boj"
    allowed_domains = ["www3.boj.or.jp"]
    date = datetime.now(timezone('Asia/Tokyo')).strftime('%y%m%d')
    start_urls = [
        'http://www3.boj.or.jp/market/jp/stat/jx{date}.htm'.format(date=date),
    ]

    def __init__(self, date=None, *args, **kwargs):
        super(BojSpider, self).__init__(*args, **kwargs)
        if date is not None:
            self.date = date
            self.start_urls = [
                'http://www3.boj.or.jp/market/jp/stat/jx{date}.htm'.format(date=self.date),
            ]

    def parse(self, response):
        for sel in response.css('table tr'):
            item = MarketstatItem()
            item['date'] = self.date
            item['name'] = sel.css('td::text').extract_first()
            item['expected_value'] = remove_comma(sel.css('td:nth-last-child(3)::text').extract_first())
            item['preliminary_value'] = remove_comma(sel.css('td:nth-last-child(2)::text').extract_first())
            item['confirmed_value'] = remove_comma(sel.css('td:nth-last-child(1)::text').extract_first())
            yield item


def remove_comma(val):
    """Remove comma if exists"""
    if isinstance(val, basestring):
        return val.replace(',', '')
    return val
