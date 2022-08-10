# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 10:21
__author__ = "ChenWC"

import os
import re
import platform


def check_and_create_folder(folder_path):
    # 判断路径是否存在，如不存在，则创建目录
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_system_type():
    # 获取当前操作系统类型Linux、Windows
    return platform.platform().split("-", 1)[0]  # 获取操作系统信息


def get_system_split():
    # 获取当前操作系统默认分隔符
    return os.sep


def get_father_path(folder_path):
    # 获取输入路径的父目录
    father_path_temp = folder_path.rsplit(os.sep, 1)[0]  # 根据当前系统分隔符对输入路径进行分割
    if re.match(r'.*:$', father_path_temp):
        print(f'-----father path {father_path_temp} ends with ":"')  # 若父目录以:结尾，说明已经到了磁盘根路径
        return father_path_temp + os.sep
    else:
        print(f'-----father path {father_path_temp} ends not with ":"')
        return father_path_temp
