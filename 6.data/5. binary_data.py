'''
바이트(byte)는 바이트의 튜플처럼 불변한다.
바이트 배열(byte array)는 바이트의 리스트처럼 변경 가능하다.
'''

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes_array = bytearray(blist)
print(the_bytes)     # 출력 : b'\x01\x02\x03\xff'
print(the_bytes_array) # 출력 : bytearray(b'\x01\x02\x03\xff')

# the_bytes[1] = 127    !!! 바이트 변수 변경 시 에러 발생 !!!
the_bytes_array[1] = 127    # 바이트 변수는 변경이 가능하다.
print(the_bytes_array)  # 출력 : bytearray(b'\x01\x7f\x03\xff')

the_bytes = bytes(range(0, 256))
the_bytes_array = bytearray(range(0, 256))

print(the_bytes)
'''
출력 : 
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d
\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82
\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0
\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe
\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc
\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa
\xfb\xfc\xfd\xfe\xff'
'''
# 출력할 수 없는 바이트에 대해서는 '\x'를 사용한다.


'''
### 이진 데이터 변환하기 : struct ###
이진 데이터 --> 파이썬 데이터  또는
파이썬 데이터 --> 이진 데이터 
로 바꿀 수 있다.
'''

import struct
print(struct.pack('>L', 154))   # 출력 : b'\x00\x00\x00\x9a'
print(struct.pack('>L', 141))   # 출력 : b'\x00\x00\x00\x8d'
# struct 모듈의 pack() 함수로 파이썬 데이터 --> 바이트로 변환할 수 있다.

'''
pack()과 unpack()에 대한 형식 지정자

### 형식 문자열의 엔디안 지정자 ###
< : 리틀엔디안
> : 빅엔디안

?? 빅엔디안, 리틀 엔디안 이란?? ???
ex) 0x1234
빅엔디안 : 12 34    리틀 엔디안 : 34 12

빅엔디안은 사람이 숫자를 읽고 쓰는 방법과 같아 디버그가 편함
리틀엔디안은 메모리에 저장된 값의 하위 바이트만 사용할 때 별도의 계산이 필요 없다.

### 형식 지정자 ###
x : 1바이트 건너 뜀        (1byte)
b : 부호 있는 바이트       (1byte)
B : 부호 없는 바이트       (1byte)
h : 부호 있는 짧은 정수    (2byte)
H : 부호 없는 짧은 정수    (2byte)
i : 부호 있는 정수         (4byte)
I : 부호 없는 정수         (4byte)
l : 부호 있는 긴 정수      (4byte)
L : 부호 없는 긴 정수      (4byte)
Q : 부호 없는 아주 긴 정수 (8byte)
f : 단정도 부동소수점수    (4byte)
d : 배정도 부동소수점수    (8byte)
p : 문자수(count)와 문자   (1 + count)
s : 문자                   (count)

ex)
struct.unpack('>16x2L6x', data)
출력 : (154, 141)

- 빅엔디안 정수 형식(>)을 사용
- 16바이트를 건너뜀 (16x)
- 두 개의 부호 없는 긴 정수의 8바이트를 읽음 (2L)
- 마지막 6바이트를 건너뜀 (6x)
'''

'''
## 바이트/문자열 변환하기 : binascii() ##
binascii 모듈은 이진 데이터와 문자열(16진수, 64진수, uuencoded 등)을 서로 변환할 수 있는 함수를 제공
'''

# \x 대신 16진수의 시퀀스인 8바이트 png 헤더 출력
import binascii
#valid_png_header = b'\x89PNG\r\n\x1a\n'
# print(binascii.hexlify(valid_png_header))   # 출력 : b'89504e470d0a1a0a'
#
# print(binascii.unhexlify(b'\x89PNG\r\n\x1a\n')) # 출력 : b'89504e470d0a1a0a'
# PNG 데이터가 지금 다운로드하지 않아서 출력 확인은 하지 않겠다.

