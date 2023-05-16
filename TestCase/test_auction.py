#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbAuction import JsbAuction
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行卖家发布竞拍内容')
class TestAuction:

    @allure.title('卖家发布竞拍内容')
    def test_auction(self, drivers):
        log.info('当前执行   竞拍填写内容   ')
        serve = '24'
        grade_number = ''  # 添加牌号下标
        add_type = ''  # 是否启用搜索牌号  1启用
        number = ''  # 搜索牌号
        circulation = ''  # 智能搜索中 商品加载次数 50个为一次
        sellerPhone = ''
        grossQuantity = ''  # 标的总量
        startQuantity = ''  # 起拍量
        quantityIncrease = ''  # 数量增幅
        maxQuotationUnit = ''  # 最大报价单位
        startUnitPrice = ''  # 起拍单价
        upPrice = ''  # 加价幅度
        maxUpPrice = ''  # 最高加价幅度
        start_time: '2023-03-30 09:25'  # 开始时间
        end_time: '2023-04-10 11:00'  # 结束时间
        buyerSuretyRatio = ''  # 定金比例
        deliveryTime = ''  # 提货时间
        additionalProvisions = ''  # 附加条款
        auction = JsbAuction(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        auction.seller_auction(serve, grade_number, add_type, number, circulation, sellerPhone, grossQuantity,
                               startQuantity, quantityIncrease, maxQuotationUnit, startUnitPrice, upPrice, maxUpPrice,
                               start_time, end_time, buyerSuretyRatio, deliveryTime, additionalProvisions)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_auction.py'])