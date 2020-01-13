import logging

logging.basicConfig(level=logging.DEBUG)    # DEBUG보다 높은 모든 레벨이 출력
logging.debug("It's raining again")
logging.info("With hail the size of hailstones")

# DEBUG:root:It's raining again
# INFO:root:With hail the size of hailstones
