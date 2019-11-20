# 聚合API

import json
from datetime import datetime   # 时间包
import requests                 # 请求包

appkey = 'xxxxxxxxxxxxxxxxx'     # 申请到的appkey
juhe_url = 'http://v.juhe.cn/'  # 聚合数据的网址


def calendar_day(date=datetime.now()):
    """
    获得日信息
    :param date:
    :return:
    """
    url = juhe_url + 'calendar/day'
    params = {
        # 'date': date.strftime('%Y-%m-%d'),
        'date': '{}-{}-{}'.format(date.year, date.month, date.day),
        'key':  appkey
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:     # 请求成功
        # return response.content         # 返回结果
        # return json.loads(response.content)
        return response.json()
    else:
        return None                     # 请求失败



