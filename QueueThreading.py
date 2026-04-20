import threading
import time
import numpy as np
from queue import Queue

def job(l,q):
    for i in range(len(list(l))):
        l[i]=l[i]**2
    q.put(l)

def multithreading():
    q=Queue()
    threads=[]
    for i in range(4):
        t=threading.Thread(target=job,args=(np.arange(1+i,10+i,10),q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    results=[]
    for _ in range(4):
        results.append(q.get())

    print("res:",results)


if __name__=='__main__':
    multithreading()