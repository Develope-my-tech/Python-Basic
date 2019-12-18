# zip 예시
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
# 결과 : [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

# list 컴프리헨션
# [ 표현식 for 항목 in 순회 가능한 객체 if 조건 ]
arr = [ num for num in range(1, 6) if num % 2 == 1 ]
print(arr)

# 중첩 루프에서 리스트 컴프리헨션
rows = range(1, 4)
cols = range(1, 4)
cells = [(row, col) for row in rows for col in cols]
print(cells)
# 결과 : [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# 한줄로 쓸 때도 for 문 순서는 일반 중첩 루프 순서와 동일하다!

# 딕셔너리 컴프리헨션
word = 'letters'
letter_counts = { letter:word.count(letter) for letter in word }
print(letter_counts)
# 결과 : {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

# 튜플은 컴프리헨션이 없다. () 로 작성시 --> 제너레이터 컴프리헨션
num_arr = (num for num in range(1, 6))
print(num_arr)
# 결과 : <generator object <genexpr> at 0x0000014FD60685C8>

