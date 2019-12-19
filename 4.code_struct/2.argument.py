# 위치 인자 모으기 : *
def print_more(r1, r2, *args):
    print('r1 : ', r1)
    print('r2 : ', r2)
    print('all the rest : ', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
# *는 매개변수에서 위치 인자 변수들을 튜플로 묶는다.

# 키워드 인자 모으기 : **
# 키워드 인자를 딕셔너리로 묶음
def print_kwargs(**kwargs):
    print('키워드 인자 : ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macarron')

# docstring : 함수 정의에 문서를 붙일 수 있다.
def echo(anything):
    'echo returns its input arguement'

    return anything
help(echo)
# 결과물
# Help on function echo in module __main__:
#
# echo(anything)
#     echo returns its input arguement

print(echo.__doc__)
# 결과 : echo returns its input arguement

