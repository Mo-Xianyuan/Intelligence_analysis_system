# encoding: utf-8
#!/usr/bin/python

import os
from Classifier import Classifier

class Classifier_controller:

    def __init__(self):
        self.tf_idf = self.create_tf_idf()
        self.df_list = self.create_df_list()
        self.classes = self.create_classes()
        self.classifier = Classifier()

    def create_tf_idf(self):
        tf_idf = []
        os.system("pwd")
        path1 = './tutorial/data/tf_idf'
        classes = os.listdir(path1)
        for each_class in classes:
            path2 = path1 + '/' + each_class
            files = os.listdir(path2)
            for each_file in files:
                path3 = path2 + '/' + each_file     
                vector = dict()
                f = open(path3)
                dimes = f.readlines()
                f.close()
                i = 1
                for dime in dimes:
                    if float(dime) != 0.0:
                        vector[i] = float(dime)
                    i += 1
                tf_idf.append( (int(each_class), vector.items()) )
                print "creating class sample_vector...\n"
        print "finished..."
        return tf_idf

    def create_df_list(self):
        df_list = []
        f1 = open('./tutorial/data/df.dat')
        f2 = open('./tutorial/data/attribute.dat')
        df_records = f1.readlines()
        att_records = f2.readlines()
        f1.close()
        f2.close()
        i = 0
        for df in df_records:
            attribute = att_records[i].strip('\n')
            i += 1
            df_list.append((attribute, int(df)))
            print "reading %s %d\n" %(attribute, int(df))
        print "finished..."
        return df_list

    def create_classes(self):
        classes = []
        f = open('./tutorial/data/classes.dat')
        for each in f.readlines():
            classes.append(each.strip('\n'))
        f.close()
        return classes

    def get_classes(self, text, k):
        i = self.classifier.fun(text, self.df_list, len(self.tf_idf), self.tf_idf, k)
        return self.classes[i]

