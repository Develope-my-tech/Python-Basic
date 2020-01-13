import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")

'''
acstime : ISO 8061 문자열의 날짜와 시간
level time : 레벨 이름
lineno : 라인 번호
message : 메시지
'''