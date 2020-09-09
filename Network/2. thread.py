import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread {} says: {}".format(threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function {}".format(n),))
        p.start()


'''
Thread <_MainThread(MainThread, started 7480)> says: I'm the main program
Thread <Thread(Thread-1, started 10944)> says: I'm function 0
Thread <Thread(Thread-2, started 2536)> says: I'm function 1
Thread <Thread(Thread-3, started 13468)> says: I'm function 2
Thread <Thread(Thread-4, started 2336)> says: I'm function 3
'''