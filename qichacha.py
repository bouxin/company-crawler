#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-16
:desc:
"""
from qichacha import crawler as QccCrawler

app = QccCrawler

if __name__ == '__main__':
    keys = ['Google中国']
    app.load_keys(keys)
    app.start()

