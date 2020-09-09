# 셋(set)은 어떤 것이 존재하는 지 여부만 판단할 때 사용
print(set('letters'))

# 리스트, 튜플을 셋으로 만드는 것은 넘어감

# 딕셔너리를 셋으로 변환하는 경우는? -> 키만 사용
print(set({'apple':'red', 'orange':'orange', 'cherry':'red'}))

# '노'씨가 있다면 이름을 출력
ex = { '재석' : '유',
       '명수' : '박',
       '형돈' : '정',
       '홍철' : '노'   }

for name, f_name in ex.items():
    if '노' in f_name:
        print(name)

# 유재석, 노홍철 찾기
ex = {
    'a class' : {'유재석', '하하', '정형돈'},
    'b class' : {'정준하', '박명수', '노홍철'},
    'c class' : {'하하', '길'},
    'd class' : {'정형돈', '박명수',}
}
for c_name, name in ex.items():
    if name & {'유재석', '노홍철'}:
        print(c_name, name)
# 출력
# a class {'정형돈', '하하', '유재석'}
# b class {'박명수', '노홍철', '정준하'}

# 박명수가 없는 class 찾기
for c_name, name in ex.items():
    if not name & {'박명수'}:
        print(c_name)

# set으로 연산하기
a = {1, 2}
b = {2, 3}
print(a&b) # a와 b의 교집합 : {2}
print(a.intersection(b)) # a와 b의 교집합 : {2}

print(a|b)
print(a.union(b)) # a와 b의 합집합 : {1,2,3}

# 첫번째 셋에는 있지만 두번째 셋에는 없는 집합
print(a-b) # {1}
print(a.difference(b)) # {1}

# exclusive : 대칭 차집합 ( 양쪽 모두에 들어있지 않은 멤버)
print(a^b) # {1, 3}
print(a.symmetric_difference(b)) # {1,3}

print(a<=b) # a는 b의 서브셋인가? False
print(a.issubset(b)) # False

ex1 = {'vodka', 'kahlua'}
ex2 = {'cream', 'kahlua', 'vodka'}
print(ex1<=ex2) # True
print(ex1<=ex1) # True