'''
로거 이름에 점(.) 문자가 포함된 경우, 각각의 다른 속성을 지닌 로거 계층 구조의 레벨을 점으로 구분한다.
quark.charmed라는 이름의 로거보다 quark라는 로거가 더 높다는 의미.
루트 로거는 제일 상단에 있고, 이름은 ''이다.
'''

import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warning("I need my axe")

'''
blue_ox.log 파일에 출력될 메시지가 들어간다.
'''