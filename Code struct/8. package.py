from sources import daily, weekly
print('Daily forecast:', daily.forecast())
print('Weekly forecast:')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# 사용자 정의 모듈
# 근데 왜 빨간 줄 뜨지
# 실행은 잘 된다. 설치도 다 완료
# --> code_struct를 mark as a source로 지정 후 해결

# 결과물
# Daily forecast: like yesterday
# Weekly forecast:
# 1 snow
# 2 more snow
# 3 sleet
# 4 freezing rain
# 5 rain
# 6 fog
# 7 hail