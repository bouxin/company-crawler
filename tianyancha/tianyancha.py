#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import time
import urllib3
from urllib import parse as url_encoder
from util import httpclient
from fake_useragent import UserAgent
from db import mysql_connector
urllib3.disable_warnings()

""" 天眼查搜索API """
SEARCH_API = 'https://api9.tianyancha.com/services/v3/search/sNorV3'
""" 企业详情API """
DETAIL_API = 'https://api9.tianyancha.com/services/v3/t/common/baseinfoV5'
""" 
请求验证头
"""
AUTHORIZATION = '0###oo34J0ePGhOIwh35OjSfJ0jGr71Y###1552015848536###bee60ad62826a4195ef55af25a1db2f5'
"""
请求token
"""
X_AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODEwMDE3NzI5NSIsImlhdCI6MTU1MTk1MDQ0MCwiZXhwIjoxNTU0NTQyNDQwfQ.364iry9elpPFO8eyoq9F0oEQGy7BydPCGu0nTHjpgLswO3yhl6xQYu22daUw_ZFpuBv_qg_KjBHH45vVU68OcA"
""" 天眼查头信息 """
REQUEST_HEADERS = {
    "User-Agent": UserAgent().random,
    "version": "TYC-XCX-WX",
    "Host": "api3.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN
}


def search_keyword(key: str):
    """
    根据关键字搜索相关企业信息
    :param key:
    :return:
    """
    payload = {
        "pageNum": 1,
        "pageSize": 20,
        "sortType": 0
    }
    url = SEARCH_API + "/" + url_encoder.quote(key)
    http_result = httpclient.get(url=url, params=payload, headers=REQUEST_HEADERS, verify=False)
    ok, message, code = http_result.ok, http_result.reason, http_result.status_code
    if ok and code == 200:
        try:
            api_result = http_result.json()  # api响应数据
        except:
            print('解析json数据异常')
            return None
        api_message, api_state = api_result.get('message'), api_result.get('state')
        if api_state == 'ok':
            companies = api_result.get('data').get('companyList')   # 搜索公司结果json array
            return companies
        print('[tyc]api error, %s-%s' % (api_state, api_message))
    print('%s-%s-%s', (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), code, message))


def build_info2db(companies: list):
    """
    解析api数据，解析一条保存一条，尽可能降低性能缓解被爬服务器压力
    :param companies:
    :return: 目标对象列表
    """
    if not companies:
        return
    enterprise = dict()
    for corp in companies:
        enterprise['name'] = get_company_name(corp)
        enterprise['representative'] = get_representative(corp)
        enterprise['address'] = get_address(corp)
        enterprise['region'] = get_region(corp)
        enterprise['city'] = get_city(corp)
        enterprise['district'] = get_district(corp)
        enterprise['biz_status'] = get_biz_status(corp)
        enterprise['credit_code'] = get_credit_code(corp)
        enterprise['email'] = get_email(corp)
        enterprise['phone'] = get_work_phone(corp)
        enterprise['biz_scope'] = get_biz_scope(corp)
        enterprise['company_type'] = get_company_type(corp)
        enterprise['taxpayer_code'] = get_taxpayer_code(corp)
        enterprise['registered_capital'] = get_registered_capital(corp)
        enterprise['setup_time'] = get_setup_time(corp)
        enterprise['lat_long'] = get_lat_long(corp)

        enterprise['homepage'] = get_website(corp)
        enterprise['register_code'] = get_register_code(corp)
        enterprise['organization_code'] = get_organization_code(corp)
        enterprise['english_name'] = get_company_english(corp)
        enterprise['authorization'] = get_register_organization(corp)
        enterprise['actual_capital'] = get_real_capital(corp)
        enterprise['industry'] = get_industry(corp)
        enterprise['used_name'] = get_company_used_name(corp)


def get_company_name(company: dict) -> str:
    name = company.get('name')
    if not name:
        return '-'
    name = name.replace('<em>', '').replace('</em>', '')
    return name.strip() if name else '-'


def get_representative(company: dict) -> str:
    representative = company.get('legalPersonName')
    if not representative:
        return '-'
    representative = representative.replace('<em>', '').replace('</em>', '')
    return representative.strip() if representative else '-'


def get_region(company: dict) -> str:
    pass


def get_city(company: dict) -> str:
    pass


def get_district(company: dict) -> str:
    pass


def get_email(company: dict) -> str:
    email = company.get('emails')
    if not email:
        return '-'
    email = email.split('\t')[0]
    return email.strip() if email else '-'


def get_work_phone(company: dict) -> str:
    phone = company.get('phoneNum')
    return phone.strip() if phone else '-'


def get_address(company: dict) -> str:
    address = company.get('regLocation')
    return address.strip() if address else '-'


def get_biz_status(company: dict) -> str:
    status = company.get('regStatus')
    return status.strip() if status else '-'


def get_credit_code(company: dict) -> str:
    credit_code = company.get('creditCode')
    return credit_code.strip() if credit_code else '-'


def get_register_code(company: dict) -> str:
    reg_code = company.get('regNumber')
    return reg_code.strip() if reg_code else '-'


def get_biz_scope(company: dict) -> str:
    biz_scope = company.get('businessScope')
    return biz_scope.strip() if biz_scope else '-'


def get_company_type(company: dict) -> str:
    company_type = company.get('companyOrgType')
    return company_type.strip() if company_type else '-'


def get_taxpayer_code(company: dict) -> str:
    credit_code = company.get('creditCode')
    return credit_code.strip() if credit_code else '-'


def get_organization_code(company: dict) -> str:
    org_code = company.get('orgNumber')
    return org_code.strip() if org_code else '-'


def get_company_english(company: dict) -> str:
    pass


def get_register_organization(company: dict) -> str:
    pass


def get_registered_capital(company: dict) -> str:
    pass


def get_website(company: dict) -> str:
    pass


def get_real_capital(company: dict) -> str:
    pass


def get_industry(company: dict) -> str:
    pass


def get_company_used_name(company: dict) -> str:
    pass


def get_short_desc(company: dict) -> str:
    pass


def get_setup_time(company: dict) -> str:
    setup_time = company.get('setupTime')
    setup_time = time.strftime('%Y-%m-%d', time.localtime(int(setup_time) / 1000))
    return setup_time


def get_lat_long(company: dict) -> str:
    pass


def get_province(company: dict) -> str:
    pass



