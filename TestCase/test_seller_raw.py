#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from page_object.JsbSellerGoodsAdd import JsbSellerGoodsAdd
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestSellerRaw:

    def test_seller_add_raw(self, drivers):
        log.info('当前执行   卖家端添加原料    ')
        seller = JsbSellerGoodsAdd(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = '24'
        sellerPhone = '18454376874'
        addGoods = '原料'
        goodsNumber = 90
        stockNum = 1000
        minPurchase = 10
        deliveryPrice = 6500
        deliveryDays = '我是配送时间'
        selfMentionDays = '我是提货时间'
        goodsDeliver = 2
        included = 1
        selfMentionPrice = 7800
        img_path = 'D:\\资料\\raw.png'
        video_path = 'D:\\资料\\video.mp4'
        profiles = '我是原料商品内容概要'
        detail = '我是原料商品详情'
        limit = 1
        seller.seller_raw_add(serve, sellerPhone, addGoods, goodsDeliver, included, stockNum, minPurchase,
                              deliveryPrice,
                              deliveryDays
                              , selfMentionPrice, selfMentionDays, profiles, detail, goodsNumber, video_path, img_path,
                              limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_raw.py'])
