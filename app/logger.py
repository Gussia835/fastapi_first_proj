import logging


def setup_logger():
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.formatter(formatter)

    logger.addHandler(ch)
    return logger

logger = setup_logger()