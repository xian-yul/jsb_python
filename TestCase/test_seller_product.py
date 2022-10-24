#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import pytest

from page_object.JsbPackagingMethod import JsbPackagingMethod
from utils.log import Log
from utils.tool_util import time_lag

log = Log()
seller_url = {'24': 'http://192.168.101.24:8070/user/login', '20': 'https://slrdm.jinsubao.cn/'}


class TestSellerProduct:

    def test_seller_add_product(self, drivers):
        log.info('当前执行   卖家端添加制成品    ')
        seller = JsbPackagingMethod(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = '20'
        seller_phone = '18965691361'
        goods_type = '制成品类型'
        title = '制成品selenium'
        subtitle = '制成品1'
        keywords = '制成品关键词'
        code = 'zzz568'
        material = '塑料'
        brand = '自动化'
        need_sign_type = 0
        address = '制成品详细地址'
        sku_img = 'D:\\资料\\raw.png'
        sku_name = '规格1'
        sku_price = 30
        sku_min_purchase = 1
        sku_stock = 500
        sku_weight = 20
        sku_remark = '无备注'
        profiles = '制成品内容概要'
        detail = '制成品详情'
        img_path = 'D:\\资料\\raw.png'
        video_path = 'D:\\资料\\video.mp4'
        limit = 10
        seller.seller_goods_add_product_repeatedly(serve, seller_phone, goods_type, title, subtitle, keywords, code,
                                                   material, brand,
                                                   need_sign_type, address, sku_img, sku_name, sku_price,
                                                   sku_min_purchase, sku_stock,
                                                   sku_weight, sku_remark, img_path, video_path, profiles, detail,
                                                   limit)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_product.py'])
