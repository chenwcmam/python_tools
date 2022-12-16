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


def time_num_to_string(number, format_string='%Y-%m-%d %H:%M:%S'):
    """
    将数字格式的时间戳转换为字符串格式, 默认为
    :param number:
    :param format_string:
    :return:
    """
    return datetime.fromtimestamp(number).strftime(format_string)


def current_time_str(format_string='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(format_string)