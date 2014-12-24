# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class newsItem(scrapy.Item):
    
    title = scrapy.Field()
    link = scrapy.Field()
    intro = scrapy.Field()
    pub_time = scrapy.Field()
    dow_time = scrapy.Field()
    text = scrapy.Field()
    classes = scrapy.Field()
    website = scrapy.Field()
    hash_value = scrapy.Field()
    pass

from scrapy.contrib.djangoitem import DjangoItem
from WebPage.models import webpage

class WebPageItem(DjangoItem):
    django_model = webpage
