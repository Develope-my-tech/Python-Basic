def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

print(edit_story(stairs, enliven))
print(edit_story(stairs, lambda word: word.capitalize() + '!'))
# 결과 : Thud!
# Meow!
# Thud!
# Hiss!
# None

# lambda 함수를 쓰면 한줄로 함수를 바로 쓸 수 있음