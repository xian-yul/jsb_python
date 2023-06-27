#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbCloudFactory import JsbCloudFactory
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家发布询价订单')
class TestCloudInquiryOrder:

    @allure.title('买家发布询价订单')
    def test_user_release_inquiry_order(self, drivers):
        log.info('当前执行   发布询价订单    ')
        serve = '24'
        user_phone = '13500135000'
        opera = JsbCloudFactory(drivers)
        limit = 20
        product_name = '询价'
        cloud_num = 10
        cloud_duration = 10
        way = 0  # 1自提 0配送
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        opera.user_cloud_release_inquiry_order(serve, user_phone, product_name, cloud_duration, cloud_num, way, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_cloud_inquiry_order.py'])
