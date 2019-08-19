import  tensorflow as tf
import  numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.5+0.3

Weights =  tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases

###损失函数###
#描述了 经由运算图产生的数据与实际数据之间的区别 用于反向传播
loss = tf.reduce_mean(tf.square(y-y_data))

#传播误差使用优化器
# 其中的参数 是学习率
#这个是梯度下降法优化器
optimizer = tf.train.GradientDescentOptimizer(0.5)

# 其中的参数 是被损失函数描述的 差距值
train = optimizer.minimize(loss)

init= tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(200):
        sess.run(train)
        if i%20==0:
            #打印 出 w与b的数值
            print(sess.run(Weights),sess.run(biases))
            #打印出方差
            print(sess.run(loss))