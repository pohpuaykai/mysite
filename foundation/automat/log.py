import logging

logger = logging.getLogger(__name__)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
format = '%(asctime)s %(levelname)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d:%(message)s'
#for more: https://docs.python.org/3/howto/logging.html
logging.basicConfig(format=format, encoding='utf-8', level=logging.DEBUG)

def debug(msg):
    logging.debug(msg, stacklevel=2)

def info(msg):
    logging.info(msg, stacklevel=2)

def warning(msg):
    logging.warning(msg, stacklevel=2)

def error(msg):
    logging.error(msg, stacklevel=2)