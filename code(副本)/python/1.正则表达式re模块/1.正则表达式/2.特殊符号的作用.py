#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
def out(m):#输出匹配结果
    if m is not None:
        print(m.group())
    else:
        print(None)

#或操作
str1="a|b"
#'a'与‘b’均可以匹配成功
m=re.match(str1,'a')
out(m)
m=re.match(str1,'b')
out(m)
#只能匹配到a 而匹配不到‘a|b’
m=re.match(str1,'a|b')
out(m)

#使用转义符号 \转义
m=re.match('a\|b','a|b')
out(m)
#字符       用途                    正则表示           样例        转义为普通片段
# |         或操作                  表达式1|表达式2      a|b       \|
# .         匹配任意非‘\n’的字符        .                  .       \.
# ^         匹配起始部分             ^表达式            ^hello     \^
# $         匹配结尾部分              表达式$          hello$      \$ 
# *         前方表达式匹配0到多次的    表达式*          [a-z]*      \*
# +         前方表达式匹配1到多次的     表达式+         [a-z]+      \+
# ?         前方表达式匹配0或1次的      表达式？        [a-z]?      \?
# {N}       前方表达式匹配N次的         表达式{N}      [a-z]{5}     \{\}
# {N,M}     前方表达式匹配N到M次的     表达式{N,M}     [a-z]{5,8}   
# […]       匹配[]中的任意一个字符     [字符集合]       [abc]        \[\]
# […a-z…]   匹配[a-z]之间的任意一个字符 [字符集合]       [a-z]        
# [^…]      不匹配[]中的任意一个字符     [字符集合]       [^abc]
# ()        封闭表达式                  (表达式)        ([0-9]{12}) \(\)
# 
# #
print("或操作")
m=re.match('a|b','a')
out(m)

print(".匹配")
m=re.match('a.b','aTb')
out(m)

print("^匹配文本头")
m=re.match('^hello','hello world')
out(m)


print("$匹配文本尾")
m=re.match(r'[a-z\s]*world$','hello world')
out(m)

print("*任意匹配次数")
m=re.match(r'[a-z]*','hello world')
out(m)

print("+ 1-多次匹配")
m=re.match(r'[a-z]+','hello world')
out(m)

print("？ 0-1次匹配")
m=re.match(r'[a-z]?','hello world')
out(m)

print("{N} 制定匹配次数")
m=re.match(r'[a-z]{5}','hello world')
out(m)

print("{N，M} 匹配一定范围次数")
m=re.match(r'[a-z]{2,5}','hello world')
out(m)

print("拒绝匹配的字符集")
m=re.match(r'[^a-z]','hello world')
out(m)

print("（）集合化")
m=re.match(r'([a-z]{5})','hello world')
out(m)

