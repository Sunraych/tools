# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 4:10 下午
# @Author  : SunRuichuan
# @File    : md5.py

import hashlib


def md5(source):
    m2 = hashlib.md5()
    m2.update(source.encode('utf-8'))
    return m2.hexdigest()


if __name__ == '__main__':
    a = md5("abc")
    print(a)

