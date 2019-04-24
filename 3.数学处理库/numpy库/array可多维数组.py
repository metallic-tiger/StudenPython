import numpy as np

#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#   object  数组(或者元祖)，或着是 嵌套数组(或者嵌套元祖)
#   dtype   元素的数据类型  默认不限定
#   copy    是否可以进行复制    【还没有试】
#   order   存储方式            【还没有试】
#   subok   返回与基类相同的数组【没有试】
#   ndmin   生成的最小维度(几个括号)
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
print("我是对不齐，会变成一维矩阵的矩阵\n",B)

#dtype =   限定矩阵部的类型
# 只能限定到二维内部
# 即：第二个括号内部
# #
A=np.array([(1,2),(1,2)],dtype=int)
print(A)
A=np.array([('world'),('hello')],dtype=str)
print(A)
A=np.array([list('world'),list('hello')],dtype=str)
print(A)

#修改或者创建时使用了其他类型就换报错
# A=np.array([(1,2),(1,'wrong')],dtype=int)
#如果是int 放入 str矩阵中会自动转化成str类型
# #
A=np.array([(1,2),(1,2),(1,1)],ndmin=1)
print('维度1\n',A)
A=np.array([(1,2),(1,2),(1,1)],ndmin=2)
print('维度2\n',A)
A=np.array([(1,2),(1,2),(1,1)],ndmin=3)
print('维度3\n',A)
A=np.array([(1,2),(1,2),(1,1)],ndmin=4)
print('维度4\n',A)
#验证从自雷当中继承原本的属性
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
print('从矩阵中创建\n',np.mat('1,1;3,4'))
print('从矩阵中创建\n',np.array(np.mat('1 2; 3 4'), subok=True))

A=np.array([[1,0,0],[2,1,0],[3,2,1],[0,0,0]])
print(A)
print('维度：',A.ndim)
print('矩阵的类型（第一维的值，第二维的值：）',A.shape)
print(r'矩阵的大小(元素的数量)',A.size)
print('元素的类型',A.dtype)
print('这个表占用的内存大小（字节）',A.itemsize)
print('实际元素的缓冲区',A.data)

###
# arrray的方法函数
# .reshape(不同维度的大小)重置矩阵的大小  顺序先行后列
# 
# #

#
# np生成矩阵的函数
# np.zeros([对应维度的长度])
# np.ones([对应维度的长度],dtype=类型名)
# empty 根据内存状态随机出一个矩阵
# np.empty( (2,3) )#空的随机举证
# np.arange(起始,结尾,间隔)和range类似
# np.linspace(起始,结尾,分割数量)
# #
print('zeros()\n',np.zeros((3,5)))
print('ones()\n',np.ones((3,5)))
print('empty()\n',np.empty((3,5)))
print('arange(1,5,1)\n',np.arange(1,5,1))


#矩阵运算
# A+B A-B
# 
# 
# #
