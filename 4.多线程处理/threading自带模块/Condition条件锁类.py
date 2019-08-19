import threading
import time

#锁
ElemLock=threading.Lock()
#条件锁
com=threading.Condition(ElemLock)

def Con():
    while True:
        print('上锁')
        ElemLock.acquire()
        time.sleep(5)
