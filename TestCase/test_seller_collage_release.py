#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbCollage import JsbCollage
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行卖家发布集采信息')
class TestSellerCollageRelease:
    test_data = [
        {
            'minimum': 10,
            'seller_phone': '',
            'serve': '24',
            'add_type': 1,  # 是否启用搜索牌号  1启用
            'circulation': 1,  # 智能搜索中 商品加载次数 50个为一次
            'addGoods': '原料',  # 添加类型 默认原料
            'goodsNumber': 7,  # 添加牌号下标
            'delivery_method': 1,  # 1配送 2自提
            'collage_num': 100,  # 集采量
            'overflow_num': 20,  # 溢出值
            'delivery_time': 20,  # 交货时间
            'delivery_price': 7905,  # 单价
            'deposit': 5,  # 定金
            'describe': '',  # 交易描述
            'limit': 1  # 循环次数
        }
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('卖家发布集采信息流程')
    def test_seller_collage_release(self, drivers, param):
        log.info('当前执行   卖家发布集采信息    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        collage = JsbCollage(drivers)
        minimum = param['minimum']
        seller_phone = param['seller_phone']
        serve = param['serve']
        add_type = param['add_type']
        circulation = param['circulation']
        addGoods = param['addGoods']
        goodsNumber = param['goodsNumber']
        delivery_method = param['delivery_method']
        collage_num = param['collage_num']
        overflow_num = param['overflow_num']
        delivery_time = param['delivery_time']
        delivery_price = param['delivery_price']
        deposit = param['deposit']
        describe = param['describe']
        limit = param['limit']
        log.info("开始时间: " + current_time)
        collage.seller_collage_release(serve, seller_phone, minimum, addGoods, add_type, circulation, goodsNumber,
                                       delivery_method, collage_num, overflow_num, delivery_time, delivery_price,
                                       deposit, describe)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_collage_release.py'])
