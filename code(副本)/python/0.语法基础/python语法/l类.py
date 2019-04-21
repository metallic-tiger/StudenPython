#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 括号内为被 classname 继承的对象
class classname(object):
    
    #公有参数
    Elem1='op'
    Elem2=2

    #私有参数
    __pub='AS'

    #构造函数
    def __init__(self):
        print("I define one\'s Elem is  "+self.Elem1+' , two\'s Elem is ' +str(self.Elem2))
'''

__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方

反向运算符重载：

__radd__: 加运算
__rsub__: 减运算
__rmul__: 乘运算
__rdiv__: 除运算
__rmod__: 求余运算
__rpow__: 乘方
复合重载运算符：

__iadd__: 加运算
__isub__: 减运算
__imul__: 乘运算
__idiv__: 除运算
__imod__: 求余运算
__ipow__: 乘方
'''


if __name__ == "__main__":
    x=classname()

    
