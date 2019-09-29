#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2019-09-27
# @description --


class Company(object):
    def __init__(self):
        self.id = None
        self.name = '-'
        self.representative = '-'
        self.address = '-'
        self.region = '-'
        self.city = '-'
        self.district = '-'
        self.biz_status = '-'
        self.credit_code = '-'
        self.email = '-'
        self.phone = '-'
        self.biz_scope = '-'
        self.company_type = '-'
        self.taxpayer_code = '-'
        self.registered_capital = '-'
        self.lat_long = '-'
        self.setup_time = '-'
        self.homepage = '-'
        self.register_code = '-'
        self.organization_code = '-'
        self.english_name = '-'
        self.authorization = '-'
        self.actual_capital = '-'
        self.industry = '-'
        self.used_name = '-'
        self.keyword = '-'

    def __str__(self) -> str:
        return "{}, {}".format(self.name, self.representative)

    def clear(self):
        self.__init__()


class Province(object):
    def __init__(self):
        self.id = None
        self.code = 000000
        self.name = '全国'
        self.short = 'CN'


class City(object):
    def __init__(self):
        self.id = None
        self.parent = 000000
        self.code = 000000
        self.name = '市区'

