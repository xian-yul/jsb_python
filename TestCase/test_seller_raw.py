#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestSellerRaw:

    def test_seller_add_raw(self, drivers):
        log.info('当前执行   卖家端添加原料    ')
        seller = JsbPackagingMethod(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = '24'
        seller_phone = '15456821564'
        add_goods_type = '原料类型'
        grade_number = 0
        stock = 1000
        min_purchase = 10
        delivery_price = 1000
        deliver_area = '全国'
        deliver_day = '我是配送时间'
        pickup_day = '我是提货时间'
        deliver_type = 1
        pickup_price = 1000
        upload_img = 'D:\\资料\\raw.png'
        upload_video = 'D:\\资料\\video.mp4'
        unit_price_type = 1
        profiles = '我是原料商品内容概要'
        detail = '我是原料商品详情'
        limit = 10
        seller.seller_goods_add_raw_repeatedly(serve, seller_phone, add_goods_type, grade_number, stock, min_purchase,
                                               delivery_price,
                                               deliver_area, deliver_day, pickup_day,
                                               deliver_type,
                                               pickup_price,
                                               upload_img, upload_video, unit_price_type, profiles, detail, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_raw.py'])
