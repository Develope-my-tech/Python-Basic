'''
####       파이썬 표준 웹 라이브러리      ####

* http : 모든 클라이언트-서버 HTTP 세부사항을 관리
- client는 클라이언트 부분 관리
- server는 파이썬 웹 서버를 작성
- cookies와 cookiejar은 사이트 방문자의 데이터를 저장하는 쿠키 관리

* urllib은 http 위에서 실행된다.
- request는 클라이언트의 요청 처리
- response는 서버의 응답 처리
- parse는 URL을 분석
'''
import urllib.request as ur
url = 'http://quotesondesign.com/wp-json/posts'
# req = ur.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
conn = ur.urlopen(url) # conn --> HTTPResponse 객체
print(conn) # <http.client.HTTPResponse object at 0x000001B1F2935C48>
# 403 에러가 나기 때문에 ur.Request을 추가해줘야 한다.
# (봇이라고 판단하고 차단한다고 함)

data = conn.read()  # 웹페이지로부터 데이터를 읽어온다.
print(data)
'''b'<html>\n<head>\n<!--<?xml version="1.0" encoding="UTF-8"?><WISPAccessGatewayParam xmlns:xsi="http://www.w3.org/200
1/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.acmewisp.com/WISPAccessGatewayParam.xsd">\t<Redirect>\t\
t<AccessProcedure>1.0</AccessProcedure>\t\t<AccessLocation>QookNShow</AccessLocation>\t\t<LocationName>QookNShow</Locati
onName>\t\t<LoginURL>https://first.wifi.olleh.com/webauth/wispr/login.php?ip=61.84.23.51&mac=181deaf0bc2f</LoginURL>\t\t
<MessageType>100</MessageType>\t\t<ResponseCode>0</ResponseCode>\t</Redirect></WISPAccessGatewayParam>--> \n\t<script>\n
\t location.href = "http://first.wifi.olleh.com/webauth/redirection.php?ip=61.84.23.51&mac=181deaf0bc2f&url=http://quot
esondesign.com&ssid=KT_starbucks&ap_mac=00300d89592f&apmodel=MW-6900AP";\n\t</script>\n</head>\n</html>'''

# HTTP 상태 코드
print(conn.status)  # 200 : "성공적으로 요청 처리" 의미

'''
* HTTP의 응답코드
- 1xx(조건부 응답) : 서버 요청은 받았으나, 클라이언트에 대한 추가 정보가 필요
- 2xx(성공) : 성공적 처리, 200 이외의 모든 성공 코드는 추가사항 전달
- 3xx(리다이렉션) : 리소스가 이전되어 클라이언트에 새로운 URL을 응답
- 4xx(클라이언트 에러) : 자주 발생하는 404은 클라이언트 측에 문제가 있음을 나타냄.
- 5xx(서버 에러) : 500은 서버에러, 웹 서버와 애플리케이션 서버가 연결 되어있지 않으면 502(불량 게이트웨이)
'''

print(conn.getheader('Content-Type'))
# text/html
# HTML을 위한 MIME 타입은 text/html
''' 
cf] MIME 이란?
--> Multipurpose Internet Mail Extensions의 약자로 '파일 변환'을 의미
(이메일과 함께 동봉할 파일을 텍스트 문자로 전환해서 이메일 시스템을 통해 전달하기 위해 개발되었기 때문)
현재는 웹을 통해서 여러 형태의 파일 전달하는데 쓰이고 있음
MIME이라는 하나의 인코딩 방식 

* 예전에는 텍스트파일을 주고받는데 ASCII로 공통된 표준에 따르기만하면 문제가 없었습니다 하지만 네트워크를 통해 ASCII 파일이
아닌 바이너리 파일을 보내는 경우가 생기게 되었습니다 
이러한 바이너리파일에는 음악파일, 무비파일, 워드파일 등등의 문서를 지칭하는 것입니다.
하지만 ASCII만으로는 전송이 불가능하여 이러한 바이너리 파일들을 기존의 시스템에서 문제 없이 전달하기 위해서 
텍스트파일로 변환이 필요하게 되었습니다

* MIME으로 인코딩 한 파일은 Content-type 정보를 파일의 앞부분에 담게 되며, Content-type은 여러가지의 타입이 있습니다.
 '''

for key, value in conn.getheaders():
    print(key, value)
# 파이썬 라이브러리는 모든 HTTP 응답 헤더를 파싱하여 딕셔너리로 제공
# Data와 Server는 쉽게 알아볼 수 있지만 다른 응답 헤더들은 조금 알아보기 힘들다.
# Content-Type과 같은 많은 HTTP 표준 헤더를 알아두면 좋다.

