#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import sys
sys.path.append('..')

TycSearchApi = "https://api9.tianyancha.com/services/v3/search/sNorV3/{q}"
TycEntApi = "https://api9.tianyancha.com/services/v3/t/common/baseinfoV5/{eid}"

""" 请求验证头 """
AUTHORIZATION = '0###oo34J0WVDdeu_k1O-sWPxFpg9WJ4###1555940540033###028a568b0150721d810d5f4417e03650'
""" 请求token """
X_AUTH_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3NTg5MjA3NSIsImlhdCI6MTU1NTk0MDU3MiwiZXhwIjoxNTU4NTMyNTcyfQ.lCJNDWQK0gD3fp9ieIlnMEzwmi00zkBqyHShdvHnspFzZQmgPHhHJAUY7mVbKY_AFk2Xhk82jMP99Q6a0wlmEQ"
""" 天眼查头信息 """
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "version": "TYC-XCX-WX",
    "Host": "api3.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN,
}



