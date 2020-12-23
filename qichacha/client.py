#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-27
# @description --
import json
from time import sleep
from qichacha import *
from util.httpclient import Request


class QichachaClient:
    @staticmethod
    def search(keyword: str) -> list:
        results = []
        if keyword:
            payload = {
                "searchKey": keyword,
                "token": TOKEN,
                "pageIndex": 1,  # 每个关键字默认获取第一页数据共20条
                "searchType": 0,
                "isSortAsc": False
            }
            data = Request(SEARCH_API, params=payload, headers=REQUEST_HEADERS).data
            sleep(2)
            if data:
                data = json.loads(data)
                if data.get('status') == 200:
                    results.append(data.get('result', {}).get('Result', []))
        return results

    @staticmethod
    def search_detail(key_no):
        detail = dict()
        if key_no:
            payload = {
                "token": TOKEN,
                "unique": key_no
            }
            data = Request(url=COMPANY_DETAIL_API, params=payload, headers=REQUEST_HEADERS).data
            sleep(2)

            if data:
                data = json.loads(data)
                if data.get('status') == 200:
                    detail = data.json().get('result', {}).get('Company', {})
        return detail


