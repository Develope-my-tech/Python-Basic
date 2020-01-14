# 정확한 부동소수점수 계산 : decimal

from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
print(total)    # 21.1894

penny = Decimal('0.01')
print(total.quantize(penny))    # 21.19


# 유리수 계산 : fractions
# 분자를 분모로 나눈 분수를 나타낼 수 있다.
from fractions import Fraction
print(Fraction(1, 3) * Fraction(2, 3))  # 2/9

print(Fraction(1.0/3.0))    # 6004799503160661/18014398509481984
print(Fraction(Decimal('1.0')/Decimal('3.0')))  # 3333333333333333333333333333/10000000000000000000000000000

import fractions
print(fractions._gcd(24, 16))   # 8
# gcd : 최소공약수