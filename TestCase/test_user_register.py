#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbUserRegister import JsbUserRegister
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家注册账号')
class TestUserRegister:
    test_data = [
        {
            'phone': '18930402314',
            'name': '测试122223456'
        },
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家注册账号流程')
    def test_register(self, drivers,param):
        log.info('当前执行   买家注册账号    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        limit = 1
        serve = '20'
        register = JsbUserRegister(drivers)
        phone = param['phone']
        name = param['name']
        register.user_register(serve, limit, phone, name)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_register.py'])
