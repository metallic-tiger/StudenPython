import threading
import time

def worker(number):
    time.sleep(5-number)
    print ("worker"+str(number))
    return

def main():
    for i in range(5):
        #不知道为什么要在args参数之后加一个“,”
        '''
        创建一个线程
        target = 函数名
        args =对应函数所使用的参数
        
        其他可以使用的标签
        name=None 线程的命名
        kwargs ={}  与args类似用于参数传递
        verbose=None   日志相关 不了解
        daemon=None 是否为守护进程
        '''
        t = threading.Thread(target=worker,args=(i,))
        t.start()

if __name__=="__main__":
    main()