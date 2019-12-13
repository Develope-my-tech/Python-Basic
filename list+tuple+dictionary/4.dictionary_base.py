# 빈 딕셔너리 생성
empty_dict = {}

# 딕셔너리 예시
inform = {'이름':'박현심', '학번':'1923029'}

# dict로 변환하기
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

# 문자열로 된 리스트
lol = ['ab', 'cd', 'ef']
print(dict(lol))
## 리스트로 예시를 들어지만 튜플도 마찬가지!

# 딕셔너리의 key는 유일해야 한다.
# 같은 key를 두번 사용하는 경우, 마지막 값이 그 key의 값으로 입력된다.

# 딕셔너리 결합하기
ex = { '재석' : '유',
       '명수' : '박',
       '형돈' : '정',
       '홍철' : '노'   }
others = { 'marx': 'Groucho', 'Howard':'Moe'}
ex.update(others)
print(ex)

# 키와 del로 항목 삭제하기
del ex['marx'], ex['Howard']
print(ex)

# '재석'이라는 이름이 있는가?
# key가 있는지 확인
print('재석' in ex)

# 모든 키 얻기
print(ex.keys())

# 모든 값 얻기
print(ex.values())

# 모든 쌍의 키-값 얻기
print(ex.items())

# 모든 항목 삭제
ex.clear()