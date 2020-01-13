'''
logging 모듈
- 로그에 저장할 메시지
- 상위 우선 레벨과 그 함수들 debug(), info(), warn(), error(), critical()
- 모듈과 연결되는 하나 이상의 로거(logger) 객체
- 터미널, 파일, 데이터베이스 등으로 메시지를 전달하는 핸들러
- 결과를 생성하는 포매터
- 입력을 기반으로 판단하는 필터
'''

import logging
logging.debug("Looks like rain")
logging.info("And hail")
logging.warning("Did I hear thunder?")
# WARNING:root:Did I hear thunder?
logging.error("Was that lightning?")
# ERROR:root:Was that lightning?
logging.critical("Stop fencing and get inside!")
# CRITICAL:root:Stop fencing and get inside!

'''
기본 우선 레벨은 WARNING이고, 
logging.debug()가 호출되자마자 잠긴다.
'''
