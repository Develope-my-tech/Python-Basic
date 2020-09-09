"""
병행성 : 동시에 여러 일을 수행.

1. 성능 (performance)
- 느린 요소를 기다리지 않고, 빠른 요소를 바쁘게 유지한다.
2. 견고함 (robustness)
- 하드웨어 및 소프트웨어의 장애를 피하기 위해 작업을 복제하여,
여러가지 안정적인 방식으로 운영한다.
3. 간소화 (simplicity)
- 복잡한 작업을 좀 더 이해하기 쉽고, 해결하기 쉬운 여러 작은 작업으로 분해한다.
4. 커뮤니케이션 (communication)
- 데이터(바이트)를 보내고 싶은 곳에 원격으로 전송하고, 다시 데이터를 수신받는다.

"""

"""
* 컴퓨터가 일을 수행하면서 뭔가 기다리는 이유
- I/O 바운드 : 대부분 이 경우. 컴퓨터의 cpu는 메모리, 디스크, 네트워크보다 빠르다.
- CPU 바운드 : 과학이나 그래픽 작업과 같이 엄청난 계산이 필요할 때 발생

*** I/O 바운드 문제 - 스레드 사용 
*** CPU 바운드 문제 - 프로세스, 네트워킹, 이벤트 사용

* 병행성
- 동기 (symchronous) : 한 줄의 장례 행렬처럼 한 작업은 다른 직업을 따른다.
- 비동기 (asymchronous) : 작업들이 독립적이다.

* 큐 (queue)
: 리스트와 같다. 먼저 온 수선대로 가져간다.
FIFO ( First In First Out)
"""


'''     1. 프로세스     '''
import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()