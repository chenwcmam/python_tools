# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:15
__author__ = "ChenWC"

import os


def read_cookies(cookie_file=None):
    # 根据文件名读取cookies，默认读取当前路径下的cookies.txt文件
    if not cookie_file:
        cookie_file = os.path.join(os.getcwd(), 'cookies.txt')
    if os.path.exists(cookie_file):
        with open(cookie_file, 'r') as f:
            cookies_from_file = f.read()
        return cookies_from_file
    return False