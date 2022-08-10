# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:17
__author__ = "ChenWC"

import socket


def port_test(ip, port):
    """
    判断ip和端口是否可达
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, int(port)))
    if result == 0:
        s.close()
        print('Port connect success!')
        return True
    else:
        print('Port connect failed!')
        return False
