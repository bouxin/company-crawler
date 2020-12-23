#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 02/28/2019
:desc: http请求工具类
"""
import logging
import requests


class Request:
    def __init__(self, url, params=None, proxy=False, headers=None, **kwargs):
        self.proxy = proxy
        self.url = url
        self.params = params
        self.data = None
        self.get(headers, **kwargs)

    def get(self, headers, **kwargs):
        resp = requests.get(self.url, params=self.params, headers=headers, verify=False, **kwargs)
        if resp and resp.status_code == 200:
            self.data = resp.text
        else:
            logging.warning(resp.json())


def proxy():
    import json
    from config.settings import PROXY_POOL_URL

    p = Request(f"{PROXY_POOL_URL}/get").data
    if p:
        p = json.loads(p)
        return {"http": "http://%s" % p.get("proxy")}


if __name__ == '__main__':
    print(proxy())


