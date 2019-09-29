#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-27
# @description --
from db.model.model import Company


class QichachaManager(object):
    @classmethod
    def assembly(cls, company: Company, raw_company: dict):
        company.name = raw_company.get('Name', '-')
        company.representative = raw_company.get('OperName', '-')
        company.address = raw_company.get('Address', '-')
        company.region = raw_company.get('AreaCode', '-')  # todo
        company.city = raw_company.get('AreaCode', '-')  # todo
        company.district = raw_company.get('AreaCode', '-')  # todo
        company.biz_status = raw_company.get('Status', '-')
        company.credit_code = raw_company.get('CreditCode', '-')
        company.email = raw_company.get('Email', '-')
        company.phone = raw_company.get('ContactNumber', '-')
        company.biz_scope = raw_company.get('Scope', '-')
        company.company_type = raw_company.get('EconKind', '-')
        company.taxpayer_code = raw_company.get('CreditCode', '-')
        company.registered_capital = raw_company.get('RegistCapi', '-')
        company.lat_long = str({
            'lat': raw_company.get('X', '-'),
            'long': raw_company.get('Y', '-')
        })
        company.setup_time = raw_company.get('StartDate', '-')

    @classmethod
    def assembly_detail(cls, company: Company, raw_company_detail: dict):
        company.homepage = raw_company_detail.get('WebSite', '-')[0:30]
        company.register_code = raw_company_detail.get('No', '-')
        company.organization_code = raw_company_detail.get('OrgNo', '-')
        company.english_name = raw_company_detail.get('EnglishName', '-')
        company.authorization = raw_company_detail.get('BelongOrg', '-')
        company.actual_capital = raw_company_detail.get('RealCapi', '缺省')
        company.industry = raw_company_detail.get('Industry', dict()).get('Industry', '-')
        company.used_name = raw_company_detail.get('OriginalName', '-')


