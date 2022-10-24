#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log

log = Log()
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestUserLogin:

    def test_user_login_001(self, drivers):
        log.info('当前执行   买家端登录    ')

        user = JsbPackagingMethod(drivers)
        serve = '24'
        user_phone = '13500135000'
        user.user_login(serve, user_phone)


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_login.py'])
