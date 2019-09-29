#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-29
# @description --
from db.model.model import Company


class TianyanchaManager(object):
    @classmethod
    def assembly(cls, company: Company, raw_company: dict):
        company.name = raw_company.get('name', '-').replace('<em>', '').replace('</em>', '')
        company.representative = raw_company.get('legalPersonName', '-')
        company.address = raw_company.get('regLocation', '-')
        company.region = raw_company.get('base', '-')
        company.city = raw_company.get('city', '-')
        company.district = raw_company.get('district', '-')
        company.biz_status = raw_company.get('regStatus', '-')
        company.credit_code = raw_company.get('creditCode', '-')
        company.email = raw_company.get('emails', ['-']).split(';')[0].replace('\t', '')
        company.phone = raw_company.get('phoneNum', '-')
        company.biz_scope = raw_company.get('businessScope', '-')
        company.company_type = raw_company.get('companyOrgType', '-').replace('\t', '')
        company.taxpayer_code = raw_company.get('creditCode', '-')
        company.registered_capital = raw_company.get('regCapital', '-')
        company.lat_long = str({
            'lat': raw_company.get('latitude', '-'),
            'long': raw_company.get('longitude', '-')
        })
        company.setup_time = raw_company.get('estiblishTime', '-')[0:10]

    @classmethod
    def assembly_detail(cls, company: Company, raw_company_detail: dict):
        company.homepage = raw_company_detail.get('websiteList', '-')
        company.register_code = raw_company_detail.get('regNumber', '-')
        company.organization_code = raw_company_detail.get('orgNumber', '-')
        company.english_name = raw_company_detail.get('property3', '-')
        company.authorization = raw_company_detail.get('regInstitute', '-')
        company.actual_capital = raw_company_detail.get('actualCapital', '缺省')
        company.industry = raw_company_detail.get('industry', '-')
        company.used_name = raw_company_detail.get('historyNames', '-')

