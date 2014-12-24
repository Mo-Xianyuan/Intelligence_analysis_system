#encoding=utf-8
class Pub_Time:
    def __init__(self):
        self.Pub_Time_Paths = [
            # qq.com 新闻页面上方的发布时间
            '//span[@class="article-time"]/text()',
            # finance.qq.com 页面上方发布时间
            '//span[@class="pubTime article-time"]/text()',
            # qq.com 图片右下角的发布时间
            '//div[@id="time_source"]/span/text()',
            # sohu.com 新闻页面上方的发布时间
            '//div[@class="time"]/text()',
            # sina.com 新闻页面上方的发布时间
            '//span[@class="time-source"]/text()'
        ]
    
    def Get_Time(self, response):
        for path in self.Pub_Time_Paths:
            pub_time = response.xpath(path).extract()
            if pub_time:
                return pub_time[0]
        return ''
