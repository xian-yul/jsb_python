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
            'minimum': 1,  # 最低采购量
            # 'seller_phone': '18929867679',  # 卖家账号
            'seller_phone': '18965691361',  # 卖家账号
            'serve': '20',  # 环境
            'add_type': 1,  # 是否启用搜索牌号  1启用
            'circulation': 1,  # 智能搜索中 商品加载次数 50个为一次
            'goodsNumber': 0,  # 添加牌号下标
            'delivery_method': 2,  # 1配送 2自提
            'collage_num': 10,  # 集采量
            'overflow_num': 1,  # 溢出值
            'delivery_day': 5,  # 交货时间
            'delivery_price': 1000,  # 单价
            'deposit': 9,  # 定金
            'describe': '我是交易描述哦我是交易描述哦我是交易描述哦我是交易描述哦',  # 交易描述
            'brand': 'pp',  # 牌号
            'limit': 3,  # 循环次数
            'start_time': '2023-05-23 09:25',  # 开始时间
            'end_time': '2023-05-25 11:00',  # 结束时间
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
        goodsNumber = param['goodsNumber']
        delivery_method = param['delivery_method']
        collage_num = param['collage_num']
        overflow_num = param['overflow_num']
        delivery_day = param['delivery_day']
        delivery_price = param['delivery_price']
        deposit = param['deposit']
        describe = param['describe']
        limit = param['limit']
        brand = param['brand']
        start_time = param['start_time']
        end_time = param['end_time']
        log.info("开始时间: " + current_time)
        collage.seller_collage_release(serve, seller_phone, minimum, add_type, circulation, goodsNumber,
                                       delivery_method, collage_num, overflow_num, delivery_day, delivery_price,
                                       deposit, describe, limit, brand, start_time, end_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_collage_release.py'])
