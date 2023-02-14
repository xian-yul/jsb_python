#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbDemandPage import JsbDemand
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestSellerSupplyDemand:

    @allure.feature('卖家发布供需资讯')
    def test_seller_supply(self, drivers):
        log.info('当前执行   卖家端发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        demand = JsbDemand(drivers)
        serve = '24'
        seller_phone = '18929867679'
        release_type = 2  # 2市场信息  1采购需求
        limit = 2
        num = 5
        seller_num = 3
        price = 8950
        title = '卖家供需资讯'
        content = '测试测试测试测试测试测试测试测试'
        video_path = 'D:\\资料\\video.mp4'
        img_path = 'D:\\资料\\raw.png'
        grade_number = 0
        add_type = 1
        number = 'pp'
        circulation = 1
        demand.seller_demand(serve, seller_phone, release_type, title, content, img_path, video_path, seller_num, price,
                             num, limit, grade_number, add_type, number, circulation)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_supply_demand.py'])
