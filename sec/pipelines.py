# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

import datetime

class SecPipeline(object):
    def process_item(self, item, spider):
        try:
            assert 'date' in item and len(item['date']) > 0
            assert 'filing' in item and len(item['date']) > 0
            assert 'date' in item and len(item['date']) > 0
        except AssertionError as e:
            raise DropItem('A field is missing from %s' % item)
        else:
            return item
