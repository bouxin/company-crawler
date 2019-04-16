#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosin
:date: 03/28/2019
"""
from tianyancha import crawler as TycCrawler

app = TycCrawler

if __name__ == '__main__':
    keys = ['Google中国']  # todo 查询字段设置
    app.load_keys(keys)
    app.start()


