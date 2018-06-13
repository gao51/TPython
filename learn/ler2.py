import logging
import threading


class TestLogging(object):
    def __init__(self):
        logFormat = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        logFileName = './testLog.txt'
        logging.basicConfig(level= logging.INFO,format=logFormat,filename=logFileName,filemode='w')

        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')
class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = TestLogging()
            MyLog.mutex.release()

        return MyLog.log
if __name__ == '__main__':
    # log = MyLog.get_log()
    # logger = log.get_logger()
    x = 'A5ED8E11836A9B99CDDCEFF7221FF0E51CE04ED2'
    print(x.lower())