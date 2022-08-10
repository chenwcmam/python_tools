# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:11
__author__ = "ChenWC"

import datetime


def datetime_format_validate(date_text, date_format):
    """
    判断字符串是否符合格式('%Y-%m-%d %H:%M:%S')，符合的话返回日期时间
    返回日期格式为datetime.datetime
    """
    try:
        return datetime.datetime.strptime(date_text, date_format)
    except ValueError:
        return False


def date_format_validate(date_text, date_format):
    """
    判断字符串是否符合格式('%Y-%m-%d')，符合的话返回日期
    返回日期格式为datetime.date
    """
    try:
        return datetime.datetime.strptime(date_text, date_format).date()
    except ValueError:
        return False
