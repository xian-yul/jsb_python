#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestSellerCoupon:

    def test_seller_coupon(self, drivers):
        log.info('当前执行   卖家端创建优惠劵    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        seller = JsbPackagingMethod(drivers)
        serve = '24'
        limit = 1
        seller_phone = '13500135000'
        coupon_name = '优惠劵 1'
        suit_type = 2
        targetRange_type = 1
        content = '优惠劵说明内容11'
        quota = 10
        coupon_type = 9
        seller.seller_coupon(serve, seller_phone, coupon_name,coupon_type, suit_type, targetRange_type, content, quota, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))

if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_coupon.py'])
