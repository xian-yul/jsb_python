#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}
log = Log()


class TestUserPlaceOrder:

    def test_place_order(self, drivers):
        log.info('当前执行   买家下单    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user_phone = "13700000000"
        org_name = "兴得铭"
        shop_num = 1
        delivery_type = 1
        pickup_type = 1
        address_name = ""
        sign_type = 2
        billing_type = 0
        limit = 3
        serve = '20'
        seller_phone = "18965691361"
        user = JsbPackagingMethod(drivers)
        user.place_order_repeatedly(user_phone, org_name, shop_num, delivery_type, pickup_type, address_name,
                                    sign_type,
                                    billing_type, limit, seller_phone, serve)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_place_order.py'])
