poem = '''All that doth flow we cannot liquid name
or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get
Then it's not cold that doth the fire put out
But it's the wet that makes it die, no dout.'''

print(poem.startswith('All'))
# 이 시는 "All" 로 시작하는 가?

print(poem.endswith('That\'s all, folks!'))
# 이 시는 "That's all, folks!" 로 끝나는 가?

word = 'the'
print(poem.find(word))
# 첫번째 'the'가 나오는 오프셋은?
# ++) rfind

print(poem.isalnum())
# 이 시는 글자와 숫자로만 이루어져 있습니까?
