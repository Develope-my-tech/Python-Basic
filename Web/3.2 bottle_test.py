# url에 http://localhost:9999/echo/Mothra 입력시,
# 출력 : Say hello to my little friend: Mothra!

import requests

resp = requests.get('http://localhost:9999/echo/Mothra')

if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Mothra!':
    print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)

'''
서버가 켜진 상태에서 Mothra로 사이트에 들어가면
출력 : It worked! That almost never happens!
'''