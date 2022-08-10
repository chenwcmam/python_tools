# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:18
__author__ = "ChenWC"

import random
import string


def rand_string(length=32):
    """
    生成20位随机字符串
    """
    chars = string.ascii_letters + string.digits + '_-@'
    return ''.join(random.choice(chars) for _ in range(length))