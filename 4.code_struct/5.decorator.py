# 소스 코드를 수정하지 않고 사용하고 있는 함수를 수정하고 싶을 때
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running funtion : ', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result : ', result)
        return result
    return new_function
    # document_it 함수 실행 시 new_function이 생성됨

def add_ints(a, b):
    return a+b
cooler_add_ints = document_it(add_ints) # 데커레이터를 수동으로 할당
cooler_add_ints(3, 5)
# 출력
# Running funtion :  add_ints
# Positional arguments: (3, 5)
# Keyword arguments:  {}
# Result :  8

# terminal 에선 @데커레이션 이름 친 후에
# add_ints함수 전문을 써줘서 사용할 수 있다.