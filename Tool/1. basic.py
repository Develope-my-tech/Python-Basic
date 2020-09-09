'''
- 패키지 설치하기
1. pip
2. 패키지 매니저 : apt-get, yum, dpkg, zypper
3. 소스에서 설치
'''

'''
- 코드 테스트
1. pylint, pyflakes, pep8
'''

# pylint
a=1
b=2
# c=3
print(a)
print(b)
print(c)
'''
pylint로 실행시 출력 
1. basic.py:18:6: E0602: Undefined variable 'c' (undefined-variable)

Global evaluation 밑에 점수가 나온다.
Your code has been rated at -8.33/10 (previous run: -8.33/10, +0.00)

고친 경우
Your code has been rated at -3.75/10 (previous run: -8.33/10, +4.58)

'''

