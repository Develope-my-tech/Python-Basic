'''     프로세스 죽이기 : terminate()    '''
import multiprocessing
import time
import os

def whoami(name):
    print("I'm {0}, in process {1}".format(name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print('\tNumber {0} of {1}. Honk!'.format(num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()

# I'm main, in process 11904
# I'm loopy, in process 11292
# 	Number 1 of 1000000. Honk!
# 	Number 2 of 1000000. Honk!
# 	Number 3 of 1000000. Honk!
# 	Number 4 of 1000000. Honk!
# 	Number 5 of 1000000. Honk!