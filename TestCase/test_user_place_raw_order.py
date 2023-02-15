#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbUserRawOrder import JsbUserRawOrder
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家原料下单')
class TestUserPlaceRawOrder:

    @allure.title('买家原料下单流程')
    def test_place_raw_order(self, drivers):
        log.info('当前执行   买家原料下单    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user_phone = "13328798899"  # 13328798899  13500511551
        # user_phone = "13700000000"
        org_name = "丹山"
        # org_name = "兴得铭"
        shop_num = 1
        pickup_type = 4  # 1自提  2配送款到发货 3配送定金 4自提定金
        address_name = ""
        sign_type = 2
        billing_type = 0
        limit = 1
        serve = '24'
        seller_phone = "18929867679"
        # seller_phone = "18965691361"
        seller_address = '卖家详细地址'
        deposit = 5
        multiple_type = 0  # 0 多发  1 一次性
        multiple_order = 3
        hide_type = 1
        user = JsbUserRawOrder(drivers)
        user.place_raw_order(serve, user_phone, org_name, pickup_type, shop_num, address_name,
                             sign_type, billing_type, seller_phone, limit, seller_address, multiple_type, deposit,
                             multiple_order, hide_type)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_place_raw_order.py'])
