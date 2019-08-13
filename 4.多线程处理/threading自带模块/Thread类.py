import threading
import time

def TestFunction(n):
    '''if n<3:
        time.sleep(5-n)
    else:
        time.sleep(n)'''
    time.sleep(2)
    print("Test~ I is "+str(n))

def main():
    #普通的线程
    threads=[]
    for i in range(5):
        ##
        #init 创建新线程
        '''
        创建一个线程
        target = 函数名
        args =对应函数所使用的参数
        不知道为什么要在args参数之后加一个“,”
        
        其他可以使用的标签
        name=None 线程的命名
        kwargs ={}  与args类似用于参数传递
        verbose=None   日志相关 不了解
        daemon=None 是否为守护进程 bool
        '''
        threads.append(threading.Thread(target = TestFunction,args =(i,),name=str(i)))

    #获取线程信息
    '''
    isDaemon()
    是否是守护进程
    
    getName()
    获取线程名称
    
    threads[0].ident
    获取标识符//似乎没有用
    
    threads[0].isAlive()
    判断线程是否还在执行
    '''
    print('第一个线程是否为守护线程 ： ',threads[0].isDaemon())
    print('第一个线程的名字 ： ',threads[0].getName())
    print('第一个线程的线程标识符是 ： ',threads[0].ident)
    print('第一个线程是否为启动 ： ',threads[0].isAlive())

    #test 样例



    #线程的使用
    '''
    启动线程
    start()
    run() run方法一般要在自定义的类中重写才能进行使用
    
    
    '''
    threads[4].daemon=True
    for i in threads:
        #启动线程
        i.start()

    '''
    如果使用join()方法  可以设置时间
    当没有设置时间时：
    
    对于非守护进程
    那么函数就会等待所有的此join线程结束之后才继续进行
    对于守护进程
    如果运行到 join的位置仍然没有结束 那么就直接杀死 该进程
    
    如果设置时间
    对于非守护进程
    那么函数就会等待一段时间，如果没有完成那么函数继续运行直到结束，子进程单独运行直到子进程结束
    对于守护进程
    如果运行到 join的位置且又过了 规定的时间 仍然没有结束 那么就杀死该进程
    '''

    for i in threads:
        i.join()
        print('A')


    for i in threads:
        print(i.getName(), ' 线程是否存活 ： ', i.isAlive())
        time.sleep(1)
    '''
    同一个线程不能被多次启动
    否则会报错
    
    threads[0].start()
    threads[0].run()
    '''


if __name__ =='__main__':
    main()
