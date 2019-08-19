import threading
import time

#公用的变量
def EhcoTime():
    cont=0
    while True:
        print('time is : ',cont, " s")
        cont+=1
        time.sleep(0.99)

#带锁的函数
def printN1(s,Lock):
    #给Lock上锁
    Lock.acquire()
    time.sleep(1)
    #给Lock解锁
    Lock.release()
    print(s)

#带可跳过锁的函数
def printN2(s,Lock):

    if Lock.acquire(False):
        time.sleep(1)
        print(s)
    else :
        print('锁定中')

#带等待锁的函数
def printN3(s,Lock):
    if Lock.acquire(timeout=0.2):
        time.sleep(1)
        Lock.release()
        print(s)
    else:
        print('超时')

def main():
    threads=[]
    ComLock=threading.Lock()

    Time=threading.Thread(target=EhcoTime,daemon=True)
    Time.start()
    #共用锁的进程
    print('实验1 使用同一个锁 锁定不同的子线程使其的 打印操作不会互相影响')
    for i in range(5):
        threads.append(threading.Thread(target = printN1,args =(str(i),ComLock),name=str(i)))
    for i in threads:
        i.start()

    #等待上一次实验的完成
    threads[4].join()
    time.sleep(2)
    print('实验结束')
    threads.clear()

    #用各自锁的进程
    print('实验2 使用不同锁 锁定不同的子线程使其的 打印操作可能会影响')
    for i in range(5):
        threads.append(threading.Thread(target = printN1,args =(str(i+5),threading.Lock()),name=str(i)))
    for i in threads:
        i.start()

    threads[4].join()
    time.sleep(2)
    print('实验结束')
    threads.clear()

    #
    print('实验3 使用不相同的锁 用不同方式锁定不同的子线程')

    threads.append(threading.Thread(target=printN1, args=(str(1), ComLock)))
    threads.append(threading.Thread(target=printN2, args=(str(2), ComLock)))
    threads.append(threading.Thread(target=printN2, args=(str(2), threading.Lock())))
    threads.append(threading.Thread(target=printN3, args=(str(3), ComLock)))
    threads.append(threading.Thread(target=printN3, args=(str(3), threading.Lock())))
    for i in threads:
        i.start()

    #查询是否被锁定
    print(threading.Lock().locked())

if __name__ =='__main__':
    main()