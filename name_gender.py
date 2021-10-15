#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""通过姓名（汉字或拼音，猜测性别）

还能自动取名。这是你见过的最好玩的Bayes分类项目。*_*
"""

import pandas as pd
import numpy as np

import nltk

try:
    import pypinyin
except:
    print('If you want to use pinyin instead of characters, then you have to download pypinyin')

PATH = 'namelist.xls' # name list of students in zjc

classes = ['xinji%d' % n for n in range(13, 19)] + ['xinjiang1', 'xinjiang2']
for n, class_ in enumerate(classes):
    
    df = pd.read_excel(PATH, sheet_name=class_)
    if not (set(df.columns) & {'学号','no','No', 'no.', 'No.'}):
        df = pd.read_excel(PATH, sheet_name=class_, skiprows=1)
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
    """name -> feature dict
    feature: 
        X1: 最后第二个字或空，X2: 最后一个字
    """

    if len(name)==2:
        return {'first':'', 'second':name[-1]}
    elif len(name)>=3:
        return {'first':name[-2], 'second':name[-1]}
    else:
        print(name, 'is a invalid name!')
        return {'first':'', 'second':''}


def get_feature_pinyin(name):
    """name -> feature dict
    feature: 
        X1: 第二个字的拼音或空，X2: 最后一个字的拼音
    """

    if len(name)==2:
        return {'first':'', 'second':name[-1]}
    else:
        return {'first':pypinyin.lazy_pinyin(name[-2])[0], 'second':pypinyin.lazy_pinyin(name[-1])[0]}

# get all data
def get_data(df, get_feature=get_feature):
    # dataframe -> List[(feature dict, label),...]
    featrues = []
    for k, row in df.iterrows():
        name = row['name']; gender = row['gender']
        if isinstance(name, str):
            if ' ' in name:
                name = name.replace(' ', '')
            if '(' not in name:
                featrues.append((get_feature(name), gender.strip('() ')))
            else:
                name = name.partition('(')[0]
                featrues.append((get_feature(name), gender.strip('() ')))
    return featrues

def get_train_test(featrues, ratio=0.9):
    # 分割训练数据集、测试数据集
    N = len(featrues)
    T = int(N * ratio)
    train = featrues[:T]
    test = featrues[T:]
    return train, test

def gender_classifier(df, f=get_feature):
    data = get_data(df, f)
    train, test = get_train_test(data)
    classifier = nltk.NaiveBayesClassifier.train(train)
    acc = nltk.classify.accuracy(classifier, test)
    return classifier, acc

def show_gender(name, pinyin=False, show_acc=False):
    # 姓名 -> 性别
    f = get_feature_pinyin if pinyin else get_feature
    classifier, acc = gender_classifier(df, f)
    if show_acc:
        print(f'精确度: {acc:.4}')
    # predict
    gender = classifier.classify(f(name))
    print(f'{name}: {gender}')
    classifier.show_most_informative_features(10)


def give_name(first='欣', gender='女'):
    # 自动取名
    def get_data_(df, get_feature=get_feature):
        data = get_data(df, get_feature)
        return [({'gender':g, 'first':n['first']}, n['second']) for n, g in data]

    data = get_data_(df, get_feature)
    classifier = nltk.NaiveBayesClassifier.train(data)
    following = classifier.prob_classify({'gender':gender, 'first':first})
    x = following.generate()
    print(f'{gender}: {first}{x}')


if __name__ == '__main__':
    
    print('With Chinese:')
    show_gender("蔡徐坤")
    print('With Pinyin:')
    show_gender("曹楚奇", True)
    print('取名字:(给出性别和第一个字)')
    give_name(first='红')
