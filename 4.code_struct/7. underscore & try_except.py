# underscore
# def underscore_ex():
#     '''this is underscore example
#     function name is underscore_ex'''
#     print('This is function is named: ', underscore_ex.__name__)
#     print('And its docstring is: ', underscore_ex.__doc__)
#
# underscore_ex()


# try_catch
# short_list = [1, 2, 3]
# while True:
#     value = input('q to quit?')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index : ', position)
#     except Exception as other:
#         print('Something else broke:', other)

# 특별한 상황에 따른 예외 처리 만들기
class OopsException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise OopsException('panic')
        except OopsException as exc:
            print(exc)


