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


class TestSellerClassification:

    def test_seller_classification(self, drivers):
        log.info('当前执行   卖家端创建商品分类    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        seller = JsbPackagingMethod(drivers)
        serve = '24'
        limit = 1
        seller_phone = '13500135000'
        type_name = '商品分类1'
        classification_type = 1
        state = 1
        father_type = 1
        seller.seller_goods_classification_add(serve, seller_phone, type_name, classification_type, state, father_type,
                                               limit
                                               )
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_goods_classification.py'])
