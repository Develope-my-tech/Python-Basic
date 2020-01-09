from gevent import monkey
import gevent
monkey.patch_all()
# gevent의 영향을 가능한 많이 받아 속도가 향상될 수 있도록
# 프로그램 상단에 위 코드를 추가
import socket

hosts = ['www.naver.com', 'www.daum.net', 'www.google.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)

'''
125.209.222.142
211.231.99.17
216.58.197.196
'''