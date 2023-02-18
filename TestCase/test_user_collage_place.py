#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家集采下单')
class TestUserCollagePlace:
    test_data = [
        {

        }
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家集采下单流程')
    def test_user_collage_place(self, drivers,param):
        log.info('当前执行   买家购买集采    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_collage_place.py'])
