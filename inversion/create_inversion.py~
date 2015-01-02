#!/usr/bin/env python
#encoding=utf-8

import jieba
import cPickle
import sys
sys.path.append('/home/dinosaur/projects/Intelligence_analysis_system')
from db_controlter import DB_controlter

class Create_Inversion(DB_controlter):
    def __init__(self):
        DB_controlter.__init__(self)
        self.inversion = dict()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS \
            inversion_posting_list( id int unsigned not null primary key, \
                                    value longtext collate utf8_bin not null)")
        self.update_inversion()
        
    def get_webpage_from_db(self):
        self.cursor.execute("SELECT * FROM WebPage_webpage")
        return self.cursor.fetchall()

    def add_a_posting_list(self, word_id, _dict):
        p = cPickle.dumps(_dict)
        self.cursor.execute(
            """INSERT INTO inversion_posting_list(id, value) VALUES ('%d', '%s')""" %(word_id, p))
    
    def get_a_posting_list(self, word_id):
        self.cursor.execute(
            "SELECT * FROM inversion_posting_list where id = %d" %word_id)
        return cPickle.loads(self.cursor.fetchall()[0][1])

    def update_inversion(self):
        for webpage in self.get_webpage_from_db():
            for word in jieba.cut_for_search(webpage[4]):
                if not word in self.inversion:
                    self.inversion[word] = dict()
                if not webpage[0] in self.inversion[word]:
                    self.inversion[word][webpage[0]] = 1   
                self.inversion[word][webpage[0]] += 1

class Search_Inversion(DB_controlter):
    def __init__(self):
        DB_controlter.__init__(self)
        self.inversion = Create_Inversion().inversion

    def get_webpage_by_id(self, doc_id):
        self.cursor.execute("SELECT * FROM WebPage_webpage where id = %d" %doc_id)
        return self.cursor.fetchall()

    def search(self, word):
        if not word in self.inversion:
            print('not found')
        else:
            i = 1
            for doc_id in self.inversion[search_word]:
                webpage = self.get_webpage_by_id(doc_id)
                print "(%d) %s" %(i, webpage[0][1])
                i += 1

if __name__ == '__main__':
    search_inversion = Search_Inversion()
    while True:
        word = raw_input('输入关键词:')

        # word是str类型,而索引中的键值是utf8类型的unicode
        # 因此需要将str转为unicode,用decode函数
        search_word = word.decode("utf8")
        search_inversion.search(search_word)
