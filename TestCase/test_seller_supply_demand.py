#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import allure
import pytest

from page_object.JsbDemandPage import JsbDemand
from utils.log import Log
from utils.tool_util import time_lag

log = Log()


@allure.feature('卖家发布供需资讯')
class TestSellerSupplyDemand:
    test_data = [
        {
            'serve': '24',  # 环境
            'seller_phone': '18929867679',  # 买家账号
            'limit': '1',  # 循环次数
            'title': '出售原料 原厂原包',  # 供需标题
            'seller_num': 8,  # 卖家数量
            'price': 7054,  # 价格
            'num': 10,  # 数量
            'release_type': 2,  # 发布类型  2市场信息  1采购需求
            'video_path': 'D:\\资料\\video.mp4',  # 供需视频
            'content': '出售原厂原包原料',  # 供需详情
            'img_path': 'D:\\资料\\raw.png',  # 供需图片
            'grade_number': 0,  # 牌号下标
            'add_type': '1',  # 是否启用搜索牌号 1启用
            'number': 'pp',  # 牌号搜索
            'circulation': 1,  # 加载牌号次数 50为一次
        }
    ]

    @pytest.mark.parametrize('param', test_data)
    @allure.title('卖家发布供需资讯流程')
    def test_seller_supply(self, drivers, param):
        log.info('当前执行   卖家端发布供需    ')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        demand = JsbDemand(drivers)
        serve = param['serve']
        seller_phone = param['seller_phone']
        limit = param['limit']
        title = param['title']
        seller_num = param['seller_num']
        price = param['price']
        num = param['num']
        release_type = param['release_type']
        video_path = param['video_path']
        img_path = param['img_path']
        content = param['content']
        grade_number = param['grade_number']
        add_type = param['add_type']
        number = param['number']
        circulation = param['circulation']
        demand.seller_demand(serve, seller_phone, release_type, title, content, img_path, video_path, seller_num, price,
                             num, limit, grade_number, add_type, number, circulation)
        log.info("开始时间: " + current_time)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log.info("结束时间: " + now_time)
        lead_time = time_lag(now_time, current_time)
        log.info("共计使用时间: " + str(lead_time))


if __name__ == '__main__':
    pytest.main(['TestCase/test_seller_supply_demand.py'])
