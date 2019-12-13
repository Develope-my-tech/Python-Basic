# list의 기본적인 개념은 pass

# list+tuple+dictionary() 함수로 빈 리스트를 할당할 수 있다.
ex_list = list()
print(ex_list)

# 요소들의 순서 상관없이 유일한 값으로만 유지될 필요가 있다면
# 리스트보다 셋(set)을 사용하는 것이 더 좋다.

# 한 문자열을 리스트로 만들기
print(list('cat'))

# 튜플을 리스트로 반환하기
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# 문자열 나누기 split() 함수
# 괄호 안의 문자를 기준으로 나눠진 요소들의 리스트
birthday = '1/6/195//2'
print(birthday.split('/'))