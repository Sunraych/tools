# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 2:29 下午
# @Author  : SunRuichuan
# @File    : get_ip.py

import socket


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        _ip = s.getsockname()[0]
    finally:
        s.close()
    return _ip


if __name__ == '__main__':
    ip = get_host_ip()
    print(ip)
