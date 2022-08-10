# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:16
__author__ = "ChenWC"

import base64
import hashlib


def sha256encode(rand_string):
    # sha256加密，加密方法为：用户名+随机字符串+秘钥拼成的字符串，求sha256值，再取前40位
    sha256 = hashlib.sha256(rand_string.encode('utf-8')).hexdigest()
    return sha256


def md5encode(raw_data):
    # 根据输入字符串生成MD5值
    a = hashlib.md5()
    a.update(raw_data.encode())
    b = a.hexdigest()
    return b[0:16]


def base64decode(text):
    # 对base64数据进行解码
    result = base64.b64decode(text)
    return result