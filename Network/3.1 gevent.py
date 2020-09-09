'''
개발자는 스레드나 프로세스를 실행하여 프로그램 속도가 느린 부분을 피함.
아파치 웹 서버가 이러한 설계의 예

또 다른 대안으로 이벤트 기반(event-based) 프로그래밍
: 중앙 이벤트 루프를 실행하고 모든 작업을 조금씩 실행하면서 루프를 반복
엔진엑스 웹 서버는 이러한 설계를 따르므로, 일반적으로 아파치 웹 서버보다 빠르다.
'''

import gevent
from gevent import socket
hosts = ['www.naver.com', 'www.daum.com', 'www.google.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# gethostbyname(host) : IP 주소를 찾음

'''gevent.spawn() 
각각의 gevent.socket.gethostbyname(host)를 실행하기 위해
greenlet (그린스레드 or 마이크로 스레드)를 생성'''
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)

'''
210.89.164.90
49.51.10.192
216.58.197.196
'''

'''
greenlet과 일반적인 스레드의 차이점은 블록(block)을 하지 않는 것이다.
한 스레드에서 무슨 일이 발생하여 블록되었다면
gevent는 제어를 다른 하나의 greenlet으로 바꾼다.

gevent.joinall() 메서드는 생성된 모든 작업이 끝날 때까지 기다린다.
그리고 호스트네임에 대한 IP 주소를 한번에 얻게 된다.

gevent 버전의 socket 대신, 기억하기 쉬운 이름의 몽키-패치 함수를 쓸 수 있다.
gevent 버전의 모듈을 호출하지 않고, greenlet을 사용하기 위해 socket과 같은
표준 모듈을 수정한다.

심지어 gevent에 접근할 수 없는 코드에도 적용할 수 있다.
'''