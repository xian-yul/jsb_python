#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import pytest

from page_object.JsbSellerGoodsAdd import JsbSellerGoodsAdd
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


class TestSellerRaw:

    def test_seller_add_raw(self, drivers):
        log.info('当前执行   卖家端添加原料    ')
        seller = JsbSellerGoodsAdd(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = '20'
        sellerPhone = '18970712256'
        addGoods = '原料'
        goodsNumber = 0
        stockNum = 1000
        minPurchase = 10
        deliveryPrice = 10000
        deliveryDays = '我是配送时间'
        selfMentionDays = '我是提货时间'
        goodsDeliver = 1
        included = 1
        selfMentionPrice = 20000
        add_type = 1
        number = '【南通星辰】ER | 0164'
        img_path = 'D:\\资料\\raw.png'
        video_path = 'D:\\资料\\video.mp4'
        profiles = '我是原料商品内容概要'
        detail = '我是原料商品详情'
        limit = 1
        seller.seller_raw_add(serve, sellerPhone, addGoods, goodsDeliver, included, stockNum, minPurchase,
                              deliveryPrice,
                              deliveryDays
                              , selfMentionPrice, selfMentionDays, profiles, detail, goodsNumber, video_path, img_path,
                              limit, add_type, number)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_raw.py'])
