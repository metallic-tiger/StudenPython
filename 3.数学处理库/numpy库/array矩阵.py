import numpy as np

#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#   object  数组(或者元祖)，或着是 嵌套数组(或者嵌套元祖)
#   dtype   元素的数据类型  默认不限定
#   copy    是否可以进行复制    【还没有试】
#   order   
# #
A=np.array([(1,1),(1,1),(1,0)])
B=np.array([(1,1),(1,1),(1)])
#与MATLAB不同 使用‘ ’不能分割元素
#矩阵中的行列必须对齐
#即：每个内涵的列表（或者元组）中的 长度必须相同
#   否者则会当做 以列表作为元素的 一维矩阵
# 
# #

#对齐的矩阵
print("我是对齐的矩阵\n",A)
#没有对齐的一维矩阵
print("我是对齐的矩阵\n",B)
