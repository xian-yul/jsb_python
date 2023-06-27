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
    test_data = [
        {
            'user_phone': '13500135002',  # 买家账号
            'org_name': '丹山',  # 购买企业
            'shop_num': 1,  # 购买数量
            'pickup_type': 4,  # 下单类型 1自提  2配送款到发货 3配送定金 4自提定金
            'address_name': '',  # 收货地址
            'sign_type': 0,  # 1 个人 或  0 企业签署
            'billing_type': 0,  # 开票
            'limit': 2,  # 循环次数
            'serve': '24',  # 环境
            'seller_phone': '18929867679',  # 卖家账号
            'seller_address': '卖家详细地址',  # 卖家发货详细地址
            'deposit': 5,  # 定金比例
            'multiple_type': 1,  # 提货方式 0多发 1一次性
            'multiple_order': 3,  # 多发单数
            'hide_type': 1,  # 是否隐藏收货地址  1隐藏 0不隐藏
            'send_type': 0,  # 是否签署发货委托书  1是 0不
            'pay_type': 0,  # 是否提前支付 1是 0不
        }
        # {
        #     'user_phone': '13500135002',  # 买家账号
        #     'org_name': '丹山',  # 购买企业
        #     'shop_num': 1,  # 购买数量
        #     'pickup_type': 2,  # 下单类型 1自提  2配送款到发货 3配送定金 4自提定金
        #     'address_name': '',  # 收货地址
        #     'sign_type': 0,  # 1 个人 或  0 企业签署
        #     'billing_type': 0,  # 开票
        #     'limit': 1,  # 循环次数
        #     'serve': '24',  # 环境
        #     'seller_phone': '18929867679',  # 卖家账号
        #     'seller_address': '卖家详细地址',  # 卖家发货详细地址
        #     'deposit': 5,  # 定金比例
        #     'multiple_type': 1,  # 提货方式 0多发 1一次性
        #     'multiple_order': 3,  # 多发单数
        #     'hide_type': 1,  # 是否隐藏收货地址  1隐藏 0不隐藏
        #     'send_type': 0,  # 是否签署发货委托书  1是 0不
        #     'pay_type': 0,  # 是否提前支付 1是 0不
        # },
        # {
        #     'user_phone': '13500135002',  # 买家账号
        #     'org_name': '丹山',  # 购买企业
        #     'shop_num': 1,  # 购买数量
        #     'pickup_type': 2,  # 下单类型 1自提  2配送款到发货 3配送定金 4自提定金
        #     'address_name': '',  # 收货地址
        #     'sign_type': 0,  # 1 个人 或  0 企业签署
        #     'billing_type': 0,  # 开票
        #     'limit': 1,  # 循环次数
        #     'serve': '24',  # 环境
        #     'seller_phone': '18929867679',  # 卖家账号
        #     'seller_address': '卖家详细地址',  # 卖家发货详细地址
        #     'deposit': 5,  # 定金比例
        #     'multiple_type': 1,  # 提货方式 0多发 1一次性
        #     'multiple_order': 3,  # 多发单数
        #     'hide_type': 1,  # 是否隐藏收货地址  1隐藏 0不隐藏
        #     'send_type': 0,  # 是否签署发货委托书  1是 0不
        #     'pay_type': 0,  # 是否提前支付 1是 0不
        # },
        # {
        #     'user_phone': '13500135002',  # 买家账号
        #     'org_name': '丹山',  # 购买企业
        #     'shop_num': 1,  # 购买数量
        #     'pickup_type': 3,  # 下单类型 1自提  2配送款到发货 3配送定金 4自提定金
        #     'address_name': '',  # 收货地址
        #     'sign_type': 0,  # 1 个人 或  0 企业签署
        #     'billing_type': 0,  # 开票
        #     'limit': 1,  # 循环次数
        #     'serve': '24',  # 环境
        #     'seller_phone': '18929867679',  # 卖家账号
        #     'seller_address': '卖家详细地址',  # 卖家发货详细地址
        #     'deposit': 5,  # 定金比例
        #     'multiple_type': 1,  # 提货方式 0多发 1一次性
        #     'multiple_order': 3,  # 多发单数
        #     'hide_type': 1,  # 是否隐藏收货地址  1隐藏 0不隐藏
        #     'send_type': 0,  # 是否签署发货委托书  1是 0不
        #     'pay_type': 0,  # 是否提前支付 1是 0不
        # },
        # {
        #     'user_phone': '13500135002',  # 买家账号
        #     'org_name': '丹山',  # 购买企业
        #     'shop_num': 1,  # 购买数量
        #     'pickup_type': 4,  # 下单类型 1自提  2配送款到发货 3配送定金 4自提定金
        #     'address_name': '',  # 收货地址
        #     'sign_type': 0,  # 1 个人 或  0 企业签署
        #     'billing_type': 0,  # 开票
        #     'limit': 1,  # 循环次数
        #     'serve': '24',  # 环境
        #     'seller_phone': '18929867679',  # 卖家账号
        #     'seller_address': '卖家详细地址',  # 卖家发货详细地址
        #     'deposit': 5,  # 定金比例
        #     'multiple_type': 1,  # 提货方式 0多发 1一次性
        #     'multiple_order': 3,  # 多发单数
        #     'hide_type': 1,  # 是否隐藏收货地址  1隐藏 0不隐藏
        #     'send_type': 0,  # 是否签署发货委托书  1是 0不
        #     'pay_type': 0,  # 是否提前支付 1是 0不
        # },
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家原料下单流程')
    def test_place_raw_order(self, drivers, param):
        log.info('当前执行   买家原料下单    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        user_phone = param['user_phone']
        seller_phone = param['seller_phone']
        org_name = param['org_name']
        shop_num = param['shop_num']
        pickup_type = param['pickup_type']
        address_name = param['address_name']
        sign_type = param['sign_type']
        billing_type = param['billing_type']
        seller_address = param['seller_address']
        deposit = param['deposit']
        multiple_type = param['multiple_type']
        multiple_order = param['multiple_order']
        hide_type = param['hide_type']
        serve = param['serve']
        limit = param['limit']
        send_type = param['send_type']
        pay_type = param['pay_type']
        user = JsbUserRawOrder(drivers)
        user.place_raw_order(serve, user_phone, org_name, pickup_type, shop_num, address_name,
                             sign_type, billing_type, seller_phone, limit, seller_address, multiple_type, deposit,
                             multiple_order, hide_type, send_type, pay_type)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_place_raw_order.py'])
