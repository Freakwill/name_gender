from name_gender import *

import pytest
class Test_NG:
    # 函数级开始
    def test_chinese(self):
        print('With Chinese:')
        show_gender("蔡徐坤")
        assert True
    def test_pinyin(self):
        print('With Pinyin:')
        show_gender("蔡徐坤", True)
        assert True
    def test_give_name(self):
        print('取名字:(给出性别和第一个字)')
        give_name()
        assert True
        
if __name__ == '__main__':
    pytest.main("-s test_ng.py")
