#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-11
:desc:
"""
import logging as log
from config.settings import MysqlConfig


ENV = 'development'  # 环境变量


class MysqlEnviron:
    mapping = {
        'development': MysqlConfig.get('development'),
        'testing': MysqlConfig.get('testing'),
        'production': MysqlConfig.get('production')
    }

    CONFIG = mapping.get(ENV, 'development')

    if not CONFIG:
        log.error('no active environment')
        exit(0)

    @staticmethod
    def host():
        return MysqlEnviron.CONFIG.get('host')

    @staticmethod
    def port():
        return MysqlEnviron.CONFIG.get('port')

    @staticmethod
    def database():
        return MysqlEnviron.CONFIG.get('db')

    @staticmethod
    def username():
        return MysqlEnviron.CONFIG.get('username')

    @staticmethod
    def password():
        return MysqlEnviron.CONFIG.get('password')

