# 데이터 값을 문자열에 끼워넣기 : format

# [첫번째] 파이썬 2에서 쓰던 %
n = 42; f =7.03;   s = 'string cheese'
print('%10.4d %10.4f %10.4s' % (n, f, s))
# 출력 :       0042     7.0300       stri
# 10.4d : 10자 필드 오른쪽 정렬 및 최대 문자길이 4
# 10.4f : 10자 필드 오른쪽 정렬 및 소수점 이후 숫자길이 4
# 10.4s : 10자 필드 오른쪽 정렬 및 최대 문자길이 4

# 인자로 필드 길이 지정도 가능하다.
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))
# 결과는 위와 같다.

# [두번째] {}
print('{} {} {}'.format(n, f, s))
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
# 출력 : 42 7.03 string cheese

print('{2} {0} {1}'.format(n, f, s))    # 순서 지정도 가능
# 출력 : string cheese 42 7.03

d = {'n':42, 'f':7.03, 's':'string cheese'}  # 딕셔너리를 넣어보자!
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))
# 출력 : 42 7.03 string cheese other

print('{0:d} {1:f} {2:s}'.format(n, f, s))  # 타입 지정해주기
# 출력 : 42 7.030000 string cheese

print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))  # 인자에 이름 지정
# 출력 : 42 7.030000 string cheese

print('{0:10d} {1:10f} {2:10s}'.format(n, f, s)) # 최소 필드 길이 10, 오른쪽 정렬
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s)) # '>'를 통해 오른쪽 정렬을 명확히 표현
# 공통된 출력 :         42   7.030000 string cheese

print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s)) # 왼쪽 정렬
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s)) # 오른쪽 정렬
# 출력 : 42         7.030000   string cheese
# 출력 :     42      7.030000  string cheese

print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))
# 정수는 10.4d를 사용할 수 없다!!!!
# 출력 :         42     7.0300       stri

print('{0:!^20s}'.format('BIG SALE'))   # 길이 지정자 이전에 채워 넣고 싶은 문자를 입력
# 출력 : !!!!!!BIG SALE!!!!!!