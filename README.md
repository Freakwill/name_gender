# name_gender
guess genders from names (only Chinese names)

Inspirited by the classification of English names.

## test results
    With Chinese:
    0.9772727272727273
    李春娜 女
    Most Informative Features
                       first = '佳'                 女 : 男      =      3.0 : 1.0
                       first = '春'                 女 : 男      =      2.1 : 1.0
                       first = '易'                 女 : 男      =      2.1 : 1.0
                       first = '红'                 女 : 男      =      2.1 : 1.0
                       first = '怡'                 女 : 男      =      2.1 : 1.0
    With Pinyin:
    0.9772727272727273
    李春娜 女
    Most Informative Features
                      second = 'jie'               男 : 女      =      4.3 : 1.0
                      second = 'qing'              女 : 男      =      3.5 : 1.0
                       first = 'chen'              女 : 男      =      2.4 : 1.0
                       first = 'chu'               女 : 男      =      2.4 : 1.0
                       first = 'chun'              女 : 男      =      2.4 : 1.0

## summary
1. Girls' names are repeated more likely then boy's. They are named simply by their parents.
2. Many boys have name with `jie`
