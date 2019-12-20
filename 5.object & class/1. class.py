## 객체 = 데이터 + 코드를 모두 포함하는 틀의 인스턴스(instance)

# 빈 클래스 생성
class person():
    pass

# someone 변수에 person 객체 할당
someone = person()

# 객체 초기화 메서드 예시
class init_ex():
    def __init__(self, name): # 객체 초기화 메서드 : 객체 생성시 초기화한다.
        self.name = name

human = init_ex('minsu')
print(human.name) # 출력 : minsu

## 기존 클래스에 필요한 기능을 추가하고 싶다면 ?? ->  '상속'을 사용하자
class Name():
    def q(self):
        print("What's your name?")

class get_name(Name): # Name 클래스(부모 클래스)를 상속 받음
    pass

ask_name = get_name()
ask_name.q() # 출력 : What's your name?

## 상속받은 부모 클래스의 메서드를 바꾸고 싶다 -> '오버라이드'
# 상속 받은 메서드들 중 쓰고 싶은 메서드 이름이 있을 경우 사용한다고 한다.

class young():
    def name(self):
        print('What\'s your name?')
    def age(self):
        print('He\'s 12')

class old(young): # young 클래스 상속
    def age(self):
        print('He\'s 53') # overriding

boy = young()
guy = old()
boy.age() # He's 12
guy.age() # He's 53
# ** __init__ 메소드를 포함한 모든 메서드를 오버라이드 할 수 있다.

## 자식 클래스에서 부모 클래스의 메서드 호출 --> 'super' 메서드
# 부모 클래스에서 메서드가 변경되면 자식 클래스도 변경된 메서드를 사용할 수 있는 이점
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name) # 부모 클래스의 __init__ 메서드 사용
        self.email = email

bob = EmailPerson('Bobo Frapples', 'bob@naver.com')
print('name : %s , email : %s' % (bob.name, bob.email))
# 출력 : name : Bobo Frapples , email : bob@naver.com

# 파이썬에선 인스턴스 메서드의 첫번째 인자로 self를 포함해야한다.
class hello():
    def say(self):
        print('hello!')

h = hello()
h.say() # h 객체를 hello 클래스의 say 메서드의 self 매개변수에 전달한다.
hello.say(h) # h.say()와 같다. (\굳이 이렇게 쓸 이유가 없을 뿐)

# 파이썬에서는 모든 속성과 메서드가 public
## 그러나 자바처럼 private 같이 쓰고 싶다면
## 1. '프로퍼티'를 이용하자 (그런데 외부인이 히든 변수 이름을 알고 있으면 접근 가능...)
class ex_class():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        return self.hidden_name
    def set_name(self, input_name):
        self.hidden_name = input_name
    name = property(get_name, set_name)

student = ex_class('hong')
print(student.name) # 출력 : hong
print(student.get_name()) # 출력 : hong
student.name = 'park'
print(student.name) # 출력 : park

## 2. '데커레이터'를 이용하자. ( 마찬가지..)
class ex_class2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property       # getter 메서드 앞에는 @property 데커레이터를 씀
    def name(self):
        return self.hidden_name
    @name.setter    # setter 메서드 앞에서는 @name.setter 데커레이터를 씀
    def name(self, input_name):
        self.hidden_name = input_name
stu = ex_class2('철수')
print(stu.name)     # 출력 : 철수
stu.name = '민수'
print(stu.name)     # 출력 : 민수

# 프로퍼티를 이용하면 데이터 수정시 클래스 정의에서 수정하면 모두 변경된다!

# 하지만 프로퍼티 데커레이션으로도 완전히 숨겨지지 않는다.
## 외부에서 볼 수 없도록 하려면 '언더스코어'를 사용하자 (Name Mangling)
class ex_class3():
    def __init__(self, input_name):
        self.__name = input_name
stu2 = ex_class3('영희')
# print(stu2.__name) # 에러 발생
print(stu2._ex_class3__name) # 이것 또한 쓸라면 쓸수는 있음
# 그러나 속성이 완벽하게 보호되지는 않지만 의도적인 접근을 막는 느낌이다.

# 메서드 타입
## 1. 인스턴스 메서드 : 첫번째 매개변수는 self로 객체를 전달
## 2. 클래스 메서드 : 첫번재 매개변수는 클래스 자신
# 클래스에 대한 어떤 변화가 모든 객체에 영향을 미친다.
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def excalim(self):  # 인스턴스 메서드
        print('hello A')
    @classmethod
    def kids(cls):      # 클래스 메서드
        print('A has', cls.count)
ex_a = A()
ex_a2 = A()
A.kids()    # 출력 :  A has 2
# 궁금해서 ex_a2.kids() 도 해봤는데 출력값이 같다.

## 객체 없이 메서드 사용하기 : '정적 메서드'
class B():
    @staticmethod
    def hello():
        print('hello!!')
B.hello() # hello!!

## 파이썬의 특수 메서드 (오버라이드 가능)
# __eq__(self, other)     '==' 사용 시 호출되는 함수
# __ne__(self, other)     '!=' 사용 시 호출되는 함수
# __lt__(self, other)     '<' 사용 시 호출되는 함수
# __gt__(self, other)     '>' 사용 시 호출되는 함수
# __le__(self, other)     '<=' 사용 시 호출되는 함수
# __ge__(self, other)     '>=' 사용 시 호출되는 함수

# __add__(self, other)     '+' 사용 시 호출되는 함수
# __sub__(self, other)     '-' 사용 시 호출되는 함수
# __mul__(self, other)     '*' 사용 시 호출되는 함수
# __floordiv__(self, other)     '//' 사용 시 호출되는 함수
# __truediv__(self, other)     '/' 사용 시 호출되는 함수
# __mod__(self, other)     '%' 사용 시 호출되는 함수
# __pow__(self, other)     '**' 사용 시 호출되는 함수

# __str__(self, other)     str(self) 사용 시 호출되는 함수
# __repr__(self, other)     repr(self) 사용 시 호출되는 함수 -- 유효 17자리
# __len__(self, other)     len(self) 사용 시 호출되는 함수 -- 문자열 길이

## 자식 클래스가 부모 클래스처럼 행동하기 'Composition(=aggregation)'
class Bill():
    def __init__(self, decription):
        self.description = decription

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('tail : %s, bill : %s' %(self.tail.length, self.bill.description))
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about() # 출력 : tail : long, bill : wide orange

# 클래스는 상속을 지원하지만 모듈은 상속을 지원하지 않는다.
# 한가지 일만 수행? --> 모듈 / 여러 함수 & 여러 변수 ?? -> 클래스

# 과한 자료구조 엔지니어링보다는 네임드 튜플이 낫다.
## 네임드 튜플이란??? : 튜플의 서브 클래스
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck) # 출력 : Duck(bill='wide orange', tail='long')
print(duck.tail,"&" , duck.bill) # 출력 : long & wide orange

# 딕셔너리도 네임드 튜플로 가능하다.
parts = {'bill' : 'wide orange', 'tail':'long' }
duck2 = Duck(**parts)
print(duck2) # 출력 : Duck(bill='wide orange', tail='long')

# 네임드 튜플은 불변하지만 필드를 바꿔서 또 다른 네임드 튜플 반환 가능하다.
duck3 = duck2._replace(tail='magnificent' ,bill='crushing')
print(duck3) # 출력 : Duck(bill='crushing', tail='magnificent')

# duck3.tail = 'None'   # 에러 발생!! 변경 안 됨