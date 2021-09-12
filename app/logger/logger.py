"""
Logger initializer
"""

import os
import logging.config
import yaml


def _setup_logger() -> logging.Logger:
    """
    Initialize logger
    """
    logger = logging.getLogger('oauth')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logger_config_file = os.path.join(current_dir, 'logger.yml')

    with open(logger_config_file, 'rt') as _file:
        config = yaml.safe_load(_file.read())

    logging.config.dictConfig(config)

    return logger


log = _setup_logger()
