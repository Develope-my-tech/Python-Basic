'''
unittest
소스 컨트롤 시스템에서 코드를 커밋하기전에,
독립적인 테스트 프로그램을 작성하여 코드를 검증
(특히 회귀 테스트)
'''

from packs import cap   # cap.py : 단어 첫 글자를 대문자로 바꾸는 모듈 작성
import unittest

class TestCap(unittest.TestCase):

    def setUp(self):
        pass    # 테스트 메서드 전에 호출

    def tearDown(self):
        pass    # 테스트 메서드 후에 호출

    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Duck')    # assertion : 예상되는 결과

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')

    def test_words_with_apostrophes(self):
        text = "I'm fresh out of ideas"
        result = cap.just_do_it(text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")

    def test_words_with_quotes(self):
        text = "\"You're despicable,\" said Daffy Duck"
        result = cap.just_do_it(text)
        self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")

if __name__ == '__main__':
    unittest.main()

'''
출력
Traceback (most recent call last):
  File "2.3 unittest.py", line 27, in test_multiple_words
    self.assertEqual(result, 'A Veritable Flock Of Ducks')
AssertionError: 'A veritable flock of ducks' != 'A Veritable Flock Of Ducks'
- A veritable flock of ducks
?   ^         ^     ^  ^
+ A Veritable Flock Of Ducks
'''

# cap.py에서 capitalize() 대신에 title()로 하면 잘 동작.
# ++) I'm 을 title() 실행 시키면 I'M이 되는 오류가 있음.
#   ---> 헬퍼 함수인 capwords() 사용해보자

'''
test_words_with_quotes() 함수에서 .... 
capwords()가 첫번째 "를 인식해 나머지(You're)을 소문자로 바꾸는 오류 발생.

- "you're Despicable," Said Daffy Duck
?  ^
+ "You're Despicable," Said Daffy Duck
?  ^
'''