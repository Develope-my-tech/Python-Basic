'''
'비동기 입출력 지원 재정리' : asyncio 모듈

Redis 서버는 하나의 머신에서 실행.
클라이언트는 같은 머신에서 실행하거나 네트워크를 통해서 접근
모두 클라이언트는 TCP를 통해 서버와 통신을 하여 네트워킹한다.
하나 이상의 공급자 클라이언트는 리스트의 한쪽 끝에 메시지를 푸시한다.
하나 이상의 클라이언트 워커는 리스트를 감시하면 블로킹 팝 연산을 수행한다.
'''

import redis
conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'dessert']
for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
print('Washer is done')


