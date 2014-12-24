import json
import time

class ReadJson:
    def __init__(self):
        self.jsonfile = 'items.jl'
    
    def GetItems(self):
        items = []
        f = open(self.jsonfile, 'r')
        for str_d in f.readlines():
            items.append(json.loads(str_d))
        return items

class SortWebPage:
    def sort_by_pub_time(self):
        items = ReadJson().GetItems()
        t1 = time.time()
        for item in items:
            t2 = time.mktime(time.strptime(item['pub_time'], "%Y-%m-%d %H:%M"))
            item['rank'] = t1 - t2
        return sorted(items, key = lambda item : item['rank'], reverse = False)
