#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-27
# @description --
from urllib import parse as url_encoder
from const.constants import TIANYANCHA
from util import httpclient
from json import JSONDecodeError
import time
import logging as log

""" ua """
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
""" 请求验证头 """
AUTHORIZATION = '0###oo34J0WVDdeu_k1O-sWPxFpg9WJ4###1555940540033###028a568b0150721d810d5f4417e03650'
""" 请求token """
X_AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3NTg5MjA3NSIsImlhdCI6MTU1NTk0MDU3MiwiZXhwIjoxNTU4NTMyNTcyfQ.lCJNDWQK0gD3fp9ieIlnMEzwmi00zkBqyHShdvHnspFzZQmgPHhHJAUY7mVbKY_AFk2Xhk82jMP99Q6a0wlmEQ"
""" 天眼查头信息 """
REQUEST_HEADERS = {
    "User-Agent": UA,
    "version": "TYC-XCX-WX",
    "Host": "api3.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN
}


class TianyanchaClient(object):
    @classmethod
    def search(cls, keyword: str) -> list:
        """
        根据关键字搜索相关企业信息
        :param keyword: 关键字
        :return:
        """
        payload = {
            "pageNum": 1,
            "pageSize": 20,
            "sortType": 0
        }
        url = TIANYANCHA.SEARCH_API + "/" + url_encoder.quote(keyword)
        http_result = httpclient.get(url=url, params=payload, headers=REQUEST_HEADERS)
        time.sleep(2)
        if http_result.status_code == 200:
            try:
                api_result = http_result.json()  # api响应数据
                if api_result.get('state') == 'ok':
                    return api_result.get('data', dict()).get('companyList', list())
                else:
                    log.info(str(api_result))
            except JSONDecodeError as error:
                pass
        else:
            log.info(str(http_result.text))
        return list()

    @classmethod
    def search_detail(cls, company_id: int):
        """
        根据公司ID查询公司信息详情
        :param company_id:
        :return: 公司详情json结果
        """
        url = TIANYANCHA.DETAIL_API + "/" + str(company_id)
        http_result = httpclient.get(url=url, params=None, headers=REQUEST_HEADERS)
        time.sleep(2)
        if http_result.status_code == 200:
            try:
                api_result = http_result.json()  # api响应数据
                if api_result.get('state') == 'ok':
                    return api_result.get('data', dict())
                else:
                    log.info(str(api_result))
            except JSONDecodeError as error:
                pass
        else:
            log.info(str(http_result.text))
        return dict()
