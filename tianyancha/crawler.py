#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import time
import urllib3
from urllib import parse as url_encoder
from util import httpclient, log
from db import mysql_connector
urllib3.disable_warnings()

""" 天眼查搜索API """
SEARCH_API = 'https://api9.tianyancha.com/services/v3/search/sNorV3'
""" 企业详情API """
DETAIL_API = 'https://api9.tianyancha.com/services/v3/t/common/baseinfoV5'
""" 请求验证头 """
AUTHORIZATION = '0###oo34J0ePGhOIwh35OjSfJ0jGr71Y###1552015848536###bee60ad62826a4195ef55af25a1db2f5'
""" ua """
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
""" 请求token """
X_AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODEwMDE3NzI5NSIsImlhdCI6MTU1MTk1MDQ0MCwiZXhwIjoxNTU0NTQyNDQwfQ.364iry9elpPFO8eyoq9F0oEQGy7BydPCGu0nTHjpgLswO3yhl6xQYu22daUw_ZFpuBv_qg_KjBHH45vVU68OcA"
""" 天眼查头信息 """
REQUEST_HEADERS = {
    "User-Agent": UA,
    "version": "TYC-XCX-WX",
    "Host": "api3.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN
}


def bootstrap():
    """ 入口函数 """
    keys = ['Google']  # todo 查询字段设置
    for key in keys:
        log.info('开始搜索关键字[%s]' % key)
        companies = TycSearchApi.search(key)
        log.info('开始解析')
        TycDataBuilder.build_info4save(companies)
        log.info('数据已保存')
    log.info('结束')


class TycSearchApi:
    @staticmethod
    def search(key: str):
        """
        根据关键字搜索相关企业信息
        :param key: 关键字
        :return:
        """
        payload = {
            "pageNum": 1,
            "pageSize": 20,
            "sortType": 0
        }
        url = SEARCH_API + "/" + url_encoder.quote(key)
        http_result = httpclient.get(url=url, params=payload, headers=REQUEST_HEADERS, verify=False)
        time.sleep(2)

        ok, message, code = http_result.ok, http_result.reason, http_result.status_code
        if not ok or code != 200:
            log.error('%s-%s-%s' %
                      (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), code, message))
        try:
            api_result = http_result.json()  # api响应数据
        except RuntimeError as error:
            log.error('unboxing error, error: %s' % error)
            return None

        api_message, api_state = api_result.get('message'), api_result.get('state')
        if api_state != 'ok':
            log.error('[tyc]api error, %s-%s' % (api_state, api_message))
            return None

        companies = api_result.get('data').get('companyList')   # 搜索公司结果json array
        return companies

    @staticmethod
    def search_detail(company_id: int):
        url = DETAIL_API + "/" + str(company_id)
        http_result = httpclient.get(url=url, params=None, headers=REQUEST_HEADERS, verify=False)
        time.sleep(2)

        ok, message, code = http_result.ok, http_result.reason, http_result.status_code
        if not ok or code != 200:
            log.error('%s-%s-%s' %
                      (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), code, message))
        try:
            api_result = http_result.json()  # api响应数据
        except RuntimeError as error:
            log.error('unboxing error, error: %s' % error)
            return None

        api_message, api_state = api_result.get('message'), api_result.get('state')
        if api_state != 'ok':
            log.error('[tyc]api error, %s-%s' % (api_state, api_message))
            return None

        company_detail = api_result.get('data')
        return company_detail


class TycDataBuilder:
    @classmethod
    def build_info4save(cls, companies: list):
        """
        解析api数据，解析一条保存一条，尽可能降低性能缓解被爬服务器压力
        @ps 优化点
        :param companies:
        :return: 目标对象列表
        """
        if not companies:
            log.info('no companies available')
            return

        enterprise = dict()
        for corp in companies:
            enterprise = cls.produce(corp, enterprise)
            mysql_connector.insert(enterprise)
            time.sleep(0.5)
            enterprise.clear()

    @classmethod
    def produce(cls, corp: dict, enterprise: dict):
        """ 构建存储对象 """
        enterprise['name'] = cls.get_company_name(corp)
        enterprise['representative'] = cls.get_representative(corp)
        enterprise['address'] = cls.get_address(corp)
        enterprise['region'] = cls.get_region(corp)
        enterprise['city'] = cls.get_city(corp)
        enterprise['district'] = cls.get_district(corp)
        enterprise['biz_status'] = cls.get_biz_status(corp)
        enterprise['credit_code'] = cls.get_credit_code(corp)
        enterprise['email'] = cls.get_email(corp)
        enterprise['phone'] = cls.get_work_phone(corp)
        enterprise['biz_scope'] = cls.get_biz_scope(corp)
        enterprise['company_type'] = cls.get_company_type(corp)
        enterprise['taxpayer_code'] = cls.get_taxpayer_code(corp)
        enterprise['registered_capital'] = cls.get_registered_capital(corp)
        enterprise['lat_long'] = cls.get_lat_long(corp)
        enterprise['setup_time'] = cls.get_setup_time(corp)

        company_id = corp.get('id')
        detail = TycSearchApi.search_detail(company_id)
        enterprise['homepage'] = cls.get_homepage(detail)
        enterprise['register_code'] = cls.get_register_code(detail)
        enterprise['organization_code'] = cls.get_organization_code(detail)
        enterprise['english_name'] = cls.get_company_english(detail)
        enterprise['authorization'] = cls.get_register_organization(detail)
        enterprise['actual_capital'] = cls.get_real_capital(detail)
        enterprise['industry'] = cls.get_industry(detail)
        enterprise['used_name'] = cls.get_company_used_name(detail)

        return enterprise

    @classmethod
    def get_company_name(cls, company: dict) -> str:
        name = company.get('name')
        if not name:
            return '-'
        name = name.replace('<em>', '').replace('</em>', '')
        return name.strip() if name else '-'

    @classmethod
    def get_representative(cls, company: dict) -> str:
        representative = company.get('legalPersonName')
        if not representative:
            return '-'
        representative = representative.replace('<em>', '').replace('</em>', '')
        return representative.strip() if representative else '-'

    @classmethod
    def get_region(cls, company: dict) -> str:
        region = company.get('base')
        return region.strip() if region else '-'

    @classmethod
    def get_city(cls, company: dict) -> str:
        city = company.get('city')
        return city.strip() if city else '-'

    @classmethod
    def get_district(cls, company: dict) -> str:
        district = company.get('district')
        return district.strip() if district else '-'

    @classmethod
    def get_email(cls, company: dict) -> str:
        emails = company.get('emails')
        if not emails:
            return '-'
        email = emails.split(';')[0]
        email = email.replace('\t', '')
        return email.strip() if email else '-'

    @classmethod
    def get_work_phone(cls, company: dict) -> str:
        phone = company.get('phoneNum')
        return phone.strip() if phone else '-'

    @classmethod
    def get_address(cls, company: dict) -> str:
        address = company.get('regLocation')
        return address.strip() if address else '-'

    @classmethod
    def get_biz_status(cls, company: dict) -> str:
        status = company.get('regStatus')
        return status.strip() if status else '-'

    @classmethod
    def get_credit_code(cls, company: dict) -> str:
        credit_code = company.get('creditCode')
        return credit_code.strip() if credit_code else '-'

    @classmethod
    def get_register_code(cls, company: dict) -> str:
        if not company:
            return '-'
        reg_code = company.get('regNumber')
        return reg_code.strip() if reg_code else '-'

    @classmethod
    def get_biz_scope(cls, company: dict) -> str:
        biz_scope = company.get('businessScope')
        return biz_scope.strip() if biz_scope else '-'

    @classmethod
    def get_company_type(cls, company: dict) -> str:
        company_type = company.get('companyOrgType')
        return company_type.replace('\t', '').strip() if company_type else '-'

    @classmethod
    def get_taxpayer_code(cls, company: dict) -> str:
        credit_code = company.get('creditCode')
        return credit_code.strip() if credit_code else '-'

    @classmethod
    def get_organization_code(cls, company: dict) -> str:
        if not company:
            return '-'
        org_code = company.get('orgNumber')
        return org_code.strip() if org_code else '-'

    @classmethod
    def get_company_english(cls, company: dict) -> str:
        if not company:
            return '-'
        english_name = company.get('property3')
        return english_name.strip() if english_name else '-'

    @classmethod
    def get_register_organization(cls, company: dict) -> str:
        if not company:
            return '-'
        reg_organ = company.get('regInstitute')
        return reg_organ.strip() if reg_organ else '-'

    @classmethod
    def get_registered_capital(cls, company: dict) -> str:
        reg_capital = company.get('regCapital')
        return reg_capital.strip() if reg_capital else '-'

    @classmethod
    def get_homepage(cls, company: dict) -> str:
        if not company:
            return '-'
        homepage = company.get('websiteList')
        return homepage.strip() if homepage else '-'

    @classmethod
    def get_real_capital(cls, company: dict) -> str:
        if not company:
            return '-'
        actual_capital = company.get('actualCapital')
        return actual_capital.strip() if actual_capital else '-'

    @classmethod
    def get_industry(cls, company: dict) -> str:
        if not company:
            return '-'
        industry = company.get('industry')
        return industry.strip() if industry else '-'

    @classmethod
    def get_company_used_name(cls, company: dict) -> str:
        if not company:
            return '-'
        used_name = company.get('historyNames')
        return used_name if used_name else '-'

    @classmethod
    def get_setup_time(cls, company: dict) -> str:
        setup_time = company.get('estiblishTime')
        if not setup_time:
            return '-'
        setup_time = setup_time[0:10]
        return setup_time if setup_time else '-'

    @classmethod
    def get_lat_long(cls, company: dict) -> str:
        lat = company.get('latitude')
        long = company.get('longitude')
        temp = {
            'lat': lat if lat else '-',
            'long': long if long else '-'
        }
        return str(temp)




