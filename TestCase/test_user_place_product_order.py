#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from page_object.JsbUserPage import JsbUserPage
from page_object.JsbUserProductOrder import JsbUserProductOrder
from utils.log import Log
from utils.tool_util import time_lag


log = Log()


class TestUserPlaceProductOrder:

    def test_place_product_order(self, drivers):
        log.info('当前执行   买家制成品下单    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user_phone = "13500135003"
        product_name = "QQQQQ"
        shop_num = 10
        cart_type = 0
        limit = 5
        serve = '24'
        seller_phone = "17346709428"
        address = '制成品下单测试地址'
        user = JsbUserProductOrder(drivers)
        user.place_product_order(serve,user_phone,seller_phone,product_name, shop_num, cart_type,address,limit)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_place_product_order.py'])
