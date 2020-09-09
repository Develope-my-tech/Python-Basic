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

# @데커레이션 이름 친 후에
# add_ints함수 전문을 써줘서 사용할 수 있다.

## 이해가 잘 가지 않아 블로그 검색을 해보았다.

def decorator_f(func):
    def wrapper_f(*args): # 예시에선 매개변수로 *args, **kwargs 로 줬음
        return func(*args)
    return wrapper_f

@decorator_f
def display():
    print('display 실행')

@decorator_f
def display_info(name, age):
    print('display_info({}, {}) 함수 실행'.format(name, age))

display()
display_info('john', 25)

# Class에서도 사용이 가능하다!
class decorator_class:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('%s 함수가 호출되기 전입니다.'% self.func.__name__)
        return self.func(*args, **kwargs)

@decorator_class
def display():
    print('display 실행')

@decorator_class
def display_info(name, age):
    print('display_info({}, {}) 함수 실행'.format(name, age))

display()
display_info('john', 25)

# 일반적으로 데코레이터는 로그를 남기거나 유저의 로그인 상태를 확인,
# 혹은 프로그램의 성능 테스트에서 많이 쓰인다고 한다.

