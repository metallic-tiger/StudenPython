import re
def out(m):#输出匹配结果
    if m is not None:
        print(m.group())
    else:
        print(None)
    #
    # 数字字符集     %d  匹配所有的0-9数字相当于[0-9] %D为不匹配数字相当于[^0-9]
    # 字母数字字符集  %w  匹配所有的常规字符相当于[0-9a-zA-Z] %W为不匹配数字相当于[^0-9a-zA-Z]
    # 空格字符集     %s  匹配所有的空白字符相当于[\n\t\r\v\f] %S为不匹配数字相当于[^\n\t\r\v\f]
    # 字符边界匹配   %b  匹配单词（周围用空格字符隔开的字符串）
    # 
    # #
#1.匹配任意数量的字符
# \要用字符\进行转义 写法为\\d
# #
print('匹配任意数量的字符')
m=re.match('\\d+','123456A')
out(m)

#2.匹配字母字符集
# 
# #
print('匹配字母字符集')
m=re.match('\\w+','alsdkjalkA')
out(m)

#3.%s匹配空白
# 
# #
print(r'%s匹配空白')
m=re.match('\\s+\\w+','         A')
out(m)

#4.匹配字母字符集
# 

print('匹配字母字符集')
m=re.match('(\\b(\\w)+\\b)+','sdfsdf')
out(m)

# #
