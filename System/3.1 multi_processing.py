# 2. multiprocessing
import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print('Process %s says: %s'% (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n, ))
        p.start()

# Process 11960 says: I'm the main program
#  --------------- 멀티 프로세싱
# Process 6460 says: I'm function 0
# Process 1812 says: I'm function 1
# Process 14868 says: I'm function 2
# Process 14816 says: I'm function 3
