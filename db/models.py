#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author bouxin
# @since 2019-09-27
# @description --


class Company(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.short_name = None
        self.representative = None
        self.found_time = None
        self.company_address = None
        self.register_address = None
        self.province = None
        self.city = None
        self.district = None
        self.biz_status = None
        # lat-long:: eg. {'latitude': '12.0023', 'longitude': '120.180'}
        self.geoloc = None
        self.emails = None
        self.phones = None
        self.contact = None
        self.biz_scope = None
        self.company_type = None
        self.score = 50.00
        self.register_capital = None
        self.websites = None
        self.credit_code = None
        self.taxpayer_code = None
        self.register_code = None
        self.organization_code = None
        self.tags = None
        self.industry = None
        self.keyword = None
        self.logo = None
        self.company_desc = None
        self.financing_round = None
        self.competitions = None
        self.english_name = None
        self.register_institute = None
        self.actual_capital = None
        self.used_name = None
        self.staffs = 1
        self.tax_address = None
        self.taxpayer_bank = None
        self.portraits = None
        self.shareholders = []
        self.managers = []

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())


class CompanyShareholder(object):
    def __init__(self):
        self.name = None
        self.alias = None
        self.avatar = None
        self.control_ratio = None
        self.tags = []

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())


class CompanyManager(object):
    def __init__(self):
        self.name = None
        self.titles = []
        self.manager_type = None

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())


class Province(object):
    def __init__(self):
        self.id = None
        self.code = 000000
        self.name = '全国'
        self.simple = 'CN'

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())


class City(object):
    def __init__(self):
        self.id = None
        self.parent = 000000
        self.code = 000000
        self.name = '市区'

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())

