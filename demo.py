from us_visa.logger import logging
from us_visa.exception import UsVisaException
import os
import sys

if __name__ == '__main__':
    logging.info('Started')
    try:
        a = 1/0
        logging.info('Division by zero')
    except Exception as e:
        raise UsVisaException(e,sys)