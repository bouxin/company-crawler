#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
 todo 详情api/数据抽取
:author: lubosson
:date: 2019-04-15
:desc:
"""
import logging as log
from json import JSONDecodeError
from time import sleep
from util import httpclient
from db import mysql_connector as mydb

""" 关键字搜索API """
QCC_SEARCH_API = "https://xcx.qichacha.com/wxa/v1/base/advancedSearchNew"
""" 企业详情API """
QCC_SEARCH_DETAIL_API = "https://xcx.qichacha.com/wxa/v1/base/getEntDetail"
""" 地区代码列表 """
QCC_AREA_API = "https://xcx.qichacha.com/wxa/v1/admin/getAreaList"
""" web浏览器no-login COOKIE """
COOKIE = "zg_did=%7B%22did%22%3A%20%22168dbc0b22f6e5-0d361e70cfef92-10306653-13c680-168dbc0b23013bd%22%7D; _uab_collina=154987506595105102560196; acw_tc=78c7474915498750659746725e47bcf5da5e01750eaa818d83d5019d1f; saveFpTip=true; UM_distinctid=168e101305e193-0665042ea0cf1-133b6850-13c680-168e101305f37d; CNZZDATA1254842228=1871928231-1549959491-https%253A%252F%252Fwww.qichacha.com%252F%7C1549959491; QCCSESSID=780j6eils4m98fspmr9cvtc9p5; hasShow=1; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201551756182960%2C%22updated%22%3A%201551756803803%2C%22info%22%3A%201551242110203%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22fc6fca91d248e7cf976bd652db7e11c6%22%7D"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
""" 伪装请求头，更多参数抓包qcc小程序 """
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Cookie": COOKIE
}
"""
授权企查查小程序返回TOKEN 过期时间1h 
"""
TOKEN = "9a62aaad7cda6c73a35d598f93e8d169"


def start():
    keywords = globals().get('keywords')
    if not keywords:
        log.info('no available keywords')
        return

    for keyword in keywords:
        log.info('开始搜索关键字[%s]' % keyword)
        apiret = QccSearchApi.search(keyword)
        log.info('开始解析')
        QccDataBuilder.build4save(apiret)
        log.info('数据已保存')
    log.info('success')


def load_keys(keys: list):
    globals().setdefault('keywords', keys)


class QccSearchApi:
    @staticmethod
    def search(keyword: str):
        if not keyword:
            return None

        payload = {
            "searchKey": keyword,
            "token": TOKEN,
            "pageIndex": 1,  # 每个关键字默认获取第一页数据共20条
            "searchType": 0,
            "isSortAsc": False
        }
        httpret = httpclient.get(url=QCC_SEARCH_API, params=payload, headers=REQUEST_HEADERS)
        sleep(2)

        message, code = httpret.reason, httpret.status_code

        if code != 200:
            log.warning('http error, %s-%s' % (code, message))
            return None

        try:
            apiret = httpret.json()
        except JSONDecodeError:
            log.error('解析httpret失败')
            return None

        return apiret.get('result')

    @staticmethod
    def search_detail(key_no):
        if not key_no:
            log.info('company id null')
            return None
        payload = {
            "token": TOKEN,
            "unique": key_no
        }

        httpresult = httpclient.get(url=QCC_SEARCH_DETAIL_API, params=payload, headers=REQUEST_HEADERS)
        sleep(2)

        message, code = httpresult.reason, httpresult.status_code

        if code != 200:
            log.warning('http error, %s-%s' % (code, message))
            return None

        try:
            apiret = httpresult.json()
        except JSONDecodeError:
            log.error('解析httpret失败')
            return None

        return apiret.get('result')


class QccDataBuilder:
    @classmethod
    def build4save(cls, res: dict):
        if not res:
            log.info('no res available')
            return

        target = dict()
        results = res.get('Result')
        for src in results:
            target = cls.copy_properties(src, target)
            log.info(target)
            # mydb.insert(target)
            sleep(0.5)
            target.clear()

    @classmethod
    def copy_properties(cls, source: dict, target: dict) -> dict:
        target['name'] = cls.get_company_name(source)
        target['representative'] = cls.get_representative(source)
        target['address'] = cls.get_address(source)
        target['region'] = cls.get_region(source)
        target['city'] = cls.get_city(source)
        target['district'] = cls.get_district(source)
        target['biz_status'] = cls.get_biz_status(source)
        target['credit_code'] = cls.get_credit_code(source)
        target['email'] = cls.get_email(source)
        target['phone'] = cls.get_work_phone(source)
        target['biz_scope'] = cls.get_biz_scope(source)
        target['company_type'] = cls.get_company_type(source)
        target['taxpayer_code'] = cls.get_taxpayer_code(source)
        target['registered_capital'] = cls.get_registered_capital(source)
        target['lat_long'] = cls.get_lat_long(source)
        target['setup_time'] = cls.get_setup_time(source)

        company_key_no = source.get('KeyNo')
        detail = QccSearchApi.search_detail(company_key_no)
        if detail:
            detail = detail.get('Company')
        target['homepage'] = cls.get_homepage(detail)
        target['register_code'] = cls.get_register_code(detail)
        target['organization_code'] = cls.get_organization_code(detail)
        target['english_name'] = cls.get_company_english(detail)
        target['authorization'] = cls.get_register_organization(detail)
        target['actual_capital'] = cls.get_real_capital(detail)
        target['industry'] = cls.get_industry(detail)
        target['used_name'] = cls.get_company_used_name(detail)

        return target

    @classmethod
    def get_company_name(cls, source):
        name = source.get("Name")
        return name.replace('<em>', '').replace('</em>', '').strip() if name else '-'

    @classmethod
    def get_representative(cls, source):
        representative = source.get('OperName')
        if representative:
            return representative.replace('<em>', '').replace('</em>', '').strip()
        else:
            return '-'

    @classmethod
    def get_address(cls, source):
        address = source.get('Address')
        return address.strip() if address else '-'

    @classmethod
    def get_region(cls, source):
        # todo
        # region_short_code = source.get('Province')
        # region = distinct.get(region_short_code)
        # return region if region else '-'
        pass

    @classmethod
    def get_city(cls, source):
        # todo
        pass

    @classmethod
    def get_district(cls, source):
        # todo
        pass

    @classmethod
    def get_biz_status(cls, source):
        company_status = source.get('Status')
        return company_status if company_status else '-'

    @classmethod
    def get_credit_code(cls, source):
        credit_code = source.get('CreditCode')
        return credit_code if credit_code else '-'

    @classmethod
    def get_email(cls, source):
        email = source.get('Email')
        return email.strip() if email else '-'

    @classmethod
    def get_work_phone(cls, source):
        phone = source.get('ContactNumber')
        if phone:
            return phone.replace('\t', '').replace('\r', '').strip()
        else:
            return '-'

    @classmethod
    def get_biz_scope(cls, source):
        scope = source.get('Scope')
        if scope:
            return scope.replace('<em>', '').replace('</em>', '').strip()
        else:
            return '-'

    @classmethod
    def get_company_type(cls, source):
        company_type = source.get('EconKind')
        if company_type:
            return company_type.strip()
        else:
            return '-'

    @classmethod
    def get_taxpayer_code(cls, source):
        """ 三码合一 """
        taxpayer_code = source.get('CreditCode')
        return taxpayer_code if taxpayer_code else '-'

    @classmethod
    def get_registered_capital(cls, source):
        registered_capi = source.get('RegistCapi')
        return registered_capi if registered_capi else '-'

    @classmethod
    def get_lat_long(cls, source):
        lat = source.get('X')
        long = source.get('Y')
        location = {
            'lat': lat if lat else '-',
            'long': long if long else '-'
        }
        return str(location)

    @classmethod
    def get_setup_time(cls, source):
        setup_time = source.get('StartDate')
        return setup_time if setup_time else '-'

    @classmethod
    def get_homepage(cls, source):
        if not source:
            return '-'
        homepage = source.get('WebSite')
        return homepage[0:30] if homepage else '-'

    @classmethod
    def get_register_code(cls, source):
        register_code = source.get('No')
        return register_code if register_code else '-'

    @classmethod
    def get_organization_code(cls, source):
        org_code = source.get('OrgNo')
        return org_code if org_code else '-'

    @classmethod
    def get_company_english(cls, source):
        engname = source.get('EnglishName')
        return engname if engname else '-'

    @classmethod
    def get_register_organization(cls, source):
        regi_org = source.get('BelongOrg')
        return regi_org if regi_org else '-'

    @classmethod
    def get_real_capital(cls, source):
        # todo
        pass

    @classmethod
    def get_industry(cls, source):
        pass

    @classmethod
    def get_company_used_name(cls, detail):
        pass










