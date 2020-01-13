'''
timeit.timeit(code, number, count)
'''

from timeit import timeit
print(timeit('num=5;num*=2', number=1))
# 2.5000000000025002e-06

from timeit import repeat
print(repeat('num=5;num*=2', number=1, repeat=3))
# [5.000000000005e-07, 3.000000000086267e-07, 3.000000000086267e-07]