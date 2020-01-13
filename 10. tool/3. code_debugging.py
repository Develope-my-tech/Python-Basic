'''
파이썬에서 디버깅하는 가장 간단한 방법은
문자열을 출력하는 것이다.
- vars() : 함수의 인자값과 지역 변수값을 추출
'''

def func(*args, **kwargs):
    print(vars())

func(1, 2, 3)
# {'args': (1, 2, 3), 'kwargs': {}}

'''
데커레이터(decorator)를 사용하면 함수 내의 코드를 수정하지 않고,
이전 혹은 이후에 코드를 호출할 수 있다.
'''

def dump(func):
    "인자값과 결과값을 출력한다."
    def wrapped(*args, **kwargs):
        print("Function name: {}".format(func.__name__))
        print("Input arguments: {}".format(''.join(map(str, args))))
        print("Input keyword arguments: {}".format(kwargs.items()))
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return wrapped

@dump
def double(*args, **kwargs):
    "모든 인자값을 두 배로 반환한다."
    output_list = [ 2 * arg for arg in args ]
    output_dict = { k:2*v for k,v in kwargs.items() }
    return output_list, output_dict

if __name__ == '__main__':
    output = double(3, 5, first=100, next=98.6, last=-40)

'''
출력
Function name: double
Input arguments: 35
Input keyword arguments: dict_items([('first', 100), ('next', 98.6), ('last', -40)])
Output: ([6, 10], {'first': 200, 'next': 197.2, 'last': -80})
'''

