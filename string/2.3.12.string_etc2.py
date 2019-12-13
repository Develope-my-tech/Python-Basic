setup = 'a duck goes into a bar...'

#양쪽에 . 시퀀스를 삭제한다.
print(setup.strip('.'))

# 첫번째 단어를 대문자로
print(setup.capitalize())

# 모든 단어의 첫째 문자를 대문자로
print(setup.title())

# 글자를 모두 대문자 upper 함수
# 글자를 모두 소문자 lower 함수

# 대문자 -> 소문자로, 소문자 -> 대문자로
print(setup.swapcase())

# 문자를 지정한 공간에서 중앙에 배치
print(setup.center(30))

# 왼쪽 : ljust 함수 / 오른쪽 : rjust 함수

# a 를 a famous 로 100회 바꾼다.
print(setup.replace('a', 'a famous', 100))