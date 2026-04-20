import threading
import time

def threading_job():
    print('T1 start \n')
    for i in range(3):
        time.sleep(1)
    print("T1 finish\n")

    print("A new Threading: %s\n" % threading.current_thread())

def T2():
    time.sleep(2.5)
    print("T2 start\n")
    time.sleep(4)
    print("T2 finish\n")

def main():
    added_thread=threading.Thread(target=threading_job,name='T1')
    thread2=threading.Thread(target=T2,name="T2")
    threading.active_count()
    added_thread.start()
    thread2.start()
    added_thread.join()
    thread2.join()
    print('all done\n')

if __name__=='__main__':
    main()