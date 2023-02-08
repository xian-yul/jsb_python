#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import pytest

from page_object.JsbDemandPage import JsbDemand
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
user_url = {'24': 'http://192.168.101.24:8090/shop/home', '20': 'https://demo.jinsubao.cn/'}
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestUserSupplyDemand:

    def test_user_supply(self, drivers):
        log.info('当前执行   买家发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        demand = JsbDemand(drivers)
        serve = '24'
        user_phone = '13500135000'
        limit = 1
        title = '测试买家供需资讯'
        seller_num = 1
        price = 5000
        num = 10
        release_type = 1    # 2市场信息  1采购需求
        video_path = 'D:\\资料\\video.mp4'
        content = '测试测试测试测试测试测试测试测试'
        img_path = 'D:\\资料\\raw.png'
        demand.user_demand(serve, user_phone, release_type, title, content, img_path, video_path, seller_num, price,
                           num, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_user_supply_demand.py'])
