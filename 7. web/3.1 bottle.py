# '''     1. Bottle       '''
# # 테스트 웹 서버를 실행하는 코드
# from bottle import route, run
# import socket
#
# @route('/')
# def home():
#     return  "It isn't fancy, but it's my home page"
#
# run(host='locahost', port=80)
#
# # socket.gaierror: [Errno 11001] getaddrinfo failed



# from bottle import route, run, static_file
#
# @route('/')
# def main():
#     return static_file('index.html', root='.')
#
# run(host='localhost', port=9999)

# 출력 : My new and improved home page!!!

''' 라우트의 <thing>은 /echo/ 다음에 오는 URL의 문자열을 문자열 인자 thing에 할당
echo 함수에 전달'''

from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing

run(host='localhost', port=9999)

'''
run() 함수를 호출할 때 아래 인자를 추가하여 실행 가능하다.
- debug=True : HTTP 에러가 발생한다면 디버깅 페이지를 생성
- reloader=True : 파이썬 코드가 변경되면 변경된 코드를 다시 불러온다.
'''