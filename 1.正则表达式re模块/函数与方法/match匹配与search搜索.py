#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re

m1 = re.match('oo%d','foo215312')   #匹配函数 第一个是表达式，第二个是被处理的字符串
# #
# 根据匹配规则匹配最开始遇到的字符串
# 
# 如果没有返回 ‘None’
# 例如：
#  ‘[a-z][a-z][a-z]’,'abcdefg' 返回 ‘abc’
#  ‘[a-z][a-z][1-2]’,'abcdefg' 返回 ‘abc’#
# #
if m1 is not None:   
    print(m1.group())        #显示匹配对象
else:
    
    