#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbCollage import JsbCollage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行运营审核')
class TestOperaInspect:

    @allure.title('运营集采信息审核流程')
    def test_opera_examine(self, drivers):
        log.info('当前执行   集采信息审核    ')
        serve = '24'
        opera_phone = '13600136001'
        opera = JsbCollage(drivers)
        limit = 10
        inspect_type = 1  # 1通过 2 驳回
        reject_reason = ""
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        opera.opera_collage_inspect(serve, opera_phone, inspect_type, reject_reason, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_opera_inspect.py'])
