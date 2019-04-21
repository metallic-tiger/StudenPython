import re
def out(m):#输出匹配结果
    if m is not None:
        print(m.group())
    else:
        print(None)
