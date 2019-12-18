# 클로져 : 다른 함수에 의해 동적으로 생성
def out(saying):
    def inner():
        return 'say : %s' %saying
    return inner
a = out('Duck')
print(a())
# 결과 : say : Duck
# out('Duck') 을 print하면 프로토타입이 나옴

