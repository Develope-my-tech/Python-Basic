import math
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# fabs : 인자의 절댓값 반환
print(math.fabs(98.6))  # 98.6
print(math.fabs(-271.1))    # 271.1

# floor : 내림, ceil : 올림
print(math.floor(98.6))     # 98
print(math.floor(-271.1))   # -272
print(math.ceil(98.6))  # 99
print(math.ceil(-271.1))    # -271

# factorial : 팩토리얼
print(math.factorial(0))    # 1
print(math.factorial(2))    # 2
print(math.factorial(10))   # 3628800

# sqrt : 제곱근
print(math.sqrt(100.0))     # 10.0

# hypot : 빗변의 길이 구하기
x = 3.0
y = 4.0
print(math.hypot(x, y)) # 5.0

print(math.sqrt(x*x+y*y))   # 5.0
print(math.sqrt(x**2+y**2)) # 5.0

# radians : 각도의 좌표를 변환
print(math.radians(180.0))  # 3.141592653589793

