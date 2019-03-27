#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""
import logging
from urllib import parse as url_encoder

logging.basicConfig(filename='../tianyancha.log', format='')  # todo


def warn(msg: str):
    logging.warning(msg)


def info(msg: str):
    logging.info(msg)


def error(msg: str):
    logging.error(msg)


def debug(msg: str):
    logging.debug(msg)


if __name__ == '__main__':
    print(url_encoder.quote('微策略软件杭州'))
