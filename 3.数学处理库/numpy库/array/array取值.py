import numpy as np
#
#验证当中继承原本的属性
# 从矩阵当中创建
# #

##
#   .ndim   矩阵的维度
#   .shape  矩阵的形状
#   .size   矩阵元素的数量
#   .dtype  元素的类型
#   .itemsize 所占用的字节大小
#   .data   所处内存的位置
# 
# #

print(r'从矩阵中创建\n',np.mat('1,1;3,4'))
print(r'从矩阵中创建\n',np.array(np.mat('1 2; 3 4'), subok=True))

A=np.array([[1,0,0],[2,1,0],[3,2,1],[0,0,0]])
print(A)
print(r'维度：',A.ndim)
print(r'矩阵的类型（第一维的值，第二维的值：）',A.shape)
print(r'矩阵的大小(元素的数量)',A.size)
print('元素的类型',A.dtype)
print('这个表占用的内存大小（字节）',A.itemsize)
print('实际元素的缓冲区',A.data)
