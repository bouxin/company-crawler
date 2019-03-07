#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""

from DBUtils.PooledDB import PooledDB
from util import log
from env.settings import MysqlConfig
import pymysql

connection_pool = PooledDB(creator=pymysql,
                           maxconnections=20,
                           host=MysqlConfig.host(),
                           port=MysqlConfig.port(),
                           db=MysqlConfig.database(),
                           username=MysqlConfig.username(),
                           passwd=MysqlConfig.password())


def tx_commit(sql: str, data: any):
    """
    事务方法
    :param sql:
    :param data:
    :return:
    """
    connection = connection_pool.connection()
    cursor = connection.cursor()
    result = cursor.execute(sql, data)
    try:
        connection.commit()
        return result
    except RuntimeError as error:
        connection.rollback()
        log.error('事务提交失败！已回滚')
        raise error


def insert(data: dict):
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'insert into enterprise(`name`, `representative`, `address`, `region`, `biz_status`,' \
          '`credit_code`, `register_code`, `phone`, `email`, `setup_time`, `industry`, `biz_scope`,' \
          '`company_type`, `registered_capital`, `paid_capital`, `taxpayer_code`, `organization_code`,' \
          '`english_name`, `authority`, `homepage`, `desc`, `used_name`, `insert_time`, `last_time`) ' \
          'values(%(name)s, %(representative)s, %(address)s, %(region)s, %(bizStatus)s, %(creditCode)s, ' \
          '%(registerCode)s, %(phone)s, %(email)s, %(setupTime)s, %(industry)s, %(bizScope)s, %(companyType)s, ' \
          '%(registeredCapital)s, %(paidCapital)s, %(taxpayerCode)s, %(organizationCode)s, %(englishName)s, ' \
          '%(authority)s, %(homepage)s, %(desc)s, %(usedName)s, %(insertTime)s, %(lastTime)s) ' \
          'on duplicate key update `name`=%(name)s, `representative`=%(representative)s, `address`=%(address)s,' \
          '`region`=%(region)s, `biz_status`=%(bizStatus)s, `credit_code`=%(creditCode)s, `register_code`=%(registerCode)s,' \
          '`phone`=%(phone)s, `email`=%(email)s, `setup_time`=%(setupTime)s, `industry`=%(industry)s,' \
          '`biz_scope`=%(bizScope)s, `company_type`=%(companyType)s, `registered_capital`=%(registeredCapital)s,' \
          '`paid_capital`=%(paidCapital)s, `taxpayer_code`=%(taxpayerCode)s, `organization_code`=%(organizationCode)s,' \
          '`english_name`=%(englishName)s, `authority`=%(authority)s, `homepage`=%(homepage)s, `desc`=%(desc)s,' \
          '`used_name`=%(usedName)s, `insert_time`=%(insertTime)s, `last_time`=%(lastTime)s'
    return tx_commit(sql, data)

