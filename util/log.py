#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""
import logging


logging.basicConfig(filename='../crawler.log', format='')  # todo


def warn(msg: str):
    logging.warning(msg)


def info(msg: str):
    logging.info(msg)


def error(msg: str):
    logging.error(msg)


def debug(msg: str):
    logging.debug(msg)

