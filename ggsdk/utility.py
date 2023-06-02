#!/usr/bin/env python
#coding:utf-8

import logging
import threading
import six

_DEFAULT_LOGGER = None
__LOGGER_LOCK = threading.Lock()


def get_default_logger(simple_fmt=True, logger=None):
    global _DEFAULT_LOGGER
    if _DEFAULT_LOGGER is None:
        __LOGGER_LOCK.acquire()
        if _DEFAULT_LOGGER is None:
            if logger is None:
                logger = logging.getLogger('_utility_default_')
            hdl = logging.StreamHandler()
            hdl.setFormatter(logging.Formatter(
                '%(levelname)s %(asctime)s %(thread)d %(message)s' if simple_fmt else '%(levelname)s %(asctime)s %(process)d %(thread)d %(message)s'))
            hdl.setLevel(logging.DEBUG)
            logger.addHandler(hdl)
            logger.setLevel(logging.DEBUG)
            _DEFAULT_LOGGER = logger
        __LOGGER_LOCK.release()
    return _DEFAULT_LOGGER


def unicode_to_str(u_or_str, enc='utf-8'):
    if isinstance(u_or_str, (six.text_type, six.binary_type)):
        return six.ensure_str(u_or_str)
    return u_or_str


def str_to_unicode(u_or_str, enc='utf-8'):
    if isinstance(u_or_str, six.string_types):
        return six.ensure_text(u_or_str)
    return u_or_str

