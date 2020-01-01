
'''     ### requests 라이브러리 ###      '''
import requests
url1 = 'http://quotesondesign.com/wp-json/posts'
resp = requests.get(url1)
print(resp) # <Response [404]>
print(resp.text)
# {"code":"rest_no_route","message":"No route was found matching the URL and request method","data":{"status":404}}

'''
     ### 웹 서버 ###    
초기 상태 메세지 : Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
0.0.0.0 : 모든 TCP 주소

로그라인 예시
127.0.0.1 - - [27/Jun/2015 19:46:22] "GET / HTTP/1.1" 200 -
- 127.0.0.1 : 클라이언트의 IP 주소
- 첫번째 "-" : 원격 사용자 이름
- 두번째 "-" : 로그인 사용자 이름
- [27/Jun/2015 19:46:22] : 접근한 날짜와 시간
- "GET / HTTP/1.1" : 웹 서버로 보내는 명령
    - HTTP 메서드(GET)
    - 리소스 요청(/)
    - HTTP 버전(HTTP/1.1)
- 200 : 웹 서버로부터 반환된 HTTP 상태 코드

$ python -m http.server 9999
= 기본 포트 번호는 8000이지만, 다른 포트 번호를 지정할 수 있다.


###     웹 서버 게이트웨이 인터페이스    ###
- 공용 게이트웨이 인터페이스(Common Gateway Interface, CGI)
: 클라이언트를 위해 웹 서버가 외부 프로그램을 실행하고, 그 결과를 반환하도록 설계,
클라에서 받은 입력 인자를 서버를 통해 처리하여 외부 프로그램으로 전달
프로그램은 각 클라의 접근을 위해 처음부터 다시 시작. --> 확장성이 떨어짐, 시간 오래 걸림
해결 --> 웹 서버에 인터프리터를 두는 방식으로 함

웹 서버 게이트웨이 인터페이스(Web Server Gateway Interface)
: 모든 파이썬 웹 프레이워크와 웹 서버는 WSGI를 사용한다.


###     프레임워크       ###
웹 서버는  HTTP와 WSGI의 세부사항을 처리
웹 프레임워크는 파이썬 코드를 작성하여 강력한 웹 사이트를 만들 수 있다.

- 라우트(route)
    : URL을 해석하여 해당 서버의 파일이나 파이썬 코드를 찾아준다.
- 템플릿(template)
    : 서버 사이드의 데이터를 HTML 페이지에 병합
- 인증(authentication) 및 권한(authorization)
    : 사용자 이름과 비밀번호, 퍼미션(permission)을 처리
- 세션(session)
    : 웹사이트에 방문하는 동안 사용자의 임시 데이터를 유지
'''