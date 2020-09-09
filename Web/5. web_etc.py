'''     웹 서비스와 자동화      '''

import antigravity
# 비밀리에 표준 라이브러리의 webbrowser 모듈을 호출하여
# 파이썬 찬양 링크를 브라우저에 바로 던져준다.

import  webbrowser
url = "http://www.python.org"
print(webbrowser.open(url)) # url 사이트를 불러옴
# 출력 : True

print(webbrowser.open_new(url)) # 탭을 지원한다면 새 탭으로 열기
# 출력 : True


'''
* 웹 API
: 웹 페이지 대신 Application Programming Interface(API)를 통해 테이터를 제공
- 클라이언트는 URL 요청을 서비스에 접근하여 요청에 대한 상태와 데이터가 들어 있는 응답을 받을 수 있다.
- HTML 페이지 대신 JSON과 XML 같은 포맷을 사용하여 데이터를 쉽게 소비하는 프로그램을 작성할 수 있다.

* REST(REpresentational State Transfer)
- HTTP 동사
1. HEAD : 실제 데이터가 아닌 리소스에 대한 정보를 얻어온다.
2. GET : 서버에서 리소스의 데이터를 검색
물음표(?)와 함께 인자들이 따라오는 URL이 GET 요청이다. (요청 데이터는 생성, 변경, 삭제에 사용해선 안된다.)
3. POST : 서버의 데이터를 갱신. 주로 HTML 폼과 웹 API에서 사용
4. PUT : 새로운 리소스를 생성
5. DELETE : 서버의 데이터를 삭제 

* JSON
: 웹 클라이언트와 서버 간에 데이터를 교환하는데 유용하게 쓰임.
오픈스택(OpenStack)과 같은 웹기반 API에서 인기가 높다.

* Crawling과 Scrapping
- 자동화된 웹 패처(fetcher)로 크롤러(crawler) 혹은 스파이더(spider)
- 웹 서버에서 콘텐츠를 찾은 후, 스크래퍼(scraper)에서 원하는 정보를 찾기 위해 파싱

* BeautifulSoup : HTML 스크랩
: HTML 추출에 용이
'''
