import numpy as np

#创建一个行矩阵与列矩阵
# A行  ，  B列
# #

#对应的元素想乘相除加减
# 
# 
# #
A=np.array([[1,0,0],[0,1,0],[0,0,1]])
B=np.array([[1,0,0],[2,1,0],[3,2,1]])
print(A-B)
print(A+B)
print(A*B)
print(A/B)
print(A%B)
print(B**5)


#   .dot(矩阵乘法)
# 矩阵乘法
#       注意
# 左右互换结果不同
# 矩阵的维度必须相同
# 
# #
print("B**A\n",B**A,A**B)

A=np.array([[1,1]])
B=np.array([[1],[1]])
print('A:',A)
print('B:',B)

print((A.dot(B)))
print((B.dot(A)))
