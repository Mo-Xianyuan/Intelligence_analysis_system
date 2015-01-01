#!/usr/bin/env python
#encoding=utf-8

import jieba


#该类主要用simhash算法判断是否重复
#simhash算法将网页内容通过 特征提取 + 哈希 使得每一个内容对应一个固定位数的二进制哈希值(此类实现中为128位二进制)
#有点在于:当网页内容越相近，哈希值的二进制表示相同位数越多
#主要函数：1. simhash 用于返回网页对应simhash值，以便储存在数据库中   
#         2. isDuplicate 用于判断传入simhash值是否跟该正文对应simhash值足够相似
class Simhash():
    def __init__(self, content, hashbits=128):
        self.hashbits = hashbits
        #for item in jieba.cut(content):
        #    print item

        self.hash = self.simhash(content)


    def __str__(self):
        return str(self.hash)

    def __long__(self):
        return long(self.hash)

    def __float__(self):
        return float(self.hash)


    #func : 用于计算simhash值    
    #param :content : 网页正文内容
    #return : 返回这个content的对应simhash值(128)
    def simhash(self, content):
        #首先将content进行分词，为每个词统计词频作为权重
        word_dic = {} 
        for item in jieba.cut(content):
            if word_dic.has_key(item):
                word_dic[item] += 1
            else :
                word_dic[item] = 1

        tokens = word_dic.keys()
        #print len(tokens)
        #for item in tokens:
            #print item

        # 用一个数组表示哈希值的每一位，初始化为0
        v = [0]*self.hashbits

        count = 0
        for item in tokens:
            count += 1
            #if word_dic[item] != 1 :
            #    print item + "  " + str(word_dic[item])
                
            raw_hash = self._string_hash(item)
            bitmask = 0
            
            for i in range(self.hashbits):
                bitmask = 1 << i
                #print(raw_hash,bitmask, raw_hash & bitmask)
                if raw_hash & bitmask:
                    v[i] += word_dic[item] #查看当前bit位是否为1，是的话则将该位+分词权重(词频)
                else:
                    v[i] -= word_dic[item] #否则得话，该位-分词权重(词频)

        #print count
        
        #数组每一位皆为0或1，将其所对应的十进制数计算出来
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        
        return fingerprint

    def _string_hash(self, v):
        # A variable-length version of Python's builtin hash
        if v == "":
            return 0
        else:
            x = ord(v[0])<<7
            m = 1000003
            mask = 2**self.hashbits-1
            for c in v:
                x = ((x*m)^ord(c)) & mask
            x ^= len(v)
            if x == -1:
                x = -2
            return x


    #func : 用于计算传入simhash值跟该正文simhash值的hamming distance(即二进制表示中有多少位不同)
    #param :other_hash : 用于跟当前正文simhash值进行比较的哈希值
    #return : 返回传入simhash值跟该正文simhash值的hamming distance
    def hamming_distance(self, other_hash):
        x = (self.hash ^ other_hash) & ((1 << self.hashbits) - 1)
        hamming_distance = 0
        while x:
            hamming_distance += 1
            x &= x-1
        return hamming_distance


    #func : 用于计算传入simhash值跟该正文simhash值的相似度(两数相除)
    #param :other_hash : 用于跟当前正文simhash值进行比较的哈希值
    #return : 用于计算传入simhash值跟该正文simhash值的相似度
    def similarity(self, other_hash):
        a = float(self.hash)
        b = float(other_hash)
        if a > b: 
            return b / a
        return a / b

    #func : 用于判断传入simhash值是否跟该正文对应simhash值足够相似
    #param :other_hash : 用于跟当前正文simhash值进行比较的哈希值
    #return : 判断输入是否simhash值是否跟当前正文对应simhash值足够相似
    def isDuplicate(self, other_hash):
        if self.hamming_distance(other_hash) < 3:
            return True
        else:
            return False



if __name__ == '__main__':
    #测试
    s1 = '退市新政大幕开启，首家触及“红线”的上市公司已浮出水面。７月２３日，闽灿坤Ｂ（２００５１２）公告称，从７月９日至７月２０日止，，股票已连续１０个交易日每日收盘价低于每股面值１元人民币，如果在之后的１０个交易日此类情形没有消除，股票将可能被终止上市。'

    s2 = '退市新政大幕开启，首家触及“红线”的上市公司已浮出水面。７月２３日，闽灿坤Ｂ（２００５１２）公告称，从７月９日至７月２０日止，，股票已连续１０个交易日每日收盘价低于每股面值１元人民币，如果在之后的１０个交易日此类情形没有消除，股票将可能被终止上市。由此，闽灿坤Ｂ将相关公司股票走势成为首家因新规退市的公司。'

    hash1 = Simhash(s1)
    print hash1
    #print("0x%x" % hash1)
    #print ("%s\t0x%x" % (s1, hash1))

    hash2 = Simhash(s2)
    print hash2
    #print ("%s\t[simhash = 0x%x]" % (s2, hash2))

    print '%f%% percent similarity on hash' %(100*(hash1.similarity(hash2)))
    print hash1.hamming_distance(hash2),"bits differ out of", hash1.hashbits
