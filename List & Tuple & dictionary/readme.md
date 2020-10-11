# List  
 
## :pushpin: Base
- ### list() : 빈 리스트 할당
- ### list(문자열) : 문자열을 리스트 형태로 변환
- ### list(튜플) : 튜플을 리스트 형태로 변환
- ### split() : split()을 통해 리스트 형태로 변환

<br>

## :pushpin: List Function
- ### list1 += list2 : list1에 list2를 추가
- ### list1.extends(list2) : 위와 동일하다.
- ### list1.insert(idx, value) : list[idx]에 삽입
- ### del list1[-1] : 맨 마지막 원소를 삭제.
	- del은 리스트 함수가 아니라 **파이썬 구문**이다.
	- 따라서 list1[-1].del()을 수행할 수 없다.
	
<br>

# Tuple

## :pushpin: base
### 튜플은 리스트와 달리 ``불변``한다.<br>
### 튜플은 뒤에 콤마를 붙인다. 두 개 이상인 경우엔 붙이지 않는다.<br>

- ### Tuple Unpacking : 한번에 여러 변수를 할당

      a, b, c = ex_tuple

### tuple() 함수를 통해 다른 객체를 튜플로 만들어 줄 수도 있다.<br>

<br>

## :pushpin: Tuple vs List
- ### 튜플은 더 적은 공간을 사용한다.
- ### 튜플의 항목이 손상될 염려가 없다.
- ### 튜플을 딕셔너리 키로 사용할 수 있다.
- ### 네임드 튜플은 객체의 단순한 대안이 될 수 있다.
- ### 함수의 인자들은 튜플로 전달된다.      
		
<br>

# Dictionary
### 딕셔너리는 값에 상응하는 고유한 키를 지정한다. <br>
### 키는 대부분 문자열이지만, 어떤 타입도 될 수 있다.<br>

<br>

## :pushpin: base
- ### dict(list1) : 리스트 원소가 (키, 값)으로 구성되어있으면 사전으로 변환
	- 같은 key를 두번 사용 하는 경우 마지막 값이 그 key의 값이 된다.
- ### dict1.update(dict2) : dict1에 dict2를 추가
- ### del dict1['key'] : 해당 항목 삭제하기
- ### dict1.clear() : 모든 항목 삭제
- ### 'key'  in dict1 : 'key'가 dict1에 있는 키인지 확인
- ### 그 외는 [주석 참고](https://github.com/Develope-my-tech/Python-Basic/blob/master/List%20%26%20Tuple%20%26%20dictionary/4.dictionary_base.py)

<br>

# Set
### Set은 키만 남은 딕셔너리와 같다.(유일해야함)<br>

<br>

## :pushpin: base
- ### set(dict1) : 키 값만 사용
- ### 셋 인터섹션 연산자(교집합 연산자) 
	- set1&set2
	- set1.intersection(set2)
- ### 셋 유니온 연산자 (합집합 연산자)
	- set1 | set2
	- set1.union(set2)
- ### 셋 디퍼런스 연산자(차집합 연산자)
	- set1 - set2
	- set1.difference(set2)
- ### 셋 익스클루시브 연산자(대칭 차집합 : 양쪽 모두에 들어있지 않은 멤버)
	- set1^set2
	- set1.symmetric_difference(set2)
- ### 셋 서브셋 연산자(부분집합 체크)
	- set1 <= set2 : set1이 set2에 부분집합인가?
	- set1.issubset(set2) : set1이 set2에 부분집합인가?
- ### 셋 프로퍼 서브셋(진부분집합 체크)
	- set1 < set2 : set1이 set2의 진부분집합인지
	  (두번째 셋에 첫번째 셋 모든 멤버를 포함하는 멤버 구성이어야한다.)
	  
		