#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbUserProductOrder import JsbUserProductOrder
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行买家制成品下单')
class TestUserPlaceProductOrder:
    test_data = [
        {
            'user_phone': '13500135003',  # 买家账号
            'product_name': 'QQQQQ',  # 搜索商品名称
            'shop_num': 10,  # 购买数量
            'cart_type': 0,  # 加入购物车  1加入 0加入
            'limit': 1,  # 循环次数
            'serve': '24',  # 环境
            'sign_type': 0,  # 签署类型  1个人签署  0默认企业
            'seller_phone': '17346709428',  # 卖家账号
            'address': '制成品下单测试地址',  # 发货地址
        },
        {
            'user_phone': '13500135003',
            'product_name': '重申',
            'shop_num': 10,
            'cart_type': 0,
            'limit': 1,
            'serve': '24',
            'sign_type': 0,
            'seller_phone': '17346709428',
            'address': '制成品下单测试地址',
        }
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('买家制成品下单流程')
    def test_place_product_order(self, drivers, param):
        log.info('当前执行   买家制成品下单    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        # user_phone = "13500135003"
        # product_name = "QQQQQ"  # 重申
        # shop_num = 10
        # cart_type = 0
        # limit = 1
        # serve = '24'
        # sign_type = 0
        # seller_phone = "17346709428"
        # address = '制成品下单测试地址'
        user_phone = param['user_phone']
        product_name = param['product_name']
        shop_num = param['shop_num']
        cart_type = param['cart_type']
        limit = param['limit']
        serve = param['serve']
        sign_type = param['sign_type']
        seller_phone = param['seller_phone']
        address = param['address']
        user = JsbUserProductOrder(drivers)
        user.place_product_order(serve, user_phone, seller_phone, product_name, shop_num, cart_type, address, sign_type,
                                 limit)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("开始时间: " + current_time)
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_place_product_order.py'])
