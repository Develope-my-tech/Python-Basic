'''     디렉터리 함수     '''

import os

# 1. mkdir() : 폴더 만들기
os.mkdir('poems')
print(os.path.exists('poems'))  # True

# 2. rmdir() : 삭제하기
os.rmdir('poems')
print(os.path.exists('poems'))  # False

# 3. listdir() : 콘텐츠 나열
os.mkdir('poems')
os.mkdir('poems/mcintyre')
print(os.listdir('poems'))  # ['mcintyre']

fout = open('poems/mcintyre/the_good_man', 'wt')
print(fout.write('''Cheerful and happy was his mood,
He to the poor was kin and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had panned a sonnet in his praise,
'Tis sad, but such is world's ways.
'''))   # 240
fout.close()

# 콘텐츠 나열
print(os.listdir('poems/mcintyre')) # ['the_good_man']

# 4. chdir() : 현재 디렉터리 바꾸기
os.chdir('poems')
print(os.listdir('.'))  # ['mcintyre']

# 5. glob() : 일치하는 파일 나열
'''
- 모든 것에 일치 : * (re 모듈에서의 .*와 같다.)
- 한 문자에 일치 : ?
- a,b 혹은 c 문자에 일치 : [abc]
- a,b 혹은 c를 제외한 문자에 일치 : [!abc]
'''
import glob
print(glob.glob('m*'))  # m으로 시작하는 파일, 디렉터리             # ['mcintyre']
print(glob.glob('??'))  # 두 글자로 된 파일 or 디렉터리             # []
print(glob.glob('m??????e'))  # m으로 시작, e로 끝나는 여덟글자     # ['mcintyre']
print(glob.glob('[klm]*e')) # k,l,m으로 시작하고 e로 끝나는 단어    # ['mcintyre']