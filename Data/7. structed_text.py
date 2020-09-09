'''  구조화된 텍스트 파일 형식
- CSV : 탭('\t'), 콤마(','), 수직바('|')와 같은 문자를 구분자(분리자)로 사용
- XML & HTML : 태그('<', '>')
- JSON : 구두점
- YAML : 들여쓰기
'''

'''     1. CSV      '''
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]

# 파일 쓰기(csv 형식)
with open('villains', 'wt')  as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# 파일 읽기(csv)
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)

# csv파일 --> 딕셔너리로 읽기
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)
'''
[OrderedDict([('first', 'Doctor'), ('last', 'No')]), OrderedDict([('first', 'Rosa'), ('last', 'Klebb')]), 
OrderedDict([('first', 'Mister'), ('last', 'Big')]), OrderedDict([('first', 'Auric'), ('last', 'Goldfinger')]), 
OrderedDict([('first', 'Ernst'), ('last', 'Blofeld')])]
'''

villains = [
    {'first':'Doctor', 'last': 'No'},
    {'first':'Rosa', 'last': 'Klebb'},
    {'first':'Mister', 'last': 'Big'},
    {'first':'Auric', 'last': 'Goldfinger'},
    {'first':'Ernst', 'last': 'Blofeld'},
]

# DictWriter() 함수를 이용하여 CSV 파일을 다시 써보자
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)  # 헤더 라인과 함께 villains 파일 생성

print(villains)
# first,last
# Doctor,No
# Rosa,Klebb
# Mister,Big
# Auric,Goldfinger
# Ernst,Blofeld

# 읽어보자
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)
# [OrderedDict([('first', 'Doctor'), ('last', 'No')]), OrderedDict([('first', 'Rosa'), ('last', 'Klebb')]),
#  OrderedDict([('first', 'Mister'), ('last', 'Big')]), OrderedDict([('first', 'Auric'), ('last', 'Goldfinger')]),
#  OrderedDict([('first', 'Ernst'), ('last', 'Blofeld')])]

print('\n---------------')

'''     2. XML      '''
# 행과 열의 2차원 구조로 구성
import xml.etree.ElementTree as et

# XML을 파싱(해석)의 간단한 방법 = Element Tree
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag) # menu
for child in root:
    print('tage', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
       # tag: 태그 문자열, attrib : 속성의 딕셔너리
''' 출력
tage breakfast attributes: {'hours': '7-11'}
	tag: item attributes: {'price': '$6.00'}
	tag: item attributes: {'price': '$4.00'}
tage lunch attributes: {'hours': '11-3'}
	tag: item attributes: {'price': '$5.00'}
tage dinner attributes: {'hours': '3-10'}
	tag: item attributes: {'price': '$8.00'}'''

print(len(root))    # 3
print(len(root[0])) # 2

''' 
기타 표준 파이썬 XML 라이브러리
- xml.dom : 전체 XML 파일을 메모리에 로딩하여 XML의 모든 항목에 접근
- xml.sax : 한번에 전체 XML 파일을 메모리에 로딩하지 않고 즉석에서 파싱
    큰 XML 스트림을 처리해야 한다면 이 모듈을 사용
'''



'''     3. JSON     '''
''' 데이터를 교환하는데 자주 쓰이는 형식
다수의 XML 모듈과 달리, JSON에 하나의 메인 모듈이 있다.
데이터를 JSON 문자열로 인코딩(dumps),
JSON 문자열을 다시 데이터로 디코딩(loads)
'''

menu = {
"breakfast": {
        "hours":"7-11",
        "items": {
              "breakfast burritos": "$6.00",
              "pancakes": "$4.00"
        }
    },
"lunch": {
        "hours":"11-3",
        "items": {
              "hamburger": "$5.00"
        }
    },
"dinner": {
        "hours":"3-10",
        "items": {
              "hamburger": "$5.00"
        }
    },
"dinner": {
        "hours": "3-10",
        "items": {
              "spaghetti": "$8.00"
        }
    }
}
import json
menu_json = json.dumps(menu)    # JSON 문자열로 인코딩하기
print(menu_json)
# {"breakfast": {"hours": "7-11", "items": {"breakfast burritos": "$6.00", "pancakes": "$4.00"}},
# "lunch": {"hours": "11-3", "items": {"hamburger": "$5.00"}}, "dinner": {"hours": "3-10", "items": {"spaghetti": "$8.00"}}

menu2 = json.loads(menu_json)    # JSON 문자열을 자료구조로 디코딩
print(menu2)
# {'breakfast': {'hours': '7-11', 'items': {'breakfast burritos': '$6.00', 'pancakes': '$4.00'}},
# 'lunch': {'hours': '11-3', 'items': {'hamburger': '$5.00'}}, 'dinner': {'hours': '3-10', 'items': {'spaghetti': '$8.00'}}}


# 객체를 인코딩 혹은 디코딩하는 도중에 예외 발생하는 경우
import datetime
now = datetime.datetime.utcnow()
print(now)  # 2019-12-30 08:41:17.496146
# json.dumps(now)
# !!! 표준 JSON 모듈에서 날짜 또는 시간 타입을 정의하지 않아 ERROR 발생 !!!!

now_str = str(now)
print(json.dumps(now_str))  # "2019-12-30 08:45:56.287254"
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))    # 1577663134


# JSON 문서에서 예외가 발생할 수 있는 복잡한 허수 인코딩 예제
''' DTEncoder 클래스는 JSONEncoder의 서브 클래스
default() 메서드만 오버라이드하면 됨. 
'''
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):     # isinstance()는 obj의 타입을 확인
            return int(mktime(obj.timetuple()))
        # obj가 datetime 타입이 아니라면 기본 JSON 문자열로 인코딩
        return json.JSONEncoder.default(self, obj)
print(json.dumps(now, cls=DTEncoder))   # 1577663461

print(type(now))    # <class 'datetime.datetime'>
print(isinstance(now, datetime.datetime)) # True
print(isinstance(234, int)) # True
print(isinstance('hey', str)) # True
# JSON과 다른 구조화된 텍스트 형식의 파일을 자료구조로 불러올 수 있다.


'''     4. YAML        '''
'''
JSON과 유사하게 키와 값을 가지고 있지만,
날짜와 시간 같은 데이터 타입을 더 많이 처리
'''
import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text, Loader=yaml.BaseLoader)
print(data['details'])  # {'bearded': 'true', 'themes': ['cheese', 'Canada']}
print(data['poems'][1]['title'])    # Canadian Charms

# PyYAML은 문자열에서 파이썬 객체를 불러올 수 있다고 함.
# 신뢰할 수 없는 YAML을 불러오는 것은 위험하기때문에 load() 대신 항상 safe_load() 사용하는 것이 좋다.



'''
라이브러리에 대한 보안으로 defusedxml 라이브러리를 사용할 수 있다.
- 보안되지 않은 parse
from xml.etree.ElementTree import parse
et = parse(xmlfile)

- 보안된 parse
from defusedxml.ElementTree import parse
et = parse(xmlfile)
'''


'''
자료구조(객체)를 파일로 저장하는 것 : 직렬화
바이너리 형식으로 된 객체를 저장, 복원할 수 있는 pickle 모듈 제공
'''
import pickle, datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)    #
now2 = pickle.loads(pickled)
print(now1, now2, sep="\n")
# 2019-12-30 09:17:46.093361
# 2019-12-30 09:17:46.093361

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1) # tiny

pickled = pickle.dumps(obj1)    # 직렬화
print(pickled)  # b'\x80\x03c__main__\nTiny\nq\x00)\x81q\x01" 바이너리당
obj2 = pickle.loads(pickled)    # 역직렬화
print(obj2) # tiny


'''     구조화되 이진 파일      '''
'''
1. 스프레드시트 : 광범위한 이진 데이터 형식
CSV 파일로 저장하면 표준 csv 모듈을 사용하여 읽을 수 있다.

2. HDF5 : 다차원 혹은 계층적 수치 데이터를 위한 이진 데이터 형식
큰 데이터 집합에 대한 임의적인 접근이 필요한 과학 분야에 주로 사용
디비 보호가 필요하지 않은 웜 애플리케이션에 적합
'''