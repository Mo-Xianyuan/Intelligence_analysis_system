#encoding=utf-8
import scrapy
import time
from tutorial.items import newsItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from Pub_Time import Pub_Time
#提取正文
from readability.readability import Document
#布隆过滤器
from pybloomfilter import BloomFilter
from WebSite import WebSite
#用于分类
from tutorial.Classifier_controller import Classifier_controller
from WebPage.models import webpage
#用于去重
from Simhash_with_weight import Simhash

def LevelIsVaild(level):
    return level <= 0

class newsSpider(scrapy.Spider):

    name = "newsSpider"

    def __init__(self, website=None, *args, **kwargs):
        super(newsSpider, self).__init__(*args, **kwargs)
        self.bf = BloomFilter(10000000, 0.01, 'bloom UrlFilter')
        self.hash_bf = BloomFilter(10000000, 0.01, 'bloom HashFilter')
        self.allowed_domains = []
        self.start_urls = []
        self.ws = WebSite()
        for ad in self.ws.get_allowed_domains():
            self.allowed_domains.append(ad)
        for su in self.ws.get_start_urls(): 
            self.start_urls.append(su)
        #对象cc复制处理分类
        self.cc = Classifier_controller()

    def parse(self, response):
        
        #如果页面是新的
        if not self.bf.add(response.url):
            pt = Pub_Time()          
            item = newsItem()
            level = response.meta.get('level', 0)
            if pt.Get_Time(response):
                text = Document(response.body).summary()
                import re
                pattern = re.compile(r'<.*?>')
                hash_value = Simhash(text)
                pages = webpage.objects.all()
                #如果网页没有内容重复
                dup_flag = False
                for page in pages:
                    if hash_value.isDuplicate(page.hash_value):
                        dup_flag = True
                        break
                if not dup_flag:
                    item['text'] = pattern.sub('', text)          
                    item['classes'] = self.cc.get_classes(item['text'], 10)
                    item['intro'] = '' 
                    item['title'] = response.xpath('/html/head/title/text()').extract()[0]     
                    item['link'] = str(response.url)
                    item['pub_time'] = pt.Get_Time(response)
                    item['dow_time'] = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
                    item['website'] = ''
                    item['hash_value'] = hash_value.__float__()
                    yield item

            for url in response.xpath('//a/@href').extract():
                import urlparse
                abs_url = urlparse.urljoin(response.url, url.strip())
                if LevelIsVaild(level):
                    yield scrapy.Request(abs_url, callback=self.parse, meta={'level': level + 1})
    
    def closed(self, reason):
        print "------------------>3<----------------------"
        f = open('newsSpider.log', 'aw')
        f.write(u"爬完一轮，结束时间：%s" %time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())))
        f.close()
