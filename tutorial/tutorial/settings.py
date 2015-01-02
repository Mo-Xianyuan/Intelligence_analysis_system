# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
SCHEDULER_ORDER = 'BFO'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

#决定在pipelines.py文件中使用的类
ITEM_PIPELINES = {
    'tutorial.pipelines.DjangoItemPipeline': 200,
    #'tutorial.pipelines.dbWriterPipeline': 300,
    #'tutorial.pipelines.JsonWriterPipeline': 800,
}

#取消默认的useragent，使用新的useragent
DOWNLOADER_MIDDLEWARES = {  
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,  
    'tutorial.rotate_useragent.RotateUserAgentMiddleware' :400  
    } 

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLES = False

LOG_LEVEL = 'INFO'

#DjangoItem设置
import sys
sys.path.append('/home/dinosaur/projects/Intelligence_analysis_system/mysite5')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite5.settings'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
