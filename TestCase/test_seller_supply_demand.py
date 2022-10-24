#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestSellerSupplyDemand:

    def test_seller_supply(self, drivers):
        log.info('当前执行   卖家端发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        seller = JsbPackagingMethod(drivers)
        serve = '20'
        seller_phone = '18929867679'
        supply_type = 1
        limit = 1
        title = '卖家供需资讯'
        content = '测试测试测试测试测试测试测试测试'
        video_path = 'D:\\资料\\video.mp4'
        img_path = 'D:\\资料\\raw.png'
        seller.seller_supply_demand(serve, seller_phone, supply_type, limit, title, content, video_path, img_path)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_supply_demand.py'])
