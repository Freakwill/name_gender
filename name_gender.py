#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import nltk

path = 'namelist.xls' # name list of students in zjc

classes = ['xinji%d' % n for n in range(13, 18)] + ['xinjiang1', 'xinjiang2']
for n, class_ in enumerate(classes):
    
    df = pd.read_excel(path, sheet_name=class_)
    if not (set(df.columns) & {'学号','no','No', 'no.', 'No.'}):
        df = pd.read_excel(path, sheet_name=class_, skiprows=1)
    if 'name' in df.columns:
        name_key = 'name'
    else:
        name_key = '姓名'
    if 'gender' in df.columns:
        gender_key = 'gender'
    else:
        gender_key = '性别'
    df = df[[name_key, gender_key]]
    df.dropna()
    if n == 0:
        data = df.values
    else:
        data = np.vstack((data, df.values))

# get raw data from xls file
df = pd.DataFrame(data=data, columns=('name', 'gender'))

def get_feature(name):
    # name -> feature dict
    if len(name)==2:
        return {'first':'', 'second':name[-1]}
    else:
        return {'first':name[-2], 'second':name[-1]}

# get all data
def get_features(df, get_feature):
    featrues = []
    for row in df.iterrows():
        d = dict(row[1])
        name = d['name']
        if isinstance(name, str):
            if ' ' in name:
                name = name.replace(' ', '')
            if '(' not in name:
                featrues.append((get_feature(name), d['gender'].strip('() ')))
            else:
                name = name.partition('(')[0]
                featrues.append((get_feature(name), d['gender'].strip('() ')))
    return featrues

def get_train_test(featrues):
    # split the data into train part and test part
    N = len(featrues)
    T = int(N * 0.2)
    train = featrues[:T]
    test = featrues[T:]
    return train, test

def example1():
    featrues = get_features(df, get_feature)
    train, test = get_train_test(featrues)
    classifier = nltk.NaiveBayesClassifier.train(featrues)
    acc = nltk.classify.accuracy(classifier, test)
    print(acc)

    # predict
    new_name = '李春娜'
    gender = classifier.classify(get_feature(new_name))
    print('李春娜', gender)
    classifier.show_most_informative_features(10)

import pypinyin
def get_feature_pinyin(name):
    if len(name)==2:
        return {'first':'', 'second':name[-1]}
    else:
        return {'first':pypinyin.lazy_pinyin(name[-2])[0], 'second':pypinyin.lazy_pinyin(name[-1])[0]}

def example2():
    featrues = get_features(df, get_feature_pinyin)
    train, test = get_train_test(featrues)
    classifier = nltk.NaiveBayesClassifier.train(featrues)
    acc = nltk.classify.accuracy(classifier, test)
    print(acc)

    # predict
    new_name = '李春娜'
    gender = classifier.classify(get_feature(new_name))
    print('李春娜', gender)
    classifier.show_most_informative_features(5)

print('With Chinese:')
example1()
print('With Pinyin:')
example2()