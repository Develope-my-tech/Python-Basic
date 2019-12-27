# 표준 모듈 're'
import re

# 1. match 함수 : 패턴과 텍스트가 매치하면 match 객체를 반환, 그렇지 않으면 None 반환
result = re.match('You', 'Young Frankenstein')  # 패턴 : You, 문자열 소스 : Young Frankenstein
print(result)
# 출력 : <re.Match object; span=(0, 3), match='You'>

# 다른 방법
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result)
# 출력 : <re.Match object; span=(0, 3), match='You'>


# 'Young Frankenstein' 문자열은 'You' 단어로 시작하는가? 에 대한 코드
source = 'Young Frankenstein'
m = re.match('You', source) # 소스의 시작부터 패턴(You)가 일치하는지 확인
if m:
    print(m.group())    # 출력 : You

# 2. search 함수 : 패턴이 아무데나 있어도 작동
m = re.search('Frank', source)
if m:
    print(m.group())    # 출력 : Frank

m = re.search('.*Frank', source)    # . : '한 개의 문자' & * : '앞의 문자가 여러개 올 수 있다'(0회 이상)
if m:
    print(m.group())    # 출력 : Young Frank

# 3. findall 함수 : 일치하는 모든 패턴 찾기
m = re.findall('n', source)
print(m)    # 출력 :  ['n', 'n', 'n', 'n']

m = re.findall('n.', source)
print(m)    # 출력 : ['ng', 'nk', 'ns'] --> 마지막 'n'은 뒤에 문자가 없으므로 출력 되지 않음

m = re.findall('n.?', source)
print(m)    # 출력 : ['ng', 'nk', 'ns', 'n'] --> . : '한 개의 문자' & ? : '0 또는 1회'


# 4. split 함수 : 문자열 대신 패턴으로 문자열 리스트를 생성
m = re.split('n', source)
print(m)    # 출력 : ['You', 'g Fra', 'ke', 'stei', '']

# 5. sub 함수 : 일치하는 패턴 대체하기
# 문자열 replace() 메서드와 비슷하나, 리터럴 문자열이 아닌 패턴을 사용!!!
m = re.sub('n', '?', source)
print(m)    # 출력 : You?g Fra?ke?stei?



'''
### 패턴에서의 특수 문자 ####
리터럴은 모든 비특수 문자와 일치한다.
\n을 제외한 하나의 문자 : .
0회 이상 : *
0 또는 1 : ?

* 특수 문자
\d : 숫자
\D : 비숫자
\w : 알파벳 숫자
\W : 비알파벳 숫자
\s : 공백 문자
\S : 비공백 문자
\b : 단어 경계
\B : 비단어 경계

? \b와 \B의 차이가 뭘까 ?
ex1) \bo.\b --> on, of 이런 것만 나타냄
ex2) \Bo.\B --> roses(os), raindrops(op) 가 나타남
한글과 같은 2바이트 문자는 포함하지 않기때문에 \b로 처리할 수 없다고 함 
'''

''' string 모듈은 테스트에 사용할 수 있는 문자열 상수가 미리 정의 되어 있다.'''
import string
p = string.printable
print(p[0:50])  # 출력 : 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
print(p[50:])   # 출력 : OPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c

# p에서 숫자를 찾아보자.
print(re.findall('\d', p))  # 출력 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 숫자와 문자, 언더스코어를 찾아보자! (알파벳)
print(re.findall('\w', p))
# 출력 : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
# 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
# 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']

# 공백문자는 ???
print(re.findall('\s', p))  # 출력 : [' ', '\t', '\n', '\r', '\x0b', '\x0c']

x = 'abc' + '-/*' + '\u00ea' + '\u0115' # -/*는 \w 패턴에 앍하지 않는 구두점을 예시로 넣어본 것임
print(re.findall('\w', x))
# 출력 : ['a', 'b', 'c', 'ê', 'ĕ']

'''
### 패턴 지정자 ###
( expr ) : expr
expr1 | expr2 : expr1 또는 expr2
. : \n을 제외한 모든 문자
^ : 소스 문자열의 시작
$ : 소스 문자열의 끝
prev? : 0 또는 1회의 prev
prev* : 0회 이상의 최대 prev
prev*? : 0회 이상의 최소 prev
prev+ : 1회 이상의 최대 prev
prev+? : 1회 이상의 최소 prev
prev{m} : m회의 prev
prev{m, n} : m에서 n회의 최대 prev
prev{m, n} : m에서 n회의 최소 prev
[abc] : a 또는 b 또는 c (a|b|c와 같음)
[^abc] : (a 또는 b 또는 c)가 아님
prev (?=next) : 뒤에 next가 오면 prev
prev (?!next) : 뒤에 next가 오지 않으면 prev
(?<=prev) next : 전에 prev가 오면 next
(?<!prev) next : 전에 prev가 오지 않으면 next
'''

# 패턴 지정자 예제
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

print(re.findall('wish', source))   # 출력 : ['wish', 'wish']

print(re.findall('wish|fish', source))  # 출력 : ['wish', 'wish', 'fish']

print(re.findall('^wish', source))  # 출력 : []

print(re.findall('^I wish', source))    # 출력 : ['I wish']

print(re.findall('fish$', source))  # 출력 : []

# .은 패턴 지정자 .으로 들어감
print(re.findall('fish tonight.$', source)) # 출력 : ['fish tonight.']

# .을 문자로 인식하려면 \을 사용해주어야 한다.
print(re.findall('fish tonight\.$', source))    # 출력 : ['fish tonight.']

print(re.findall('ght\W', source))  # ['ght\n', 'ght.']

print(re.findall('I (?=wish)', source)) # ['I ', 'I ']

print(re.findall('(?<=I) wish', source))  # [' wish', ' wish']

# \b(단어의 시작 부분)을 입력하기 전에 r을 입력해야 한다. (이스케이프 문자 사용 충돌을 피할 수 있다.)
print(re.findall(r'\bfish', source))

'''
match() 또는 search()를 사용할 때 모든 매칭은  m.group()과 같이 객체 m으로부터 결과를 반환한다.
패턴을 괄호로 둘러 싸는 경우, 그 괄호만의 그룹으로 저장된다.
'''

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())    # 출력 : a dish of fish
print(m.groups())   # 출력 : ('a dish', 'fish')

# (?P< name > expr) 패턴을 사용한다면 표현식(expr)이 매칭되고, 그룹 이름(name)의 매칭 내용이 저장 된다.
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())    # 출력 : a dish of fish
print(m.groups())   # 출력 : ('a dish', 'fish')
print(m.group('DISH'))  # 출력 : a dish
print(m.group('FISH'))  # 출력 : fish



