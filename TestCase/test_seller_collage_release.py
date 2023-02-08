#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestSellerCollageRelease:

    def test_seller_collage_release(self, drivers):
        log.info('当前执行   卖家端发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_collage_release.py'])
