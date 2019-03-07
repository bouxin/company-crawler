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
    try:
        response = requests.get(url=url, params=params, **kwargs)
    except ConnectionError as error:
        logger.error('HttpGet网络请求错误，%s' % error)
        raise error
    return response


def post(url, body, **kwargs):
    """
    post请求，更多入参查看requests.api
    :param url:
    :param body:
    :param kwargs:
    :return:
    """
    try:
        response = requests.post(url=url, json=body, **kwargs)
    except ConnectionError as error:
        logger.error('HttpGet网络请求错误，%s' % error)
        raise error
    return response
