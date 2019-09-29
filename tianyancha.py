#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosin
:date: 03/28/2019
"""
from tianyancha import crawler as TycCrawler
from util import log
import urllib3
urllib3.disable_warnings()


log.set_file("tianyancha.log")
app = TycCrawler

if __name__ == '__main__':
    keys = ['西湖龙井']  # todo 查询字段设置
    app.load_keys(keys)
    app.start()


