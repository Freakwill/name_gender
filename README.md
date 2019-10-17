# name_gender
👫guess genders from names, and give names to a boy or a girl (only for Chinese names)

Inspirited by the classification of English names.

## New feature
Give name automaticly

    取名字:(给出性别和第一个字)
    女: 怡皓

## test results
Seperate the data as train (80%) and test(20%) data, before training and testing

    With Chinese:
    李春娜: 女
    Most Informative Features
                       first = '佳'                 女 : 男      =      3.0 : 1.0
                       first = '春'                 女 : 男      =      2.1 : 1.0
                       first = '易'                 女 : 男      =      2.1 : 1.0
                       first = '红'                 女 : 男      =      2.1 : 1.0
                       first = '怡'                 女 : 男      =      2.1 : 1.0
    With Pinyin:
    叶娅芬: 女
    Most Informative Features
                      second = 'jie'               男 : 女      =      4.3 : 1.0
                      second = 'qing'              女 : 男      =      3.5 : 1.0
                       first = 'chen'              女 : 男      =      2.4 : 1.0
                       first = 'chu'               女 : 男      =      2.4 : 1.0
                       first = 'chun'              女 : 男      =      2.4 : 1.0

## summary
1. Girls' names are repeated more likely then boy's. They are named simply by their parents.
2. Many boys have name with `jie`
