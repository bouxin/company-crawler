#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-11
:desc:
"""
import datetime


def datetime2timestamp(pytime: datetime.datetime.now()):
    ts = pytime.timestamp() * 1000
    return int(ts)


def timestamp2datetime(timestamp: int):
    date = datetime.datetime.fromtimestamp(timestamp / 1000)
    return date





