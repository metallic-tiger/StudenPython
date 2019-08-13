# -*- coding: UTF-8 -*-


import threading
#引入threading模块
from time import ctime, sleep
#引入时间模块

#自定义 线程 类
#父类为 threading.Thread
class Mythread(threading.Thread):
    #构造函数/初始化函数
    '''
    包含以下属性
    self 对象本身
    func 函数名--该进程所执行的参数内容
    args 参数表 一般以元组来表示
    name 线程名 默认为 ""
    '''
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    ''' rewrite run() '''

    #重载 run()方法
    def run(self):
        #调用func
        print("run "+self.name+"\n")
        self.func(self.args)



''' thread handle func --- for range 5 '''


def loop(nloop):
    # 运行 5 次之后停止
    for i in range(5):
        print('start loop ' + str(nloop), 'at: ' + str(ctime()))
        sleep(1)


def main():
    threads = []
    nloops = range(2)

    for i in nloops:
        t = Mythread(loop, (i + 1), str(i)+" thread")
        threads.append(t)

    for i in nloops:
        threads[i].start()

if __name__ == '__main__':
    main()