#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

import allure
import pytest

from page_object.JsbSellerGoodsAdd import JsbSellerGoodsAdd
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('执行卖家添加原料')
class TestSellerRaw:
    test_data = [
        {
            'serve': '24',  # 环境
            'sellerPhone': '18929867679',  # 卖家账号
            'addGoods': '原料',  # 添加类型 默认原料
            'goodsNumber': 7,  # 添加牌号下标
            'stockNum': 100,  # 商品库存
            'minPurchase': 1,  # 最低采购
            'deliveryPrice': 6573,  # 配送价格
            'deliveryDays': '我是配送时间',  # 配送时间
            'selfMentionDays': '我是提货时间',  # 提货时间
            'goodsDeliver': 3,  # 1单配送 2单自提 3配送+自提
            'included': 1,  # 是否含税  1含税
            'selfMentionPrice': 7895,  # 自提价格
            'add_type': 1,  # 是否启用搜索牌号  1启用
            'number': 'pp',  # 搜索牌号
            'img_path': 'D:\\资料\\raw.png',  # 商品图片
            'video_path': 'D:\\资料\\video.mp4',  # 商品视频
            'profiles': '原料商品内容概要',  # 商品内容概要
            'detail': '原料商品详情',  # 商品详情
            'circulation': 1,  # 智能搜索中 商品加载次数 50个为一次
            'limit': 1,
        },
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('卖家添加原料流程')
    def test_seller_add_raw(self, drivers, param):
        log.info('当前执行   卖家端添加原料    ')
        seller = JsbSellerGoodsAdd(drivers)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        serve = param['serve']
        sellerPhone = param['sellerPhone']
        addGoods = param['addGoods']
        goodsNumber = param['goodsNumber']
        stockNum = param['stockNum']
        minPurchase = param['minPurchase']
        deliveryPrice = param['deliveryPrice']
        deliveryDays = param['deliveryDays']
        selfMentionDays = param['selfMentionDays']
        goodsDeliver = param['goodsDeliver']
        included = param['included']
        selfMentionPrice = param['selfMentionPrice']
        add_type = param['add_type']
        number = param['number']
        img_path = param['img_path']
        profiles = param['profiles']
        video_path = param['video_path']
        detail = param['detail']
        limit = param['limit']
        circulation = param['circulation']
        seller.seller_raw_add(serve, sellerPhone, addGoods, goodsDeliver, included, stockNum, minPurchase,
                              deliveryPrice,
                              deliveryDays
                              , selfMentionPrice, selfMentionDays, profiles, detail, goodsNumber, video_path, img_path,
                              limit, add_type, number, circulation)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_raw.py'])
