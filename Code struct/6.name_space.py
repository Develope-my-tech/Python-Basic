animal = 'bear'

# def print_global():
#     print('name : ', animal) # 에러 생김
#     animal = 'monkey'
#     print('name : ', animal)

# def change_name():
#     global animal # 전역 변수를 가져옴
#     animal = 'monkey'
#     print('name : ', animal)
#
# change_name()

def change_name():
    animal = 'wombat'
    animal2  = 'monkey'
    print('locals:', locals())

change_name() # 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환
print('global : ', globals())
