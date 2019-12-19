# * setdefault : 딕셔너리의 키가 누락된 경우 항목을 할당 가능
periodic_table = {'Hydrogen':1, 'Helium':2 }
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12) # 새 key 값 할당

print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}

# 존재하는 키에 다른 기본값을 할당하면 원래 값만 반환되고 변화 X
helium = periodic_table.setdefault('Helium', 947)
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}

# * defaultdict : 딕셔너리를 생성할 때 모든 새 key에 대한 기본값을 먼저 지정
from collections import defaultdict
periodic_table = defaultdict(int) # 모든 누락 기본 값은 0
# int() 함수 = 정수 0, list() 함수 = 빈 리스트([]), dict()함수 = 빈 딕셔너리({})
# 인자 입력이 없을 경우 : None

periodic_table['Hydrogen'] = 1
print(periodic_table['Lead']) # 출력 : 0
print(periodic_table) # defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})

# lambda 함수 이용하기

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['A']) # 출력 : Huh?

# 카운터 만들기
food_counter = defaultdict(int) # 기본값 0
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

print(food_counter) # defaultdict(<class 'int'>, {'spam': 3, 'eggs': 1})
# food_counter가 일반 딕셔너리인 경우 예외가 발생됨

# * Counter() : 항목세기
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)    # Counter({'spam': 3, 'eggs': 1})

print(breakfast_counter.most_common()) # 모든 요소를 내림차순으로 반환
# [('spam', 3), ('eggs', 1)]
print(breakfast_counter.most_common(1)) # [('spam', 3)]

# 카운트 결합하기
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(breakfast_counter + lunch_counter) # Counter({'spam': 3, 'eggs': 3, 'bacon': 1})
print(breakfast_counter - lunch_counter) # Counter({'spam': 3})
print(lunch_counter - breakfast_counter) # Counter({'eggs': 1, 'bacon': 1})
print(lunch_counter & breakfast_counter) # Counter({'eggs': 1}) :: 공통항목은 egg 1개
print(lunch_counter | breakfast_counter) # Counter({'spam': 3, 'eggs': 2, 'bacon': 1})

# * OrderedDict() : 키 정렬하기
# 딕셔너리의 키 순서는 예측이 어렵다.
# OrderedDict() 함수는 키의 추가 순서를 기억하고 순서대로 키 값을 반환
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

print(*quotes) # Moe Larry Curly

# * deque : 스택 + 큐
# 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop(): # 중간 지점에 도달하지 않았을 때
            return False
    return True

print(palindrome('racecar')) # True
print(palindrome('halibut')) # False

# * itertools : 이터레이터 함수를 호출 시 한번에 항목을 반환하고 호출상태를 기억
import itertools
for item in itertools.chain([1, 2], ['a', 'b']): # chain : 순회 가능한 인자들을 하나씩 반환
    print(item)
# 출력
# 1
# 2
# a
# b

# for item in itertools.cycle([1, 2]): # 인자를 순환하는 무한 이터레이터
#     print(item)
# 출력
# 1
# 2
# 1
# 2

for item in itertools.accumulate([1, 2, 3, 4]): # 축적된 값 계산
    print(item)
# 1
# 3
# 6
# 10

# 함수를 사용할 수도 있음
def multiply(a, b):
    return a*b
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
# 1
# 2
# 6
# 24

# * pprint() : 깔끔하게 출력
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

print(quotes)
# OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!')])
pprint(quotes)
# OrderedDict([('Moe', 'A wise guy, huh?'),
#              ('Larry', 'Ow!'),
#              ('Curly', 'Nyuk nyuk!')])