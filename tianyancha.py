#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosin
:date: 03/28/2019
"""
from tianyancha import crawler as TycCrawler


if __name__ == '__main__':
    keys = ['Google']  # todo 查询字段设置
    TycCrawler.bootstrap(keys)

