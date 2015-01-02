# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

import mysql.connector
import MySQLdb
from tutorial.items import WebPageItem

class DjangoItemPipeline(object):
    def process_item(self, item, spider):
        DjangoItem = WebPageItem()
        DjangoItem['title'] = item['title']
        DjangoItem['intro'] = item['intro']
        DjangoItem['link'] = item['link']
        DjangoItem['text'] = item['text']
        DjangoItem['cate'] = item['classes']
        DjangoItem['pub_time'] = item['pub_time']
        DjangoItem['dow_time'] = item['dow_time']
        DjangoItem['website'] = item['website']
        DjangoItem['hash_value'] = item['hash_value']
        DjangoItem.save()

class dbWriterPipeline(object):

    def __init__(self):
        self.db = mysql.connector.connect(
            user='root', passwd='271828', db='crawl_item_db', 
            host='127.0.0.1', charset="utf8",  use_unicode=True, raise_on_warnings=False
        )
        self.cursor = self.db.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS \
            news_items_table(   id int unsigned not null auto_increment primary key, \
                                title nvarchar(255) not null, \
                                link nvarchar(255) not null, \
                                intro longtext collate utf8_bin not null, \
                                pub_time nvarchar(32) not null, \
                                dow_time nvarchar(32) not null, \
                                text longtext collate utf8_bin not null, \
                                classes nvarchar(255) not null)")

        self.sqli = """INSERT INTO news_items_table(title, link, intro, pub_time, dow_time, text, classes) \
                     VALUES ('%s','%s','%s','%s','%s','%s','%s')"""

    def process_item(self, item, spider):
        if item['pub_time']:
            self.cursor.execute(self.sqli % (item['title'], 
                                             item['link'],
                                             item['intro'],
                                             item['pub_time'],
                                             item['dow_time'],
                                             MySQLdb.escape_string(item['text']),
                                             item['classes']))
            self.db.commit()
            return item
        else:
            raise DropItem("Missing pub_time")

import codecs
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.jl', 'wb')

    def process_item(self, item, spider):
        if item['pub_time']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing pub_time")
    
