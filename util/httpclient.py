#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 02/28/2019
:desc: http请求工具类
"""
from venv import logger

import requests


def get(url, params, **kwargs):
    """
    get请求，更多入参查看requests.api
    :param url:
    :param params:
    :param kwargs:
    :return:
    """
    response = {}
    try:
        response = requests.get(url=url, params=params, **kwargs)
    except ConnectionError as error:
        logger.error('HttpGet请求发生错误，%s' % error)
        response.setdefault('reason', 'connection exception!')
        response.setdefault('code', 500)
    return response


def post(url, body, **kwargs):
    """
    post请求，更多入参查看requests.api
    :param url:
    :param body:
    :param kwargs:
    :return:
    """
    response = {}
    try:
        response = requests.post(url=url, json=body, **kwargs)
    except ConnectionError as error:
        logger.error('HttpGet请求发生错误，%s' % error)
        response.setdefault('reason', 'connection exception!')
        response.setdefault('code', 500)
    return response
