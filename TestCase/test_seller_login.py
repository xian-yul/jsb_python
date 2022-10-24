#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestSellerLogin:

    def test_seller_number_login(self, drivers):
        log.info('当前执行   卖家端登录    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        number = 'AN00000028'
        password = '123456'
        serve = '24'
        jsb = JsbPackagingMethod(drivers)
        jsb.seller_number_login(serve, number, password)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_login.py'])
