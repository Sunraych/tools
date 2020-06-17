# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 4:12 下午
# @Author  : SunRuichuan
# @File    : make_qrcode.py

import qrcode
from PIL import Image


def create_qrcode(content, filename):
    qr = qrcode.QRCode(
        version=1,
        # 设置容错率为最高
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image()
    # 设置二维码为彩色
    img = img.convert("RGBA")
    icon = Image.open('res/logo.png')
    w, h = img.size
    factor = 4
    size_w = int(w / factor)
    size_h = int(h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((w - icon_w) / 2)
    h = int((h - icon_h) / 2)
    icon = icon.convert("RGBA")
    newimg = Image.new("RGBA", (icon_w + 8, icon_h + 8), (255, 255, 255))
    img.paste(newimg, (w - 4, h - 4), newimg)

    img.paste(icon, (w, h), icon)
    img.save(filename + '.png', quality=100)


if __name__ == '__main__':
    create_qrcode("https://www.wandougongzhu.cn", "baidu")


