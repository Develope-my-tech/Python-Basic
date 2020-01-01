'''     file 함수에 대해서 알아보자   '''

# 1. open()
fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()
# oops.txt 파일에 Oops, I created a file.를 씀

# 2. exists()
import os
print(os.path.exists('oops.txt'))   # True
print(os.path.exists('./oops.txt')) # True
print(os.path.exists('waffles'))    # False
print(os.path.exists('.'))          # True
print(os.path.exists('..'))         # True

# 2. isfile()
name = 'oops.txt'
print(os.path.isfile(name)) # True
print(os.path.isdir(name))  # False
print(os.path.isdir('.'))   # True
print(os.path.isabs('name'))    # isabs는 인자가 절대 경로인지 확인 / 출력 : False
print(os.path.isabs('/python_basic/8. system/name'))    # True

# 3. copy()
import shutil
shutil.copy('oops.txt', 'ohno.txt')
# oops.txt를 ohno.txt로 복사한다.
# shutil.move()함수는 파일을 복사한 후 원본 파일을 삭제

# 4. rename()
os.rename('ohno.txt', 'ohwell.txt')
# ohno.txt --> ohwell.txt  로 바꿈

# 5. link(), symlink()
os.link('oops.txt', 'yikes.txt')    # 하드 링크 생성 (저수준)
print(os.path.isfile('yikes.txt'))  # True

print(os.path.islink('yikes.txt'))
# os.symlink('oops.txt', 'jeepers.txt')   # 심벌릭 링크
# print(os.path.islink('jeepers.txt'))

# 6. chmod() : 퍼미션 바꾸기
os.chmod('oops.txt', 0o400) # 파일의 소유자(파일을 생성한 사용자)만 읽을 수 있도록

import stat
os.chmod('oops.txt', stat.S_IRUSR)  # stat을 임포트해서 쓸 수도 있음 ( 8진수 쓰는 것 대신)

# 7. chown()
# uid = 5
# gid = 22
# os.chown('oops', uid, gid)

# 8. abspath() : 절대 경로 얻기
print(os.path.abspath('oops.txt'))
# C:\jupyternotebook\python_basic\8. system\oops.txt

# 9. realpath() : symbolic link 경로 얻기
# print(os.path.realpath('jeepers.txt'))

# 10. remove()
os.remove('oops.txt')   # 권한이 있어야함.
print(os.path.exists('oops.txt'))
