#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
#正则表达式
str1="word"

#待匹配字符串
str2="word"
str3="words"
str4="abcd"

def out(m):#输出匹配结果
    if m is not None:
        print(m.group())
    else:
        print(None)

#匹配函数 match(正则表达式,待匹配的字符串)
#word 匹配 word
# 匹配成功 返回 word
# #
m=re.match(str1,str2)
out(m)

#word 匹配 words
# 匹配成功 返回 word
# #
m=re.match(str1,str3)
out(m)

#word 匹配 abcd
# 匹配失败 
# #
m=re.match(str1,str4)
out(m)
