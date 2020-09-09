poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
And returned on the previous night.'''


'''     파일 쓰기       '''

print(len(poem))    # 131

# fout = open('relativity', 'wt')
# 파일을 쓰는 두가지 방법
# 1.
# print(fout.write(poem))   # 131 : 파일에 쓴 바이트 수를 반환
# 2.
# print(poem, file=fout)  # 131 : 파일에 쓴 바이트 수를 반환
# print()는 각 인자 뒤에 스페이스를, 끝에 줄바꿈을 추가한다.
# fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
# sep 기본 스페이스(''), end 기본 줄바꿈('\n')
fout.close()

# 파일에 쓸 문자열이 크면 특정 단위로 나누어 파일에 씀
# fout1 = open('relativity', 'wt')
# size = len(poem)
# offset=0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     fout1.write(poem[offset:offset+chunk])
#     offset += chunk
# fout1.close()

# 파일을 덮어쓰지 못하게 할 수도 있다.
try:
    fout2 = open('relativity', 'xt')    # 덮어쓰기 금지
    fout2.write('stomp stomp stomp')
except FileExistsError:
    print('File already exists. close one')


'''     텍스트 파일 읽기       '''

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))    #   131

# 한번에 읽을 크기 제한
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)  # 한번에 100문자씩
    if not fragment:    # 파일을 다 읽으면 빈 문자열('')을 반환(False)
        break
    poem += fragment
fin.close()


poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()   # 한 줄씩 읽기
    if not line:    # 파일을 다 읽으면 빈 문자열('')을 반환.
        break
    poem += line
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read') # 4 lines read

for line in lines:
    print(line, end='')
# There was a young lady named Bright,
# Whose speed was far faster than light;
# She started one day
# And returned on the previous night.

'''     이진 파일 쓰기      '''
bdata = bytes(range(0, 256))
print(len(bdata))   # 256

fout = open('bfile', 'wb')
print(fout.write(bdata))    # 256
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset+chunk]))   # 100 100 56
    offset += chunk
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))   # 256
fin.close()

with open('relativity', 'wt') as fout:
    print(fout.write(poem)) # 131
# 열려 있는 파일을 닫지 않았을 때 이 파일이 더 이상 참조되지 않다는 것을
# 확인한 뒤 파일을 닫는다.

# tell() 함수 : 파일의 시작으로부터의 현재 오프셋을 바이트 단위로 반환
fin = open('bfile', 'rb')
print(fin.tell())   # 0

# seek() 함수 : 다른 바이트 오프셋으로 위치를 이동
print(fin.seek(255))    # 255

bdata = fin.read()
print(len(bdata))
print(bdata[0]) # 255

''' seek(offset, origin)
- origin = 0 : 기본값, 시작 위치에서 offset 바이트 이동
- origin = 1 : 현재 위치에서 offset 바이트 이동
- origin = 2 : 마지막 위치에서 offset 바이트 전 위치로 이동
'''

# 표준 os 모듈에 정의되어 있음
import os
print(os.SEEK_SET)  # 0
print(os.SEEK_CUR)  # 1
print(os.SEEK_END)  # 2

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))  # 255   마지막에서 1바이트 전 위치로 이동
print(fin.tell())   # 255

bdata = fin.read()
print(len(bdata))   # 1
print(bdata[0]) # 255


print(fin.seek(254, 0)) # 254
print(fin.tell())   # 254


print(fin.seek(1, 1))   # 255
print(fin.tell())   # 255