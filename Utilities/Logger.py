import inspect
import logging


class LogGenerator:

    @staticmethod
    def log_gen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("Logs/PhpTravel_Automation.log")
        formatt = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s :%(lineno)d : %(message)s")
        logger.addHandler(logfile)
        logfile.setFormatter(formatt)
        logger.setLevel(logging.INFO)
        return logger
