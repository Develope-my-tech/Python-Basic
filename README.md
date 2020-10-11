# 처음으로 시작하는 파이썬(파이썬 3 기준)  
### Concepts and Practice

<br>

## :heavy_check_mark: Contents

- ### [*Code struct*](https://github.com/bosl95/python_basic/tree/master/Code%20struct)
- ### [*Data*](https://github.com/bosl95/python_basic/tree/master/Data)
- ### [*List&Tuple&Dictionary*](https://github.com/bosl95/python_basic/tree/master/List%20%26%20Tuple%20%26%20dictionary)
- ### [*Network*](https://github.com/bosl95/python_basic/tree/master/Network)
- ### [*Class*](https://github.com/bosl95/python_basic/tree/master/Object%20%26%20class)
- ### [*Pyart*](https://github.com/bosl95/python_basic/tree/master/Pyart)
- ### [Pyscience*](https://github.com/bosl95/python_basic/tree/master/Pyscience)
- ### [*String*](https://github.com/bosl95/python_basic/tree/master/String)
- ### [*System*](https://github.com/bosl95/python_basic/tree/master/System)
- ### [*Tool*](https://github.com/bosl95/python_basic/tree/master/Tool)
- ### [*Web*](https://github.com/bosl95/python_basic/tree/master/Web)


# :dart: What is Python?

- ### C/C++
	-  프로그램의 속도를 가장 우선시 할 때 사용되는 저수준의 언어
	- 다른 언어보다 학습하기 어렵다.
	- 충돌 및 문제가 일어날 수 있는 상황을 고려하며 코딩해야한다.

- ### JAVA
	- C/C++의 몇가지 문제를 피하기 위해 만들어진 후발 주자

<br>

### ⇒ 저수준의 세부사항을 몇가지 정해야하기 때문에 이들을 정적 언어(*Static Language*)라고 부른다.<br>

### :pushpin: 정적언어 vs 동적 언어
#### 1. 정적 언어 
- 각 변수의 타입을 선언
- 변수 타입 : 메모리에서 사용할 공간과 용도를 컴퓨터에게 알려준다.
- 컴퓨터는 이 정보를 이용해 저수준의 **기계언어**로 컴파일한다.
- **왜 정적 언어라고 부를까?  :point_right: 변수는 자신의 타입을 변경할 수 없기 때문에 정적이다.**

<br>

#### 2. 동적 언어
- 스크립트 언어라고도 함.
- **인터프리터**라는 프로그램을 해석
- 보통 동적언어는 정적언어보다 속도가 느리지만, 인터프리터가 최적화 되면서 동적 언어의 속도가 향상되고 있다.
- 변수의 타입을 선언하도록 강요하지 않는다.
		
	  x = 5			# example
- 몇년간 다용도의 동적언어로 ``Perl``을 사용했으나 python과 Ruby에 비해 인기를 잃었다.
- ``Ruby``는 Perl의 특징을 빌린 최신 언어 Ruby on Rails라는 웹 프레임워크 때문에 큰 인기를 얻었다.  또한 파이썬과 같은 분야에 많이 사용되고 있다.
- ``PHP`` 는 HTML과 쉽게 결합할 수 있어 웹 개발에 인기가 많다. 

<br>

### :pushpin: 왜 파이썬일까?
- 범용의 고수준 언어
- **코드를 읽고 작성하는 것이 쉽다**
- 정적 언어에 비해 훨씬 간결하다
- 코드를 적게 작성하기 때문에 생산성이 높다.

<br>

### :pushpin: 그렇다면 파이썬을 사용하면 안되는 경우는?
- 프로그램이 계산 작업을 많이 하는 경우 (CPU 바운드라고 하며, 수행하는 계산 작업은 CPU 속도에 의해 결정)
- C/C++ 또는 JAVA로 작성한 프로그램은 파이썬으-로 작성한 프로그래보다 빠르다. (항상 그런 것은 아니다.)
<br>
- 그러나 파이썬은 생산성이 뛰어나므로 C의 비효율적인 알고리즘을 사용하는 것보다는 파이썬의 알고리즘을 개선해나가는 것이 나을수도 있다.
- 파이썬의 표준 인터프리터는 C로 작성되었고, C 코드를 확장할 수 있다.
- 파이썬의 인터프리터는 점점 빨라지고 있다. (개선 가능성)

<br>

### :pushpin: Python2와 Python3
#### 우선 두 버전은 서로 호환되지 않는다.<br>
#### 두 버전의 가장 큰 차이는 [print 문의 호출 방법]() 과 :fire:[유니코드 문자 처리]():fire:이다.

