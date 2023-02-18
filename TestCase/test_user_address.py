#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbOperaInspectPage import JsbOperaInspect
from page_object.JsbUserAddress import JsbUserAddressPage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家添加收货地址')
class TestUserAddress:

    @allure.title('买家添加收货地址流程')
    def test_address_add(self, drivers):
        log.info('当前执行   买家地址添加   ')
        serve = '24'
        user_phone = '13500135001'
        address = JsbUserAddressPage(drivers)
        limit = 1
        default_type = 1
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        address.user_address_add(serve, user_phone, default_type, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))



if __name__ == '__main__':
    pytest.main(['TestCase/test_user_address.py'])
