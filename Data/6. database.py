'''
    *** 관계형 데이터베이스 ***
- 다수의 동시 사용자가 데이터에 접근
- 사용자에 의한 데이터 손상 보호
- 데이터를 저장, 검색하는 효율적인 방법
- 스키마에 의해 정의된 데이터와 제약조건에 한정되는 데이터
- 다양한 데이터 타입과 관계를 계산하는 조이
- 서술적인 질의 언어 : SQL
'''



'''
### SQL ###
: API나 프로토콜이 아님. 
원하는 결과를 질의하는 서술형 언어
질의는 클라이언트에서 디비 서버로 전송하는 텍스트 문자열

- DDL(데이터 정의어)
테이블, 데이터베이스, 사용자에 대한 생성, 삭제, 제약조건, 권한을 다룬다.

db 생성 : CREATE DATABASE dbname
db 선택 : USE dbname
db & table 삭제 : DROP DATABASE dbname
table 생성 : CREATE TABLE tbname
table 삭제 : DROP TABLE tbname
table 모든 행 삭제 : TRUNCATE TABLE tbname

- DML(데이터 조작어)
데이터의 조회, 삽입, 갱신, 삭제를 다룬다.

생성 : INSERT
조회 : SELECT
갱신 : UPDATE
삭제 : DELETE

###     DB-API      ###
: 서비스에 대한 접근을 얻기 위해 호출하는 함수들

- connect() : DB의 연결을 만듬. 사용자의 이름, 비번, 서버 주소 등의 인자 포함
- cursor() : 질의를 관리하기 위한 커서 객체
- excute().executemany() : DB에 하나 이상의 SQL 명령을 실행
- fetchone().fetchmany().fetchall() : 실행 결과를 얻는다.

###     SQLite      ###
: 가볍고 좋은 오픈소스의 관계형 데이터베이스.
표준 파이썬 라이브러리로 구현, 일반 파일처럼 디비 저장.

예제는 DB파일이 필요하므로 뒤에서 다시 다루어보자.

###     MySQL       ###
: SQLite와 달리 MySQL은 실제 서버로 사용한다.
클라이언트는 네트워크를 통해 MySQL 서버에 접근할 수 있다.

###     PostgreSQL      ###
: 완전한 기능을 갖춘 오픈소스 관계형 데이터베이스

###     SQLAlchemy      ###
: 크로스 데이터베이스의 파이썬 라이브러리

###      NoSQL        ###
- dbm 형식
키-값 저장 형식

- Memcached
인메모리 키-값의 캐시 서버 ( 캐시 서버라 데이터가 오래 지속되지 않음)
디비 앞단에 놓이거나 웹 서뱌의 세션 데이터 저장에 사용

- Redis 
자료구조 서버
memcached 처럼 메모리에 맞아야함(디스크에 데이터를 저장할 수 있는 옵션이 있다.)
Memcached와 달리,
1. 서버의 재시작과 신뢰성을 위해 데이터를 디스크에 저장한다.
2. 기존 데이터를 유지
3. 간단한 문자열 이상의 자료구조 제공

- 기타 NoSQL
* Cassandra
* CouchDB
* HBase
* MongoDB
* Kyoto Cabinet
* Riak

+) 풀텍스트 데이터베이스
'''