# 아스키 코드 : 7 비트
# 26개의 대/소문자, 10개의 숫자, 공백문자, 비인쇄 제어코드(널, 백스페이스 등)

# 유니코드 : 전 세계 언어의 문자를 정의하기 위한 국제 표준 코드 (8비트) 2^8 = 256 평면
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)  # name() : 유니코드 문자를 받아 대문자 이름을 반환
    value2 = unicodedata.lookup(name) # lookup() : 대/소문자 구분하지 않는 인자를 받아 유니코드 문자 반환
    print('value=%s, name=%s, value2=%s'% (value, name, value2))

unicode_test('A') # 결과 : value=A, name=LATIN CAPITAL LETTER A, value2=A
# 유니코드 통화 문자
unicode_test('\u00a2') # 결과 : value=¢, name=CENT SIGN, value2=¢

# 유니코드 인코딩하기
import unicodedata
place = 'café'  # e의 index : 00E9
print(unicodedata.name('\u00e9'))   # 출력 : LATIN SMALL LETTER E WITH ACUTE
# 유니코드 인덱스 사이트에선 "E WITH ACUTE, LATIN SMALL LETTER" 라고 되어있는데
# 콤마 지우면서 서로 순서를 바꿔서 써줘야함!
print(unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE")) # 출력 : é

print('caf\u00e9')
print('caf\N{LATIN SMALL LETTER E WITH ACUTE}')
# 출력 : café