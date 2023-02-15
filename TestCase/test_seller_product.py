#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbSellerGoodsAdd import JsbSellerGoodsAdd
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


@allure.feature('执行卖家添加制成品')
class TestSellerProduct:
    @allure.title('卖家添加制成品流程')
    def _seller_add_product(self, drivers):
        log.info('当前执行   卖家端添加制成品    ')
        seller = JsbSellerGoodsAdd(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = '24'
        sellerPhone = '18929867679'
        addGoods = '制成品'
        title = '制成品selenium'
        subtitle = '制成品1'
        keywords = '制成品关键词'
        code = 'zzz568'
        material = '塑料'
        brand = '自动化'
        needSign = 0
        producingArea = '福建'
        address = '制成品详细地址'
        sku_name = '规格1'
        sku_price = 30
        sku_min_purchase = 10
        sku_stock = 500
        sku_weight = 20
        profiles = '制成品内容概要'
        detail = '制成品详情'
        img_path = 'D:\\资料\\raw.png'
        video_path = 'D:\\资料\\video.mp4'
        limit = 1
        seller.seller_product_add(serve, sellerPhone, addGoods, title, subtitle, keywords, code, producingArea,
                                  needSign,
                                  material, brand, address, img_path, video_path, sku_name, sku_price, sku_min_purchase,
                                  sku_stock, sku_weight, profiles, detail, limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_product.py'])
