#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbUserRegister import JsbUserRegister
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestUserRegister:

    @allure.feature('买家注册账号')
    def test_register(self, drivers):
        log.info('当前执行   买家注册账号    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        limit = 5
        serve = '24'
        register = JsbUserRegister(drivers)
        register.user_register(serve, limit)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_register.py'])
