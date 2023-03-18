#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbUserConsignmentLetter import JsbUserConsignmentLetter
from utils.log import Log

from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家填写配送委托书')
class TestUserConsignmentLetter:
    test_data = [
        {
            'serve': '24',  # 环境
            'sellerPhone': '18929867679',  # 卖家账号
            'userPhone': '',  # 买家账号
            'limit': 1,  # 循环次数
        },
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家配送委托书')
    def test_user_consignment_letter(self, drivers, param):
        log.info('当前执行   买家填写配送委托书    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        serve = param['serve']
        seller_phone = param['sellerPhone']
        user_phone = param['userPhone']
        limit = param['limit']
        signEntrust = JsbUserConsignmentLetter(drivers)
        signEntrust.user_sign_entrust(serve, seller_phone, user_phone, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))
