# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

database_url = 'http://localhost:5432'
conn = psycopg2.connect(database_url)

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
