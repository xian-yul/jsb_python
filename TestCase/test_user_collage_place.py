#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbCollage import JsbCollage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家集采下单')
class TestUserCollagePlace:
    test_data = [
        {
            'user_phone': '',  # 买家账号
            'serve': '24',  # 环境
            'purchase_num': 10,  # 购买数量
            'purchase_goods': '',  # 购买商品名称
            'limit': 1,  # 循环次数
        }
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家集采下单流程')
    def test_user_collage_place(self, drivers, param):
        log.info('当前执行   买家购买集采    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        collage = JsbCollage(drivers)
        user_phone = param['user_phone']
        serve = param['serve']
        purchase_num = param['purchase_num']
        purchase_goods = param['purchase_goods']
        limit = param['limit']
        log.info("开始时间: " + current_time)
        collage.user_collage_place_order(serve,user_phone,purchase_num,purchase_goods,limit)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_collage_place.py'])
