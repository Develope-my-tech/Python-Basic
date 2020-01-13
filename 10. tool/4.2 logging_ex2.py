import logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger('bunyan')    # bunyan이라는 로거 객체 생성
logger.debug('Timber!')

# DEBUG:bunyan:Timber!
