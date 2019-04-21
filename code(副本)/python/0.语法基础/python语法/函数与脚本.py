#!/usr/bin/python3
# -*- coding:utf-8 -*-

#脚本需要加上面两行

def Fibfunction(n):
    F1=1
    F2=1
    i=2
    if n==1|n==2:
        return 1
    while i!=n:
       F3=F1+F2
       F1=F2
       F2=F3
       i+=1
    return F2

if __name__ == "__main__":
    print('这个是计算斐波那契数的脚本')
    n=int(input('第几个斐波那契数'))
    print(Fibfunction(n))
