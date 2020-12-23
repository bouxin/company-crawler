#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-15
:desc:
"""
import sys
sys.path.append('..')

""" 关键字搜索API """
SEARCH_API = "https://xcx.qichacha.com/wxa/v1/base/advancedSearchNew"
""" 企业详情API """
COMPANY_DETAIL_API = "https://xcx.qichacha.com/wxa/v1/base/getEntDetail"
""" 地区代码列表 """
AREA_API = "https://xcx.qichacha.com/wxa/v1/admin/getAreaList"
""" web浏览器no-login COOKIE """
COOKIE = "zg_did=%7B%22did%22%3A%20%22168dbc0b22f6e5-0d361e70cfef92-10306653-13c680-168dbc0b23013bd%22%7D; _uab_collina=154987506595105102560196; acw_tc=78c7474915498750659746725e47bcf5da5e01750eaa818d83d5019d1f; saveFpTip=true; UM_distinctid=168e101305e193-0665042ea0cf1-133b6850-13c680-168e101305f37d; CNZZDATA1254842228=1871928231-1549959491-https%253A%252F%252Fwww.qichacha.com%252F%7C1549959491; QCCSESSID=780j6eils4m98fspmr9cvtc9p5; hasShow=1; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201551756182960%2C%22updated%22%3A%201551756803803%2C%22info%22%3A%201551242110203%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22fc6fca91d248e7cf976bd652db7e11c6%22%7D"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
""" 伪装请求头，更多参数抓包qcc小程序 """
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Cookie": COOKIE
}
"""
授权企查查小程序返回TOKEN 过期时间1h, 自行更新 
可走代理方式模拟应用登陆获取该token
"""
TOKEN = "9a62aaad7cda6c73a35d598f93e8d169"

