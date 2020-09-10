import time
import logging

logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.INFO)
for i in range(0,100):
    # time.sleep(1)
    logging.info(i)