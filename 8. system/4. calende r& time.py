import calendar

print(calendar.isleap(1900))    # False
print(calendar.isleap(1996))    # True
print(calendar.isleap(2000))    # True
print(calendar.isleap(2002))    # False
print(calendar.isleap(2004))    # True

''' 
1. datetime 모듈
- date : 년, 월, 일
- time : 시, 분, 초, 마이크로초
- datetime : 날짜와 시간
- timedelta : 날짜 와/또는 시간 간격
'''
from datetime import date
halloween = date(2020, 1, 1)
print(halloween)    # 2020-01-01
print(halloween.day)    # 1
print(halloween.month)  # 1
print(halloween.year)   # 2020
print(halloween.isoformat())    # 2020-01-01 (메서드로 출력 가능)

from datetime import date
now = date.today()  # 오늘 날짜 출력
print(now)  # 2020-01-01

from datetime import timedelta
one_day = timedelta(days=1) # 날짜 시간 간격 배정
tomorrow = now + one_day
print(tomorrow)     # 2020-01-02
print(now + 17 * one_day)
print(now - one_day) # 2019-12-31

from datetime import time
noon = time(12, 0, 0)
print(noon)         # 12:00:00
print(noon.hour)    # 12
print(noon.minute)          # 0
print(noon.second)          # 0
print(noon.microsecond)     # 0

import time
# 1970/1/1일 자정 이후 시간의 초를 사용 (epoch)
now = time.time()
print(now)  # 1577878707.9758263

print(time.ctime(now))  # epoch 값을 문자열로
# Wed Jan  1 20:39:50 2020

print(time.localtime(now))  # 시간을 시스템 표준 시간대로
print(time.gmtime(now))     # 시간을 UTC로 제공한다.
# time.struct_time(tm_year=2020, tm_mon=1, tm_mday=1, tm_hour=20, tm_min=42, tm_sec=29, tm_wday=2, tm_yday=1, tm_isdst=0)

tm = time.localtime(now)
print(time.mktime(tm))  # 1577878949.0

ftm = "It's %A, %B %d, %Y, locatime %I:%M:%S%p"
t = time.localtime()
print(time.strftime(ftm, t))    # It's Wednesday, January 01, 2020, locatime 08:47:17PM

'''
*** strftime() 출력 지정자 ***
%Y : 년
%m : 월
%B : 월 이름
%b : 월 축약 이름
%A : 요일 이름
%a : 요일 축약 이름
%H : 24시간
%I : 12시간
%p : 오전/오후
%M : 분
%s : 초
'''

from datetime import time
some_time = time(10, 35)
print(some_time.strftime(ftm))  # It's Monday, January 01, 1900, locatime 10:35:00AM

import time
fmt = "%Y-%m-%d"
print(time.strptime("2020-01-10", fmt))
# time.struct_time(tm_year=2020, tm_mon=1, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=10, tm_isdst=-1)

import locale
from datetime import date
halloween = date(2015, 10, 31)
for lang_country in ['ko_kr', 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
    print(locale.setlocale(locale.LC_TIME, lang_country))   # setlocale()을 이용하여 로케일(국제화 설정)을 바꿈
    print(halloween.strftime('%A, %B %d'))

import locale
names = locale.locale_alias.keys()  # lang_country 값을 찾아보자
print(names)

good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(good_names[:5])   # ['a3_az', 'aa_dj', 'aa_er', 'aa_et', 'af_za']

de = [name for name in good_names if name.startswith('de')]
print(de)   # ['de_at', 'de_be', 'de_ch', 'de_de', 'de_it', 'de_lu']

