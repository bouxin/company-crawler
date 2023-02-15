#!/usr/bin/env python
# coding: utf-8

import logging

from uplink import *

AUTHORIZATION = '0###oo34J0VKzLlpdvf8kgFkMlfU_IPY###1642087379312###22494f3155c2e5a4be76e503837fa439'
""" 请求token """
X_AUTH_TOKEN = "eyJkaXN0aW5jdF9pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4xNS4yNCJ9LCJwcm9wZXJ0aWVzIjp7IiR0aW1lem9uZV9vZmZzZXQiOi00ODAsIiRzY3JlZW5faGVpZ2h0IjoxMDgwLCIkc2NyZWVuX3dpZHRoIjoxOTIwLCIkbGliIjoianMiLCIkbGliX3ZlcnNpb24iOiIxLjE1LjI0IiwiJGxhdGVzdF90cmFmZmljX3NvdXJjZV90eXBlIjoi6Ieq54S25pCc57Si5rWB6YePIiwiJGxhdGVzdF9zZWFyY2hfa2V5d29yZCI6IuacquWPluWIsOWAvCIsIiRsYXRlc3RfcmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImN1cnJlbnRfdXJsIjoiaHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2tleT0lRTYlOUQlQUQlRTUlQjclOUUlRTYlOTklQUUlRTUlODUlQjQlRTQlQkMlODElRTQlQjglOUElRTclQUUlQTElRTclOTAlODYlRTUlOTAlODglRTQlQkMlOTklRTQlQkMlODElRTQlQjglOUEiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnRpYW55YW5jaGEuY29tL3NlYXJjaD9rZXk9JUU2JTlEJUFEJUU1JUI3JTlFJUU2JTk5JUFFJUU1JTg1JUI0JUU0JUJDJTgxJUU0JUI4JTlBJUU3JUFFJUExJUU3JTkwJTg2JUU1JTkwJTg4JUU0JUJDJTk5JUU0JUJDJTgxJUU0JUI4JTlBIiwidHljaWQiOiI0MmMxZTY1MDQ0ZjYxMWVjYmIxZDY3ZmJiYzEwN2U3NSIsIm5hbWUiOiLmna3lt57mma7lhbTkvIHkuJrnrqHnkIblkIjkvJnkvIHkuJoiLCJtb2R1bGUiOiLkvJjotKjlrp7lkI3orqTor4EiLCIkaXNfZmlyc3RfZGF5IjpmYWxzZX0sImFub255bW91c19pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJ0eXBlIjoidHJhY2siLCJldmVudCI6InNlYXJjaF9yZXN1bHRfZXhwdXJlIiwiX3RyYWNrX2lkIjo3MjUyNDM3Mjd9"


def _response_handler(resp):
    """
    API接口响应参数处理器
    :return:
    """
    pass


def _error_handler(exc_type, exc_val, exc_tb):
    """
    API错误响应处理器
    :return:
    """
    logging.info('type: ' + exc_type)
    logging.info('val: ' + exc_val)
    logging.info('tb: ' + exc_tb)


@error_handler(_error_handler)
@response_handler(_response_handler)
@headers({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "version": "TYC-XCX-WX",
    "Host": "api9.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN,
})
class TianyanchaBasicInfo(Consumer):
    """
    企业基本数据
    """
    def __init__(self, base_url="", client=None, converters=(), auth=None, hooks=(), **kwargs):
        if not base_url:
            base_url = "https://api9.tianyancha.com"
        super().__init__(base_url, client, converters, auth, hooks, **kwargs)

    @returns.json
    @get("/services/v3/search/sNorV3/{q}")
    def list_by_page(self, keyword: Path("q"), page_num: Query("pageNum"), page_size: Query("pageSize"), sort_type: Query("sortType")):
        """
        根据关键字查询企业信息分页列表
        :param keyword:
        :param page_num:
        :param page_size:
        :param sort_type:
        :return:
        """

    @returns.json
    @get("/services/v3/t/common/baseinfoV5/{enterpriseId}")
    def get_enterprise_detail(self, enterprise_id: Path("enterpriseId")):
        """
        查询企业信息详情
        :param enterprise_id:
        :return:
        """

    @returns.json
    @get("/services/v3/risk/companyRiskInfoV4")
    def get_enterprise_business_risk(self, enterprise_id: Query("id")):
        """
        查询企业经营风险信息
        :param enterprise_id:
        :return:
        """


@error_handler(_error_handler)
@response_handler(_response_handler)
@headers({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "version": "TYC-XCX-WX",
    "Host": "capi.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN,
})
class TianyanchaDimensional(Consumer):
    """
    企业维度数据
    """
    def __init__(self, base_url="", client=None, converters=(), auth=None, hooks=(), **kwargs):
        if not base_url:
            base_url = "https://capi.tianyancha.com"
        super().__init__(base_url, client, converters, auth, hooks, **kwargs)

    def get_enterprise_shareholder_list(self, enterprise_id, page_num, page_size):
        """
        查询企业股东信息
        :param enterprise_id:
        :param page_size:
        :param page_num:
        :return:
        """
        body = {
            "graphId": enterprise_id,
            "hkVersion": 1,
            "typeList": {
                "shareHolder": {
                    "pageNum": page_num,
                    "pageSize": page_size,
                    "required": "true"
                }
            }
        }
        return self.__get_enterprise_shareholder_list(body)

    def get_enterprise_manager_list(self, enterprise_id, page_num, page_size):
        """
        查询企业高管信息
        :param enterprise_id:
        :param page_num:
        :param page_size:
        :return:
        """
        req_body = {
            "graphId": enterprise_id,
            "hkVersion": 1,
            "typeList": {
                "companyStaff": {
                    "pageNum": page_num,
                    "pageSize": page_size,
                    "required": "true"
                }
            }
        }
        return self.__get_enterprise_manager_list(req_body)

    @returns.json
    @post("/cloud-facade/company/familyBucket")
    def __get_enterprise_shareholder_list(self, **request_body: Body):
        """
        查询企业股东信息
        :param request_body:
        :return:
        """

    @returns.json
    @post("/cloud-facade/company/familyBucket")
    def __get_enterprise_manager_list(self, **request_body: Body):
        """
        查询企业高管
        :param request_body:
        :return:
        """
