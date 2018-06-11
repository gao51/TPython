import logging
import getpass
import sys
class Mylog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logFile = './testLog.log'
        print(logFile)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.ERROR)#只记录erro到logfile中
        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)
        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warning(msg)

    def erro(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = Mylog()
    mylog.debug("debug")
    mylog.info("info")
    mylog.warn("warn")
    mylog.erro("erro")
    mylog.critical("critical")
