#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-27
# @description --
import json
import logging

from db.models import Company
from tianyancha import *
from urllib.parse import quote
from util.httpclient import Request


class TycClient:
    def __init__(self, payload=None):
        self.payload = payload
        self.src = []
        self.companies = []

    def search(self, keyword: str):
        """
        根据关键字搜索相关企业信息
        :param keyword: 关键字
        :return:
        """
        if not self.payload:
            self.payload = {
                "pageNum": 1,
                "pageSize": 20,
                "sortType": 0
            }
        url = TycSearchApi.format(q=quote(keyword))
        data = Request(url, self.payload, headers=REQUEST_HEADERS, proxy=True).data
        if data:
            api_data = json.loads(data)
            if api_data.get("state") == 'ok':
                self.src.append(api_data.get("data", {}).get("companyList", []))
                self.__post_process__()
            else:
                logging.info("查询异常：[%s]" % api_data)
        return self

    def __post_process__(self):
        """"""
        if not self.src:
            return

        todos = self.src
        for t in todos:
            detail = Request(TycEntApi.format(eid=t.get("id")), proxy=True).data
            if not detail:
                continue
            detail = json.loads(detail)
            if detail.get("state") == 'ok':
                td = detail.get("data", {})
                company = Company()
                # 复制主体信息
                TycClient.TycEntHelper.__copy_props__(t, company)
                # 复制公司组织代码、注册资本
                TycClient.TycEntHelper.__copy_extras__(td, company)
                self.companies.append(company)

    class TycEntHelper:
        @staticmethod
        def __copy_props__(src: dict, target: Company):
            target.name = src.get('name', '-').replace('<em>', '').replace('</em>', '')
            target.representative = src.get('legalPersonName', '-')
            target.address = src.get('regLocation', '-')
            target.region = src.get('base', '-')
            target.city = src.get('city', '-')
            target.district = src.get('district', '-')
            target.biz_status = src.get('regStatus', '-')
            target.credit_code = src.get('creditCode', '-')
            target.email = src.get('emails', ['-']).split(';')[0].replace('\t', '')
            target.phone = src.get('phoneNum', '-')
            target.biz_scope = src.get('businessScope', '-')
            target.company_type = src.get('companyOrgType', '-').replace('\t', '')
            target.taxpayer_code = src.get('creditCode', '-')
            target.registered_capital = src.get('regCapital', '-')
            target.lat_long = str({
                'lat': src.get('latitude', '-'),
                'long': src.get('longitude', '-')
            })
            target.setup_time = src.get('estiblishTime', '-')[0:10]

        @staticmethod
        def __copy_extras__(src: dict, company: Company):
            company.homepage = src.get('websiteList', '-')
            company.register_code = src.get('regNumber', '-')
            company.organization_code = src.get('orgNumber', '-')
            company.english_name = src.get('property3', '-')
            company.authorization = src.get('regInstitute', '-')
            company.actual_capital = src.get('actualCapital', '缺省')
            company.industry = src.get('industry', '-')
            company.used_name = src.get('historyNames', '-')

