'''
        프로그램과 프로세스
하나의 프로그램을 실행할 때, 운영체제는 한 프로세스를 생성.
프로세스는 운영체제의 커널(파일과 네트워크 연결, 사용량 통계 등)에서 시스템 리소스(CPU, 메모리, 디스크 공간) 및 자료구조 사용
'''

import os

# 프로세트 ID와 현재 작업 디렉터리 위치 확인
print(os.getpid())  # 15288
print(os.getcwd())  # C:\jupyternotebook\python_basic\8. system

# 사용자 ID와 그룹 ID도 확인
# print(os.getuid())
# print(os.getgid())
#윈도우는 지원이 안됨

# 1. subprocess :: 프로세스 생성하기
import subprocess
ret = subprocess.getoutput('date') # ate 프로그램의 결과를 얻어온다
print(ret)
# 현재 날짜: 2020-01-01
# 새로운 날짜를 입력하십시오: (년-월-일)

''' 쉘 명령어라 파이썬에서 실행하기가 어려움.
ret = subprocess.getoutput('date -u | wc')      # 결과 : 1    6   29 (1줄, 6단어, 29 글자를 센다)

ret = subprocess.check_output(['date', '-u'])   # 표준 출력이 문자열이 아닌 바이트 타입을 반환

ret = subprocess.getstatusoutput('date')    # 프로그램 상태 코드와 결과를 튜플로 반환

ret = subprocess.call('date')   # 결과가 아닌 상태 코드만 저장
'''


