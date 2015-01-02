#encoding=utf-8
from __future__ import division
import jieba
import jieba.posseg as pseg
import os
import math, numpy
from collections import Counter

#该类用于对传入的正文进行操作从而对其进行分类
class Classifier:
    def cutWord(self, content):
        word_dic = {}
        words = pseg.cut(content)

        #过滤所不需要的词性,去重和统计TF
        for w in words:
            if (w.flag!="x" and w.flag!="uj" and w.flag!="c" and w.flag!="p"):
                if (w.flag!="u" and w.flag!="m" and w.flag!="r" and w.flag!="d"):
                    if (w.flag!="y" and w.flag!="e" and w.flag!="h" and w.flag!="k"):
                        if (w.flag!="ul" and w.flag!="uz" and w.flag!="f" and w.flag!="eng"):
                            if word_dic.has_key(w.word):
                                word_dic[w.word] += 1
                            else:
                                word_dic[w.word] = 1
        return word_dic

    def tf_idf(self, df_list, word_dic, sample_num):
        tf_idf_list = []
        for df_tuple in df_list:
            u_df_tuple_0 = unicode(df_tuple[0], "utf-8")
            if u_df_tuple_0 in word_dic: 
                tf_idf = word_dic[u_df_tuple_0] * math.log(sample_num / df_tuple[1])
                tf_idf_list.append(tf_idf)
            else:
                tf_idf_list.append(0)
        return tf_idf_list


    def classify(self, sample_vector_list, file_vector, k):
        similarity_tuple_list = []

        for sample_vector_tuple in sample_vector_list:
            class_num = sample_vector_tuple[0]
            sample_vector = sample_vector_tuple[1]
            file_vector = numpy.array(file_vector)
            
            similarity = 0
            vector_length = 0
            for attribute_tuple in sample_vector:
                similarity += attribute_tuple[1] * file_vector[attribute_tuple[0] - 1]
                vector_length += attribute_tuple[1] * attribute_tuple[1]

            similarity = similarity / (math.sqrt(vector_length) + 0.1) / (math.sqrt(numpy.dot(file_vector, file_vector) + 0.1))
            similarity_tuple_list.append((class_num, similarity))

        similarity_tuple_list = sorted(similarity_tuple_list, key = lambda item : item[1], reverse = True)

        top_k_list = []
        count = 0
        while count < k:            
            top_k_list.append(similarity_tuple_list[count][0])
            count += 1
		
        count_dic = Counter(top_k_list)
        count_list = sorted(count_dic.items(), key = lambda item : item[1], reverse = True)

        return count_list[0][0]

    #func : 用于分类	
    #param :content : 正文
    #	df_list : 这个list每一个元素为一个二元元组(attribute df)
    #	sample_num : 样本总数
    #	sample_vector_list : 该列表用于存放所有样本向量及其分类,每一个列表元素为一个二元元组(class_num, vector)
    #	k : knn算法中的k取值
    #return : 返回这个content的分类代码(0到12之间)
    def fun(self, content, df_list, sample_num, sample_vector_list, k):
        word_dic =  self.cutWord(content)
        file_vector = self.tf_idf(df_list, word_dic, sample_num)
        return self.classify(sample_vector_list, file_vector, k)
