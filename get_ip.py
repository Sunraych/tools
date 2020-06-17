# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 2:29 下午
# @Author  : SunRuichuan
# @File    : get_ip.py

import socket
import requests
from lxml import etree


# 获取网卡ip
def get_inner_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        _ip = s.getsockname()[0]
    finally:
        s.close()
    return _ip


# 解析网页，正则判断，获取用户实际公网ip
def get_outer_ip():
    url = 'http://tool.chinaz.com/'
    res = requests.get(url=url)
    html = etree.HTML(res.text)
    _ip = html.xpath('/html/body/div[1]/div[5]/div[1]/a[2]')[0].text
    _ip = str(_ip).split("：")[1]
    return _ip


if __name__ == '__main__':
    ip1 = get_inner_ip()
    ip2 = get_outer_ip()
    print(ip1)
    print(ip2)
