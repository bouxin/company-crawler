#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import logging as log

from db.model.model import Company
from tianyancha.client import TianyanchaClient
from tianyancha.manager import TianyanchaManager
from db.mysql_connector import insert as save


# 天眼查客户端
tyc_client = TianyanchaClient()
manager = TianyanchaManager()


def start():
    """ 入口函数 """
    keys = globals().get('keywords', list())
    for key in keys:
        raw_companies = tyc_client.search(key)
        cost_time = 2 * raw_companies.__len__() + 4
        log.info('正在处理爬取[%s]，大概需要%s秒' % (key, cost_time))
        # company对象
        company = Company()
        for raw_company in raw_companies:
            company.keyword = key
            manager.assembly(company, raw_company)
            # company detail
            raw_company_detail = tyc_client.search_detail(raw_company.get('id'))
            manager.assembly_detail(company, raw_company_detail)
            # log.info(company)
            save(company.__dict__)
            company.clear()
    log.info("completed")


def load_keys(keys: list):
    globals().setdefault('keywords', keys)





