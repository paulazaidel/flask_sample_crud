import logging


def initialize_log():
    logging.basicConfig(level=logging.INFO)
    handler = logging.FileHandler("logfile.log")
    logger = logging.getLogger("werkzeug")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


logger = initialize_log()
