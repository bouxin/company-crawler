#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""
from util import log

ENV = 'development'  # 环境变量


class MysqlConfig:
    config = {
        'development': {
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'geek',
            'username': 'geek',
            'password': 'Geek@123...'
        }
    }
    
    mapping = {
        'development': config.get('development'),
        'testing': config.get('testing'),
        'production': config.get('production')
    }

    env = mapping.get(ENV if ENV else 'development')
    CONFIG = env if env else mapping.get('testing')

    if not CONFIG:
        log.error('no active environment')
        exit(0)

    @staticmethod
    def host():
        return MysqlConfig.CONFIG.get('host')

    @staticmethod
    def port():
        return MysqlConfig.CONFIG.get('port')

    @staticmethod
    def database():
        return MysqlConfig.CONFIG.get('db')

    @staticmethod
    def username():
        return MysqlConfig.CONFIG.get('username')

    @staticmethod
    def password():
        return MysqlConfig.CONFIG.get('password')

