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


class TestSellerStorehouse:

    def test_seller_storehouse(self, drivers):
        log.info('当前执行   卖家端添加仓库地址    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        seller = JsbPackagingMethod(drivers)
        serve = '24'
        limit = 1
        seller_phone = '13500135000'
        storehouse_contact = '测试仓库说明'
        storehouse_address = '测试仓库默认地址'
        storehouse_name = '测试仓库地址'
        storehouse_phone = '13600136000'
        default = 0
        seller.seller_storehouse(serve, seller_phone, storehouse_name, storehouse_address, storehouse_contact,
                                 storehouse_phone, default, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_storehouse_coupon.py'])
