
# String  
  
## :pushpin: 문자추출 '[ ]'  
### 한 문자를 얻기 위해 문자열 이름 뒤에 대괄호([])와 오프셋을 지정한다.<br>  
### 그러나 문자열은 불변하기 때문에 특정 인덱스에 문자를 삽입하거나 변경할 수 없다.<br>  

```python
name = 'Henny'  
name[0] = 'P'  # error  
``` 
  
<br>  
  
## :pushpin: Slice (:zap:인덱싱도 잘 파악:zap:)  
  
```python
letters = '1234567890'    
print(letters)        # '1234567890'    
print(letters[5:])     # '67890'    
print(letters[4:6])        # '56'    
print(letters[-3:])     # '890'    
print(letters[2:-3])    # '34567'    
print(letters[1:6:2])   # '246'    
print(letters[6:1:-2])  # '753'  
```
<br>  
  
## :pushpin: Quotation mark 
  
- 큰 따옴표 " " 와 작은 따옴표 ' '  
- 두 개 다 사용하여 큰 따옴표 혹은 작은 따옴표를 표현할 수 있다.

- 세 개의 단일 이중 부호  ⇒  여러 줄의 문자열에 사용
	- 공백, \n 등 이 보존
	- 그러나 대화식 인터프리터(>>>)에서의 결과는 공백과 줄바꿈을 표시해준다. <br>
		
		  출력 :   '이런식으로\n     여러 줄의 문자열을\n    출력하는데 사용한다.'

<br>

## :pushpin: String function

- str : 문자열
- str.startswith("etc") : 'etc' 문자열로 시작하는가?
- str.endswith("etc") : 'etc' 문자열로 끝나는가?
- str.find("etc") : "etc"가 나오는 offset은?
	- str.lfind()
	- str.rfind()
- str.isalnum() : str은 글자와 숫자로만 이루어져 있는가?

<br>

## :pushpin: Capitalize
- str.strip("etc") : "etc" 시퀀스 삭제
-  str.capitalize() : 첫번째 단어를 대문자로 변경
- str.title() : 모든 단어의 첫번째를 대문자로 변경
- str.upper() : 모두 대문자로 변경
- str.lower() : 모두 소문자로 변경
- str.swapcase() : 대문자 ⇒ 소문자 / 소문자 ⇒ 대문자
- str.center(n) : 지정 공간 n에서 중앙 배치 (n은 정수)
- str.ljust(n) : 왼쪽 배치
- str.rjust(n) : 오른쪽 배치

<br>

