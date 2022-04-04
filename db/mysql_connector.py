#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""


from dbutils.pooled_db import PooledDB
from config import MysqlEnviron
import logging as log
import pymysql


connection_pool = PooledDB(creator=pymysql,
                           maxconnections=20,
                           host=MysqlEnviron.host,
                           port=MysqlEnviron.port,
                           db=MysqlEnviron.database,
                           user=MysqlEnviron.username,
                           passwd=MysqlEnviron.password)


def insert_company(data: list):
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'insert into `company`(`name`,`representative`,`address`,`region`,`city`,`district`,' \
          '`geoloc`,`biz_status`,`credit_code`,`register_code`,`phone`,`email`,`setup_time`,' \
          '`industry`, `biz_scope`,`company_type`,`registered_capital`,`actual_capital`,' \
          '`taxpayer_code`, `organization_code`,`english_name`,`authorization`,`homepage`,' \
          '`used_name`,`create_at`, `modify_at`, `search_key`) ' \
          'values(%(name)s,%(representative)s,%(address)s,%(region)s,%(city)s,%(district)s,' \
          '%(geoloc)s,%(biz_status)s,%(credit_code)s,%(register_code)s,%(phone)s,%(email)s,' \
          '%(setup_time)s, %(industry)s,%(biz_scope)s,%(company_type)s,%(registered_capital)s,' \
          '%(actual_capital)s, %(taxpayer_code)s,%(organization_code)s,%(english_name)s,' \
          '%(authorization)s,%(homepage)s, %(used_name)s,now(),now(), %(keyword)s) ' \
          'on duplicate key update `name`=%(name)s,`representative`=%(representative)s,' \
          '`address`=%(address)s,`region`=%(region)s,`geoloc`=%(geoloc)s,' \
          '`biz_status`=%(biz_status)s,`credit_code`=%(credit_code)s,' \
          '`register_code`=%(register_code)s,`phone`=%(phone)s,`email`=%(email)s,' \
          '`setup_time`=%(setup_time)s,`industry`=%(industry)s,`biz_scope`=%(biz_scope)s,' \
          '`company_type`=%(company_type)s,`registered_capital`=%(registered_capital)s,' \
          '`actual_capital`=%(actual_capital)s,`taxpayer_code`=%(taxpayer_code)s,' \
          '`organization_code`=%(organization_code)s,`english_name`=%(english_name)s,' \
          '`authorization`=%(authorization)s,`homepage`=%(homepage)s,`used_name`=%(used_name)s,' \
          '`modify_at`=now()'
    for company in data:
        managers = company.managers
        shareholders = company.shareholders
        write(sql, company)
        insert_company_manager(managers)
        insert_company_shareholder(shareholders)


def insert_company_shareholder(data: list):
    sql = 'insert into `dim_shareholder`(`credit_code`, `name`, `alias`, `avatar`, `control_ratio`, `tags`) ' \
          'values (%(credit_code)s, %s(name)s, %(alias)s, %(avatar)s, %(control_ratio)s, %(tags)s) ' \
          'on duplicate key update `name`=%(name)s, `alias`=%(alias)s, `avatar`=%(avatar)s, ' \
          '`control_ratio`=%(control_ratio)s, `tags`=%(tags)s'
    for shareholder in data:
        return write(sql, shareholder)


def insert_company_manager(data: list):
    sql = 'insert into `dim_company_manager`(`credit_code`, `name`, `titles`, `manager_type`) ' \
          'values (%(credit_code)s, %(name)s, %(titles)s, %(manager_type)s)' \
          'on duplicate key update `name`=%(name)s, `titles`=%(titles)s, `manager_type`=%(manager_type)s'
    for manager in data:
        return write(sql, manager)


def write(sql: str, data: any):
    connection = connection_pool.connection()
    cursor = connection.cursor()
    result = cursor.execute(sql, data)

    try:
        connection.commit()
    except RuntimeError as error:
        connection.rollback()
        log.error('Insertion Error!')
        raise error

    return result

