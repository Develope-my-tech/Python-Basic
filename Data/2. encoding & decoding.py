# encoding : 문자열  --> 바이트
# decoding : 바이트 --> 문자열

# 인코딩

snowman = '\u2603'
ds = snowman.encode('utf-8')    # 유니코드 문자를 바이트 시퀀스로 인코딩
print(ds) # 출력 :  b'\xe2\x98\x83'

ascii_snoman = snowman.encode('ascii', 'ignore')
# ignore로 알 수 없는 문자는 인코딩을 하지 않음
print(ascii_snoman) # 출력 : b''

ascii_snoman = snowman.encode('ascii', 'replace')
# replace는 알 수 없는 문자를 ?로 대체
print(ascii_snoman) # 출력 : b'?'

ascii_snoman = snowman.encode('ascii', 'backslashreplace')
# 유니코드 이스케이프처럼 파이썬 유니코드 문자의 문자열을 만듬
print(ascii_snoman) # 출력 : b'\\u2603'

ascii_snoman = snowman.encode('ascii', 'xmlcharrefreplace')
# 유니코드 이스케이프 시퀀스를 출력할 수 있는 문자열
print(ascii_snoman) # 출력 : b'&#9731;'

# 디코딩

place = 'caf\u00e9' # café 유니코드 문자열 생성
print(place) # 출력 : café

place_bytes = place.encode('utf-8') # 바이트 변수로 인코딩
place2 = place_bytes.decode('utf-8') # 바이트 문자열 --> 유니코드 문자열 디코딩
print(place2) # 출력 : café

# place2 = place_bytes.decode('ascii') # utf-8을 다른 인코딩 방식으로 사용한다면 어떻게 될까?
# print(place2)   # 에러
# * 아스키 코드는 128(16진수 80)에서 255(16진수 FF) 사이에 있는 일부 8비트 문자 셋의 인코딩이 유효하나,
# * UTF-8과는 다르다.

place3 = place_bytes.decode('latin-1')
print(place3)   # 출력 : cafÃ©
place4 = place_bytes.decode('windows-1252')
print(place4)   # 출력 : cafÃ©

# UTF-8은 모든 유니코드 문자를 표현할 수 있고 어디에서나 지원한다.
# 그리고 빠르게 인, 디코딩을 수행한다.
# 가능하면 UTF-8을 사용하자.