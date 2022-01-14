#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import logging
from tianyancha.client import TycClient


def start():
    def __printall(items):
        for elem in items:
            logging.info(elem.__str__())

    """ 入口函数 """
    keys = globals().get('keywords', [])
    for key in keys:
        logging.info('正在采集[%s]...' % key)
        companies = TycClient().search(key).companies
        __printall(companies)
    logging.info("completed")


def load_keys(keys: list):
    globals().setdefault('keywords', keys)





