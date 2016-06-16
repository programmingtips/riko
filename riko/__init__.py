# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab
"""
riko
~~~~
Provides functions for analyzing and processing streams of structured data

Examples:
    basic usage::

        >>> from itertools import chain
        >>> from riko.modules.pipeitembuilder import pipe as itembuilder
        >>> from riko.modules.pipestrreplace import pipe as strreplace
        >>> from riko.collections.sync import SyncPipe
        >>>
        >>> ib_conf = {
        ...     'attrs': [
        ...         {'key': 'link', 'value': 'www.google.com', },
        ...         {'key': 'title', 'value': 'google', },
        ...         {'key': 'author', 'value': 'Tommy'}]}
        >>>
        >>> sr_conf = {
        ...     'rule': [{'find': 'Tom', 'param': 'first', 'replace': 'Tim'}]}
        >>>
        >>> items = itembuilder(conf=ib_conf)
        >>> replaced = (
        ...     strreplace(i, conf=sr_conf, field='author') for i in items)
        >>> next(chain.from_iterable(replaced)) == {
        ...     'link': 'www.google.com', 'title': 'google',
        ...     'strreplace': 'Timmy', 'author': 'Tommy'}
        True
"""
from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from os import path as p
from builtins import *

__version__ = '0.32.1'

__title__ = 'riko'
__package_name__ = 'riko'
__author__ = 'Reuben Cummings'
__description__ = 'A stream processing engine modeled after Yahoo! Pipes.'
__email__ = 'reubano@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Reuben Cummings'


def get_path(name):
    return 'file://%s' % p.join('data', name)