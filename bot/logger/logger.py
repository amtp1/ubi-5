import sys
import logging

file_handler = logging.FileHandler(filename='debug/logging.ini')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('user_id', self.extra['user_id'])
        return '[%s] %s' % (my_context, msg), kwargs

logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    handlers=handlers)
logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {"user_id": None})