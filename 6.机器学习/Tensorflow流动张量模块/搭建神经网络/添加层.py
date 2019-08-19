import tensorflow as tf
import numpy as np


#
# 然后定义添加神经层的函数def add_layer(),
# 它有四个参数：
# 输入值、
# 输入的大小、
# 输出的大小
# 激励函数，我们设定默认的激励函数是None。
def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('Layer'):
        with tf.name_scope('inLine'):
    # weights为一个in_size行, out_size列的随机变量矩阵
            W = tf.Variable(tf.random_normal([in_size, out_size]), dtype=tf.float32,name='W')

    # 莫烦大佬的教程里说不推荐值为0https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/3-1-add-layer/
    #
        with tf.name_scope('B'):
            b = tf.Variable(tf.zeros([1, out_size]) + 0.1, dtype=tf.float32,name='b')
            Wx_b = tf.matmul(inputs, W) + b

        if activation_function is None:
            Out = Wx_b
        else:
            Out = activation_function(Wx_b)
        return Out


x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#可视化操作所需要的内容 用于标注数据
with tf.name_scope('Inputs'):
    xs = tf.placeholder(tf.float32, [None, 1])
    ys = tf.placeholder(tf.float32, [None, 1])

L1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
predition = add_layer(L1, 10, 1, activation_function=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition), reduction_indices=[1]),name="loss")
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1, 1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        #print('################xs : ',xs)
        if i % 50 == 0:
            # to see the step improvement
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
sess = tf.Session() # get session
# tf.train.SummaryWriter soon be deprecated, use following
writer = tf.summary.FileWriter("logs/", sess.graph)