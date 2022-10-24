#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import pytest

from page_object.JsbOperationPage import JsbOperationPage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestOperaExamine:

    def test_opera_examine(self, drivers):
        log.info('当前执行   运营原料审核    ')
        serve = '24'
       # opera_phone = '13600136001' # 20
        opera_phone = '17346709425' # 24
        opera = JsbOperationPage(drivers)
        limit = 10
        code = 1
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        opera.opera_goods_examine(serve,opera_phone,code,limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_opera_examine.py'])
