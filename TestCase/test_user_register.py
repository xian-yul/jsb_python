#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbUserPage import JsbUserPage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestUserRegister:

    def test_user_register(self, drivers):
        log.info('当前执行   用户注册    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user = JsbUserPage(drivers)
        serve = '24'
        limit = 5
        user.user_register(serve, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_register.py'])
