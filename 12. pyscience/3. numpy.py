import numpy as np

# 1. 배열 만들기 : array
b = np.array([2, 4, 6, 8])
print(b)        # [2 4 6 8]
# ndim : 랭크를 반환
print(b.ndim)   # 1
# size : 배열에 있는 값의 총 개수 반환
print(b.size)   # 4
# shape : 각 랭크에 있는 값의 개수 반환
print(b.shape)  # (4,)

a = np.arange(10)
print(a)    # [0 1 2 3 4 5 6 7 8 9]
print(a.ndim)   # 1
print(a.shape)  # (10,)
print(a.size)   # 10

a = np.arange(7, 11)
print(a)    # [ 7  8  9 10]

f = np.arange(2.0, 9.8, 0.3)
print(f)
# [2.  2.3 2.6 2.9 3.2 3.5 3.8 4.1 4.4 4.7 5.  5.3 5.6 5.9 6.2 6.5 6.8 7.1
#  7.4 7.7 8.  8.3 8.6 8.9 9.2 9.5 9.8]

g = np.arange(10, 4, -1.5, dtype=np.float)
print(g)    # [10.   8.5  7.   5.5]

a = np.zeros((3,))
print(a)        # [0. 0. 0.]
print(a.ndim)   # 1
print(a.shape)  # (3,)
print(a.size)   # 3

b = np.zeros((2, 4))
print(b)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
print(b.ndim)   # 2
print(b.shape)  # (2, 4)
print(b.size)   # 8

k = np.ones((3, 5))
print(k)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

m = np.random.random((3, 5))
print(m)
# [[0.92144665 0.79460743 0.98429623 0.5172086  0.0727177 ]
#  [0.3467992  0.07082806 0.06713763 0.92576145 0.37867405]
#  [0.57972622 0.02252859 0.66872603 0.70532502 0.7316084 ]]

a = np.arange(10)
a = a.reshape(2, 5)
print(a)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
print(a.ndim)   # 2
print(a.shape)  # (2, 5)
print(a.size)   # 10

a = a.reshape(5, 2)
print(a)
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]
print(a.ndim)   # 2
print(a.shape)  # (5, 2)
print(a.size)   # 10

a.shape = (2, 5)
print(a)

# 배열 연산
from numpy import *
a = arange(4)
a *= 3
print(a)    # [0 3 6 9]

plain_list = list(range(4))
print(plain_list)   # [0, 1, 2, 3]
plain_list = [num*3 for num in plain_list]
print(plain_list)   # [0, 3, 6, 9]

a = zeros((2, 5)) + 17.0
print(a)
# [[17. 17. 17. 17. 17.]
#  [17. 17. 17. 17. 17.]]

# @ : 행렬 곱
a = np.array([[1,2], [3,4]])
b = a @ a
print(b)
# [[ 7 10]
#  [15 22]]

# 선형 대수
# 4x + 5y = 20
# x + 2y = 13
coefficients = np.array([ [4,5], [1,2]])
dependents = np.array([20, 13])
answer = np.linalg.solve(coefficients, dependents)
print(answer)
# [-8.33333333 10.66666667]

print(4 * answer[0] + 5 * answer[1] )   # 20.0
print(1 * answer[0] + 2 * answer[1] )   # 13.0

product = np.dot(coefficients, answer)
print(product)  # [20. 13.]
print(np.allclose(product, dependents)) # True

