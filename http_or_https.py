# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:15
__author__ = "ChenWC"

import os
import urllib.parse
from requests.utils import requote_uri
from file_or_path import get_parent_path, check_and_create_folder


def read_cookies(cookie_file=None):
    # 根据文件名读取cookies，默认读取当前路径下的cookies.txt文件
    if not cookie_file:
        cookie_file = os.path.join(os.getcwd(), 'cookies.txt')
    if os.path.exists(cookie_file):
        with open(cookie_file, 'r') as f:
            cookies_from_file = f.read()
        return cookies_from_file
    return False


def read_or_input_cookies(cookie_file=None):
    # 根据文件名读取cookies，默认读取当前路径下的cookies.txt文件

    if not cookie_file:
        cookie_file = os.path.join(os.getcwd(), 'cookies.txt')
    if os.path.exists(cookie_file):
        with open(cookie_file, 'r') as f:
            cookies_from_file = f.read()
        return cookies_from_file
    else:
        cookie_data = input('输入cookies或直接回车:')
        cookie_data = cookie_data.strip()
        if cookie_data:
            check_and_create_folder(get_parent_path(cookie_file))
            with open(cookie_file, 'w') as f:
                f.write(cookie_data)
                print(f'------cookies已保存至 {cookie_file} 文件')
        return cookie_data


class UrlEncoder:

    @staticmethod
    def total_url_encoder(url_to_encode, safe=''):
        """
        对完整url进行url编码，默认所有特殊字符都会被编码
        safe可以指定哪些字符不被编码，可以为字符串，例如':/?'
        'http://www.sample.com/?id=123 abc'会被编码为'http%3A%2F%2Fwww.sample.com%2F%3Fid%3D123%20abc'
        """
        return urllib.parse.quote(url_to_encode, safe=safe)

    @staticmethod
    def partial_url_encoder(url_to_encode):
        """
        对完整url进行url编码，仅对其中非url分割符的特殊字符进行编码
        'http://www.sample.com/?id=123 abc'会被编码为'https://www.sample.com/?id=123%20abc'
        """
        return requote_uri(url_to_encode)


if __name__ == '__main__':
    print(UrlEncoder.total_url_encoder('http://www.sample.com/?id=123 abc', safe=':/?'))
