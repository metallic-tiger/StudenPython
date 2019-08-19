import tensorflow as tf
import numpy as np

# 常量的设置
x = tf.constant([[1.0, 2.0]])
# 建造变量
matone = tf.Variable(tf.ones(shape=[2, 3], dtype=tf.float32))
mattwo = tf.Variable(tf.ones(shape=[3, 1], dtype=tf.float32))

#制造待引入的量
plead = tf.placeholder(tf.float32)

#使用矩阵运算变量测试
matone=plead*matone
oneNet = tf.matmul(x, matone)
out = tf.matmul(oneNet, mattwo)

# 使用with方法
with tf.Session() as sess:

    ############
    #总是忘了的部分
    # 返回操作的结果
    init = tf.global_variables_initializer()
    #进行初始化操作
    sess.run(init)

    ############

    #进行一次 运行至out的操作 得到out的输出值
    print(sess.run(out,feed_dict={plead:[int(input('Var 1的值'))],}))