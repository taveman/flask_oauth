"""
Logger filters
"""
from logging import LogRecord


class LoggerFilterOutAbove:
    """
    Class that filters out logging events which have a logging level above the threshold
    """
    def __init__(self, filter_level: int):
        self._filter_level = filter_level

    def filter(self, record: LogRecord):
        """
        :return: True if log level is lower that INFO level
        """
        return record.levelno < self._filter_level
