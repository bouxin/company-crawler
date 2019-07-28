#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-11
:desc:
"""
import logging
import os
from logging.handlers import TimedRotatingFileHandler


def set_file(filename):
    logger = logging.getLogger()
    os.getcwd()
    handler = TimedRotatingFileHandler(filename, 'D', 1, 7)
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt=fmt, datefmt='%m/%d/%Y %H:%M:%S')

    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    # 屏幕输出
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)
    logger.addHandler(console)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)





