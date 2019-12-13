marxes = ['Groucho', 'Chico', 'Harpo']

# 리스트 끝에 항목 추가하기
marxes.append('Zeppo')
print(marxes)

# 리스트 병합하기
others = ['Gummo', 'Karl']
marxes.extend(others) # marexs += others 도 가능
# (주의) append로 추가할 경우 ['Gummo', 'Karl'] 리스트 자체가 추가됨

# 오프셋으로 항목 추가하기
marxes.insert(3, 'Hihi')
print(marxes)

# 오프셋으로 항목 삭제
# del은 함수가 아니라 파이썬 구문! <--> 할당(=)과 반대!
del marxes[-1]
print(marxes)

# 값으로 항목 삭제
marxes.remove('Harpo')
print(marxes)

# 오프셋으로 항목 값을 얻으면서 리스트에서 삭제
marxes.pop(2)

# 값의 오프셋 찾기
print(marxes.index('Groucho'))

# count와 join은 생략

# sort() : 리스트 자체를 내부적으로 정렬
# sorted() : 리스트의 정렬된 복사본을 반환
sorted_marxes = sorted(marxes)

# 리스트를 복사하기
# 1. copy() 함수
a = [1, 2, 3]
b = a.copy()
print(a)

# 2. list+tuple+dictionary() 변환 함수
c = list(a)
print(c)

# 3. 슬라이스 [:]
d = a[:]
print(d)

