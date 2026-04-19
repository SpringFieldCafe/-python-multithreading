import threading
import time

def thread_job():
    print("this is an added thrad,number:%s" % threading.current_thread())
    for i in range(3):
        time.sleep(1)
    print("end %s" % threading.current_thread())

def main():
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())


main()


