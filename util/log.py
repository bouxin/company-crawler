#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-11
:desc:
"""
import logging

LOG_FORMAT = '%(asctime)s - tianyancha-spider - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s'
logging.basicConfig(filename='tianyancha.log',
                    format=LOG_FORMAT,
                    datefmt='%m/%d/%Y %H:%M:%S')

logger = logging.getLogger()


def info(msg: str):
    logger.info(msg)


def debug(msg: str):
    logger.debug(msg)


def warn(msg: str):
    logger.warning(msg)


def error(msg: str):
    logger.error(msg)

