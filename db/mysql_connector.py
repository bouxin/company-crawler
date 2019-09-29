#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""

from DBUtils.PooledDB import PooledDB
from config.env import MysqlEnviron
from db.model.model import Company
import logging as log
import pymysql


connection_pool = PooledDB(creator=pymysql,
                           maxconnections=20,
                           host=MysqlEnviron.host(),
                           port=MysqlEnviron.port(),
                           db=MysqlEnviron.database(),
                           user=MysqlEnviron.username(),
                           passwd=MysqlEnviron.password())


def insert(data: dict):
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'insert into company(`name`,`representative`,`address`,`region`,`city`,`district`,' \
          '`lat_long`,`biz_status`,`credit_code`,`register_code`,`phone`,`email`,`setup_time`,' \
          '`industry`, `biz_scope`,`company_type`,`registered_capital`,`actual_capital`,' \
          '`taxpayer_code`, `organization_code`,`english_name`,`authorization`,`homepage`,' \
          '`used_name`,`create_at`, `modify_at`, `search_key`) ' \
          'values(%(name)s,%(representative)s,%(address)s,%(region)s,%(city)s,%(district)s,' \
          '%(lat_long)s,%(biz_status)s,%(credit_code)s,%(register_code)s,%(phone)s,%(email)s,' \
          '%(setup_time)s, %(industry)s,%(biz_scope)s,%(company_type)s,%(registered_capital)s,' \
          '%(actual_capital)s, %(taxpayer_code)s,%(organization_code)s,%(english_name)s,' \
          '%(authorization)s,%(homepage)s, %(used_name)s,now(),now(), %(keyword)s) ' \
          'on duplicate key update `name`=%(name)s,`representative`=%(representative)s,' \
          '`address`=%(address)s,`region`=%(region)s,`lat_long`=%(lat_long)s,' \
          '`biz_status`=%(biz_status)s,`credit_code`=%(credit_code)s,' \
          '`register_code`=%(register_code)s,`phone`=%(phone)s,`email`=%(email)s,' \
          '`setup_time`=%(setup_time)s,`industry`=%(industry)s,`biz_scope`=%(biz_scope)s,' \
          '`company_type`=%(company_type)s,`registered_capital`=%(registered_capital)s,' \
          '`actual_capital`=%(actual_capital)s,`taxpayer_code`=%(taxpayer_code)s,' \
          '`organization_code`=%(organization_code)s,`english_name`=%(english_name)s,' \
          '`authorization`=%(authorization)s,`homepage`=%(homepage)s,`used_name`=%(used_name)s,' \
          '`modify_at`=now()'
    return write_tx(sql, data)


def write_tx(sql: str, data: any):
    """ 写事务 """
    connection = connection_pool.connection()
    cursor = connection.cursor()
    result = cursor.execute(sql, data)

    try:
        connection.commit()
    except RuntimeError as error:
        connection.rollback()
        log.error('事务提交失败！已回滚')
        raise error

    return result

