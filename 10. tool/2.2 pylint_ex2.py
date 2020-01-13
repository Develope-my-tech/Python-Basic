"모듈 docstring"

def func():
    "함수 docstring. 안녕, 엄마!"
    first = 1
    second = 2
    third = 3
    print(first)
    print(second)
    print(third)

if __name__ == '__main__':
    func()

'''
************* Module 2.2 pylint_ex2
2.2 pylint_ex2.py:1:0: C0103: Module name "2 pylint_ex2" doesn't conform to snake_case naming s
tyle (invalid-name)

------------------------------------------------------------------
Your code has been rated at 8.89/10 (previous run: 7.78/10, +1.11)

pylint는 docstring을 원한다. 그리고 a,b,c와 같은 짧은 변수 이름은 별로 탐탁치 않게 생각한다.

+)원래 10점도 가능한데 파일 이름때문에 깎인것으로 추정된다.

'''