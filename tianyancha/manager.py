#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-29
# @description --
from db.model.model import Company


class TianyanchaManager(object):
    @classmethod
    def assembly(cls, company: Company, raw_company: dict):
        company.name = raw_company.get('name', '-')
        company.representative = raw_company.get('legalPersonName', '-')
        company.address = raw_company.get('regLocation', '-')  # todo
        company.region = raw_company.get('base', '-')
        company.city = raw_company.get('city', '-')
        company.district = raw_company.get('district', '-')
        company.biz_status = raw_company.get('regStatus', '-')
        company.credit_code = raw_company.get('creditCode', '-')
        company.email = raw_company.get('emails', ['-']).split(';')[0]
        company.phone = raw_company.get('phoneNum', '-')
        company.biz_scope = raw_company.get('businessScope', '-')
        company.company_type = raw_company.get('companyOrgType', '-')
        company.taxpayer_code = raw_company.get('creditCode', '-')
        company.registered_capital = raw_company.get('regCapital', '-')
        company.lat_long = {
            'lat': raw_company.get('latitude', '-'),
            'long': raw_company.get('longitude', '-')
        }
        company.setup_time = raw_company.get('estiblishTime', '-')

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


class TycDataBuilder:
    @classmethod
    def copy_properties(cls, source: dict, target: dict):
        """ 构建存储对象 """
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

        company_id = source.get('id')
        detail = TycSearchApi.search_detail(company_id)
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

