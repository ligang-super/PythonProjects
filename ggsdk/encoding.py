#!/usr/bin/env python
# coding=utf-8

import re
import six

def to_str(s, encoding='utf-8'):
    """
    Returns a bytestring version of 's', encoded as specified in 'encoding'.
    """
    if isinstance(s, (six.string_types, six.binary_type)):
        return six.ensure_str(s, encoding=encoding)
    return str(s)


def to_unicode(s, encoding='utf-8'):
    """
    Similar to smart_unicode, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.
    """
    # Handle the common case first, saves 30-40% in performance when s
    # is an instance of unicode. This function gets called often in that
    # setting.

    if isinstance(s, (six.string_types, six.binary_type)):
        return six.ensure_text(s, encoding=encoding)
    return s

s = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]')
def filter_invalid_charset(string):
    try:
        return s.sub(' ', string)
    except:
        try:
            return string.decode('utf8', 'ignore').encode('utf8')
        except:
            return ''
