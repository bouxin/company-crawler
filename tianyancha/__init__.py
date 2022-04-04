#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/08/2019
"""
import sys
sys.path.append('..')

TycQueryApi = "https://api9.tianyancha.com/services/v3/search/sNorV3/{q}"
TycPortraitApi = "https://api9.tianyancha.com/services/v3/t/common/baseinfoV5/{eid}"
TycShareholderPostApi = "https://capi.tianyancha.com/cloud-facade/company/familyBucket"
TycEnterpriseManagerPostApi = "https://capi.tianyancha.com/cloud-facade/company/familyBucket"
TycEnterpriseRiskApi = "https://api9.tianyancha.com/services/v3/risk/companyRiskInfoV4?{id}"

""" 请求验证头 """
AUTHORIZATION = '0###oo34J0VKzLlpdvf8kgFkMlfU_IPY###1642087379312###22494f3155c2e5a4be76e503837fa439'
""" 请求token """
X_AUTH_TOKEN = "eyJkaXN0aW5jdF9pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4xNS4yNCJ9LCJwcm9wZXJ0aWVzIjp7IiR0aW1lem9uZV9vZmZzZXQiOi00ODAsIiRzY3JlZW5faGVpZ2h0IjoxMDgwLCIkc2NyZWVuX3dpZHRoIjoxOTIwLCIkbGliIjoianMiLCIkbGliX3ZlcnNpb24iOiIxLjE1LjI0IiwiJGxhdGVzdF90cmFmZmljX3NvdXJjZV90eXBlIjoi6Ieq54S25pCc57Si5rWB6YePIiwiJGxhdGVzdF9zZWFyY2hfa2V5d29yZCI6IuacquWPluWIsOWAvCIsIiRsYXRlc3RfcmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImN1cnJlbnRfdXJsIjoiaHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2tleT0lRTYlOUQlQUQlRTUlQjclOUUlRTYlOTklQUUlRTUlODUlQjQlRTQlQkMlODElRTQlQjglOUElRTclQUUlQTElRTclOTAlODYlRTUlOTAlODglRTQlQkMlOTklRTQlQkMlODElRTQlQjglOUEiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnRpYW55YW5jaGEuY29tL3NlYXJjaD9rZXk9JUU2JTlEJUFEJUU1JUI3JTlFJUU2JTk5JUFFJUU1JTg1JUI0JUU0JUJDJTgxJUU0JUI4JTlBJUU3JUFFJUExJUU3JTkwJTg2JUU1JTkwJTg4JUU0JUJDJTk5JUU0JUJDJTgxJUU0JUI4JTlBIiwidHljaWQiOiI0MmMxZTY1MDQ0ZjYxMWVjYmIxZDY3ZmJiYzEwN2U3NSIsIm5hbWUiOiLmna3lt57mma7lhbTkvIHkuJrnrqHnkIblkIjkvJnkvIHkuJoiLCJtb2R1bGUiOiLkvJjotKjlrp7lkI3orqTor4EiLCIkaXNfZmlyc3RfZGF5IjpmYWxzZX0sImFub255bW91c19pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJ0eXBlIjoidHJhY2siLCJldmVudCI6InNlYXJjaF9yZXN1bHRfZXhwdXJlIiwiX3RyYWNrX2lkIjo3MjUyNDM3Mjd9"
""" 天眼查头信息 """
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "version": "TYC-XCX-WX",
    "Host": "api9.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN,
}



