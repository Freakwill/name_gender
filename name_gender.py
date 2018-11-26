#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import nltk

path = 'science.xls' # name list of students in zjc

for n in range(13, 18):
    class_ = 'xinji%d' % n
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
    if n == 13:
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
            if '(' not in name:
                featrues.append((get_feature(name), d['gender'].strip('()')))
            else:
                name = name.partition('(')[0]
                featrues.append((get_feature(name), d['gender'].strip('()')))
    return featrues

def example1():
    featrues = get_features(df, get_feature)

    # train-test
    N = len(featrues)
    T = int(N * 0.2)
    train = featrues[:T]
    test = featrues[T:]
    classifier = nltk.NaiveBayesClassifier.train(featrues)
    acc = nltk.classify.accuracy(classifier, test)
    print(acc)

    # predict
    gender = classifier.classify(get_feature('李春娜'))
    print(gender)

import pypinyin
def get_feature_pinyin(name):
    if len(name)==2:
        return {'first':'', 'second':name[-1]}
    else:
        return {'first':pypinyin.lazy_pinyin(name[-2])[0], 'second':pypinyin.lazy_pinyin(name[-1])[0]}

def example2():
    featrues = get_features(df, get_feature_pinyin)

    # train-test
    N = len(featrues)
    T = int(N * 0.2)
    train = featrues[:T]
    test = featrues[T:]
    classifier = nltk.NaiveBayesClassifier.train(featrues)
    acc = nltk.classify.accuracy(classifier, test)
    print(acc)

    # predict
    gender = classifier.classify(get_feature('李春娜'))
    print(gender)

print('With Chinese:')
example1()
print('With Pinyin:')
example2()