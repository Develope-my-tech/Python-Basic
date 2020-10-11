
# Sequence  
  
## :pushpin: zip()
### zip() 함수를 이용하여 여러 시퀀스를 병렬로 순회한다.<br>
### 여러 시퀀스 중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다.<br>

- ### list(zip(list1, list2)) ⇒ "list1의 원소, list2의 원소"(튜플) 들로 이루어진 리스트 생성
- ### dict(zip(list1, list2)) ⇒ "list1의 원소 :list2의원소" 들로 이루어진 딕셔너리 생성

<br>

## :pushpin: Comprehension
### 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 compact한 방법.<br>

- ### List Comprehension 
	
	  [ 표현식 for 항목 in 순회 가능한 객체 if 조건 ]
	  
- ### Dictionary Comprehension
	
	  { 키 표현식 : 값 표현식 for 표현식 in 순회 가능한 객체 }

- ### Set Comprehension

	  { 표현식 for 표현식 in 순회가능 객체 }
	 
- ### Generator Comprehension
	- 튜플은 comprehension이 없다. ⇒ 그러나 comprehension이 실행이 되는데 이때 **generator 객체**가 반환된다.
	- **generator**는 한 번만 실행되기 때문에, 다시 순회하려면 아무것도 볼 수 없다. 한 번만 실행되어 즉석에서 그 값을 생성하고 iterator를 통해 한번에 하나씩 값을 처리한다.

<br>

# Augment

## :pushpin: None
### None은 "if 인자" or "if 인자 is None"으로도 가능하다.<br>
### 정수, 부동소수점수, 빈 문자열/리스트/튜플/딕셔너리/셋은 모두 False지만, None과 같지 않다.<br>

	if thing is None:
		print("thing is none")
	elif thing:
		print("its true")
	else:
		print("its false")

<br>

## :pushpin: Positional arguments
### 인자의 타입은 값을 순서대로 상응하는 매개변수에 복사하는 위치 인자다. <br>

	def menu(wine, entree, dessert):
		return {'wine':wine, 'entree':entree, 'dessert':dessert}

	menu('beef', 'bagel', 'bordeaux')
		
<br>

## :pushpin: Keyword arguments
### 위치 인자의 혼동을 피하기 위해 매개변수에 상응하는 이름을 인자에 짖어할 수 있다.<br>

	menu(entree='beef', dessert='bagel', wine='bordeaux')

<br>

## :pushpin: Default arguments
### 매개변수에 기본값을 지정하여 호출자가 대응하는 인자를 제공하지 않을 경우 기본값을 사용한다.

	menu(wine, entree, dessert="pudding")
	
<br>

## :pushpin: asterisk (*)
### 파이썬에는 포인터가 없다.<br>
### 애스터리스크는 매개변수에서 위치 인자 변수들을 튜플로 묶는다. <br>
### 인자 없이 호출하면 아무것도 없다.<br>

	def printargs(*args)

<br>

### keyword 인자를 모으기 위해서 두 개의 애스터리스크(**)를 사용한다.[(링크)](https://github.com/Develope-my-tech/Python-Basic/blob/master/Code%20struct/2.argument.py#12)<br>
### 위치 매개변수와 *arg, **kwarg를 같이 사용하려면 순서대로 배치해야한다. <br>

<br>

## :pushpin: Docstring
### 함수 몸체 시작 부분에 문자열을 포함시켜 함수 정의에 문서를 붙일 수있다. <br>
### docstring을 출력하려면 help() 함수를 호출한다. <br>
### 서식 없는 docstring을 보고 싶다면 내부 이름인 함수 내 변수 `__doc__`을 이용하여 출력할 수 있다.[(링크)](https://github.com/Develope-my-tech/Python-Basic/blob/master/Code%20struct/2.argument.py#18)<br>

<br>

## :pushpin:  파이썬은 '모든 것이 객체다'

	def answer():
		print(42)
	
	def run(func):
		func()
	
	def add(arg1, arg2):
		print(arg1+arg2)
	
	run(answer)				# 42
	type(run(answer))		# <class 'function'>
	
<br>

## :pushpin: 내부 함수


	def outer(a, b):
		 def inner(c, d):
			 return c+d
		 return inner(a, b)
	
	outer(4, 7)	# 11

<br>

## :pushpin: Closure
### 클로져는 다른 함수에 의해 동적으로 생성.<br>
### 바깥 함수로부터 생성된 변수값을 변경하거나 저장할 수 있다. [(링크)](https://github.com/Develope-my-tech/Python-Basic/blob/master/Code%20struct/3.closer.py)<br>

<br>

## :pushpin: Lambda
### 람다 함수는 단일문으로 표현되는 익명 함수이다.<br>
### 람다는 `많은 작은 함수를 정의하고, 이들을 호출해서 얻은 모든 결과값을 저장해야하는 경우` 유용하다.<br>
### 특히, `콜백 함수`를 정의하는 GUI에서 람다를 사용할 수 있다.<br>

<br>

## :pushpin: Generator
### 파이썬의 시퀀스를 생성하는 객체<br>
### 전체 시퀀스를 한 번에 메모리에 생성하고 정렬할 필요 없이 잠재적으로 아주 큰 시퀀스를 순회할 수 있다. <br>
### 제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환

- ### 일반 함수 : 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫번째 라인부터 수행
- ### 제너레이터 함수 : 일반 함수지만 return 문으로 값을 반환하지 않고, yield 문으로 값을 반환한다.

<br>

## :pushpin: Decorator
### 소스 코드를 수정하지 않고 사용하고 있는 함수를 수정하고 싶을 때 사용한다.<br>
### `하나의 함수를 취해서 다른 함수를 반환하는 함수`<br>
### 일반적으로 decorator는 로그를 남기거나 유저의 로그인 상태를 확인, 프로그램의 성능 테스트에서 많이 쓰인다고 한다.<br>

	def documnet_it(func):
		...

	@document_it
	def add_ints(a, b):
		return a+b

<br>

## :pushpin: Name Space
### 네임스페이스는 특정 이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계 없는 것을 말한다.<br>

- ### locals() : 로컬 네임스페이스의 내용이 담긴 딕셔너리 반환
- ### globals() : 글로벌 네임스페이스의 내용이 담긴 딕셔너리 반환

<br>

## :pushpin: Underscore
### 파이썬 내의 사용을 위해 예약되어있다.<br>
### `function.__name__`, `fuction.__doc__` 등이 있다.

<br>

## :pushpin: try & except
### 어떤 함수에서 예외가 발생하여 그곳에서 잡히지 않았다면, 호출한 함수에 일치하는 핸들러에 의해서 이 예외를 잡을 때까지 버블링(bubbling)한다.<br>

- ### 인자없는 except 문은 모든 예외 타입을 잡는다는 것이다.
- ### 두 개 이상의 예외 타입이 발생하면 별도의 예외 핸들러를 제공하는 것이 가장 좋다.
	
	  # 예외 사항에 대한 세부 정보를 얻기 위하여 변수 이름에서  예외 객체 전체를 얻을 수 있다.
	  except 예외 타입 as 이름

- ### 상황에 따라서 미리 정의 되어있는 예외 처리 외에도 특별한 상황에서 발생할 수 있는 예외 타입을 정의할 수 있다. [(링크)](https://github.com/Develope-my-tech/Python-Basic/blob/master/Code%20struct/7.%20underscore%20%26%20try_except.py)

<br>
